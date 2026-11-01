import sys, os, numpy as np, pandas as pd
D=sys.argv[1]; exec(open(os.path.dirname(os.path.abspath(__file__))+'/tab.py').read().split("if __name__")[0])
P=pd.read_pickle(D+'/P3.pkl').reset_index(drop=True)
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
SPL={'sector':'sector','age':'ageb','marital':'married','social group':'sg','religion':'rel','MPCE (grouped)':'qt','care need in HH':'care_hh'}
COHS={'all salaried':np.ones(n,bool),'KW core':P.kw_core.fillna(False).to_numpy(bool),'KW broad':P.kw_broad.fillna(False).to_numpy(bool),'WC (03 essay)':P.wc03.fillna(False).to_numpy(bool)}
work=(P.dtype=='work').values
VW={'paid work':EVE['paid work'].values,'domestic':EVE['domestic'].values,'care':EVE['care'].values,'leisure':EVE['leisure/media'].values,'%work@5pm':slot[:,26]*100.,'%work@7pm':slot[:,30]*100.}
VO={'paid work':DAY['paid work'].values,'domestic':DAY['domestic'].values,'care':DAY['care'].values,'leisure':DAY['leisure/media'].values}
rows=[]
def cell(mask,V,day,cn,sn,v,gn,minn):
    mask=np.asarray(mask,dtype=bool); nn=int(mask.sum())
    if nn<minn: return
    ww=W*mask; den=M@ww; r={'day':day,'cohort':cn,'split':sn,'value':v,'gender':gn,'n':nn}
    for name,x in V.items():
        e=(ww*x).sum()/ww.sum(); bs=(M@(ww*x))/den; lo,hi=np.percentile(bs,[2.5,97.5]); r[name]=f'{e:.0f} [{lo:.0f}-{hi:.0f}]'
    rows.append(r)
for gn,gm in [('F',(P.gender=='female').values),('M',(P.gender=='male').values)]:
  for cn,cm in COHS.items():
    for sn,col in SPL.items():
      for v in sorted(P[col].dropna().unique()):
        vm=(P[col]==v).fillna(False).to_numpy(bool)
        cell(cm&gm&vm&work,VW,'work',cn,sn,v,gn,40)
        cell(cm&gm&vm&~work,VO,'off',cn,sn,v,gn,100)
import pandas as pd
df=pd.DataFrame(rows); df.to_csv(D+'/splits_ci.csv',index=False); print(len(df))
