import sys, os, numpy as np, pandas as pd
D=sys.argv[1]; exec(open(os.path.dirname(os.path.abspath(__file__))+'/tab.py').read().split("if __name__")[0])
P=pd.read_pickle(D+'/P3.pkl').reset_index(drop=True)
P=P.merge(pd.read_parquet(D+'/employer.parquet'),on=['fsu_serial_no','sample_hh_no','person_serial_no'],how='left')
GRP=['paid work','commute','domestic','care','leisure/media','social/relig','eat/selfcare','sleep']
G['g2']=G.g.where(G.g.isin(GRP),'other')
# per-person metrics
key=P[k].copy(); key['i']=np.arange(len(P)); G=G.merge(key,on=k)
n=len(P)
slot=np.zeros((n,48),bool)   # paid work by slot
w_=G[G.g=='paid work']; slot[w_.i.values,w_.slot.values]=True
def mat(lo,hi):
    out={}
    for g_ in GRP+['other']:
        x=G[(G.g2==g_)&(G.slot>=lo)&(G.slot<hi)].groupby('i').size().reindex(range(n),fill_value=0).values*30
        out[g_]=x
    return pd.DataFrame(out)
EVE=mat(26,40); DAY=mat(0,48)
psu=(P.nss_region.astype(str)+'_'+P.sector+'_'+P.fsu_serial_no.astype(str)).values
strata=(P.nss_region.astype(str)+'_'+P.sector).values
fsu_codes,fsu_idx=np.unique(psu,return_inverse=True)
fsu_strata=pd.Series(strata).groupby(fsu_idx).first().values
rng=np.random.default_rng(7)
# precompute strata -> list of fsu ids
sl={s:np.where(fsu_strata==s)[0] for s in np.unique(fsu_strata)}
def draw():
    c=np.zeros(len(fsu_codes))
    for s,ids in sl.items():
        pick=rng.choice(ids,len(ids)); np.add.at(c,pick,1)
    return c[fsu_idx]

B=300; M=np.array([draw() for _ in range(B)])
W=P.w.values
P['ageb']=pd.cut(P.age,[0,24,34,49,120],labels=['<25','25-34','35-49','50+']).astype(str)
P['married']=np.where(P.marital_status=='currently married','married','not married')
P['qt']=P.q.map({1:'Q1-2',2:'Q1-2',3:'Q3',4:'Q4-5',5:'Q4-5'})
SPL_OLD={'sector':'sector','age':'ageb','marital':'married','social group':'sg','religion':'rel','MPCE (grouped)':'qt','care need in HH':'care_hh'}
SPL={'employer':'emp'}
COHS={'all salaried':np.ones(n,bool),'KW core':P.kw_core.fillna(False).to_numpy(bool),'KW broad':P.kw_broad.fillna(False).to_numpy(bool),'WC (03 essay)':P.wc03.fillna(False).to_numpy(bool)}
work=(P.dtype=='work').values
VW={'paid work':EVE['paid work'].values,'domestic':EVE['domestic'].values,'care':EVE['care'].values,'leisure':EVE['leisure/media'].values,'%work@5pm':slot[:,26]*100.,'%work@7pm':slot[:,30]*100.}
VO={'paid work':DAY['paid work'].values,'domestic':DAY['domestic'].values,'care':DAY['care'].values,'leisure':DAY['leisure/media'].values}

nic=P.nic2.astype('Int64').fillna(-1).astype(int).values
grad=P.grad.values.astype(bool)
sect=np.where(P.emp=='public','pub',np.where(P.emp.isin(['private corporate','private small']),'prv','x'))
VARS={'paid work':VW['paid work'],'domestic':VW['domestic'],'care':VW['care'],'leisure':VW['leisure'],'%work@5pm':VW['%work@5pm'],'%work@7pm':VW['%work@7pm']}
def wmean_b(mask,x):
    ww=W*mask; e=(ww*x).sum()/ww.sum(); bs=(M@(ww*x))/(M@ww); return e,bs
def fmt(e,bs): lo,hi=np.percentile(bs,[2.5,97.5]); return f'{e:.0f} [{lo:.0f},{hi:.0f}]'
out=[]
for gn,gm in [('F',(P.gender=='female').values),('M',(P.gender=='male').values)]:
    base=work&gm
    # A) single industries
    for nm,im in [('education 85',nic==85),('health 86',nic==86),('finance 64',nic==64),('mfg 10-33',(nic>=10)&(nic<=33))]:
        for v,x in VARS.items():
            r={'g':gn,'ind':nm,'var':v}
            ms={}
            for sc in ['pub','prv']:
                m=base&im&(sect==sc); r['n_'+sc]=int(m.sum())
                if m.sum()>=30: ms[sc]=wmean_b(m,x); r[sc]=fmt(*ms[sc])
            if len(ms)==2: d=ms['pub'][0]-ms['prv'][0]; db=ms['pub'][1]-ms['prv'][1]; r['pub-prv']=fmt(d,db)
            out.append(r)
    # B) adjusted: strata = NIC2 x graduate; weights = public worker weight share
    strata=nic*2+grad
    cells=[]
    for s_ in np.unique(strata):
        mp=base&(strata==s_)&(sect=='pub'); mq=base&(strata==s_)&(sect=='prv')
        if mp.sum()>=20 and mq.sum()>=20: cells.append((mp,mq))
    covpub=sum((W*mp).sum() for mp,_ in cells)/ (W*(base&(sect=='pub'))).sum()
    for v,x in VARS.items():
        tw=np.array([ (M@(W*mp)) for mp,_ in cells]); tw=tw/tw.sum(0)           # bootstrap public weights share (cells x B)
        dpb=np.array([ (M@(W*mp*x))/(M@(W*mp)) - (M@(W*mq*x))/(M@(W*mq)) for mp,mq in cells])
        adjb=(tw*dpb).sum(0)
        t0=np.array([(W*mp).sum() for mp,_ in cells]); t0=t0/t0.sum()
        d0=np.array([ (W*mp*x).sum()/(W*mp).sum()-(W*mq*x).sum()/(W*mq).sum() for mp,mq in cells]); adj=(t0*d0).sum()
        raw=wmean_b(base&(sect=='pub'),x)[0]-wmean_b(base&(sect=='prv'),x)[0]
        rb=wmean_b(base&(sect=='pub'),x)[1]-wmean_b(base&(sect=='prv'),x)[1]
        out.append({'g':gn,'ind':f'ADJUSTED ({len(cells)} NIC x grad cells, covers {covpub*100:.0f}% of public)','var':v,'raw pub-prv':fmt(raw,rb),'adj pub-prv':fmt(adj,adjb)})
import pandas as pd
df=pd.DataFrame(out); df.to_csv(D+'/within_ind.csv',index=False)
pd.set_option('display.width',250); pd.set_option('display.max_rows',300); pd.set_option('display.max_colwidth',60)
print(df.to_string())
