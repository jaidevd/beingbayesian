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
B=300; mult=[draw() for _ in range(B)]
W=P.w.values
def est(mask,fn,reps=True):
    base=fn(W*mask)
    bs=np.array([fn(W*m*mask) for m in mult]) if reps else None
    return base,bs
def ratio_slot(sl_):
    return lambda ww:(ww*slot[:,sl_]).sum()/ww.sum()*100
def ratio_cols(df,col):
    v=df[col].values; return lambda ww:(ww*v).sum()/ww.sum()
def ci(bs): return np.percentile(bs,[2.5,97.5])
import pickle
res={'slots':{}, 'eve':{}, 'off':{}}
COHS={'all salaried':P.index>=0,'KW core':P.kw_core.values,'KW broad':P.kw_broad.values,'WC (03 essay)':P.wc03.values,'blue-collar':P.blue.values}
work=(P.dtype=='work').values; off=~work
for cn,cm in COHS.items():
    cm=np.asarray(cm)
    for s in range(22,40):
        b,bs=est(cm&work,ratio_slot(s)); res['slots'][(cn,s)]=(b,*ci(bs))
    for gn,gm in [('F',(P.gender=='female').values),('M',(P.gender=='male').values)]:
        for g_ in GRP:
            b,bs=est(cm&work&gm,ratio_cols(EVE,g_)); res['eve'][(cn,gn,g_)]=(b,*ci(bs))
            b,bs=est(cm&off&gm,ratio_cols(DAY,g_)); res['off'][(cn,gn,g_)]=(b,*ci(bs))
        res.setdefault('n',{})[(cn,gn)]=(int((cm&work&gm).sum()),int((cm&off&gm).sum()))
pickle.dump(res,open(D+'/boot.pkl','wb'))
for cn in COHS:
    print(cn,'5pm',[round(x,1) for x in res['slots'][(cn,26)]],'7pm',[round(x,1) for x in res['slots'][(cn,30)]])
    for gn in 'FM': print('  eve domestic',gn,[round(x) for x in res['eve'][(cn,gn,'domestic')]],' off domestic',[round(x) for x in res['off'][(cn,gn,'domestic')]],'off leisure',[round(x) for x in res['off'][(cn,gn,'leisure/media')]],res['n'][(cn,gn)])
