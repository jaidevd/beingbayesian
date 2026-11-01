import sys; A=sys.argv[1]; sys.argv=[sys.argv[0],A,'none']
import os
exec(open(os.path.dirname(os.path.abspath(__file__))+'/tab.py').read().split("if __name__")[0])
P=pd.read_pickle(D+'/P3.pkl')
GR=['paid work','domestic','care','leisure/media','social/relig']
def wp(mask):
    ids=P[mask]
    if len(ids)<100: return None
    W=ids.w.sum(); x=G.merge(ids[k+['w']],on=k); m=x.groupby('g').w.sum()/W*30
    return {'n':len(ids),**{g:round(m.get(g,0)) for g in GR}}
P['qt']=P.q.map({1:'Q1-2',2:'Q1-2',3:'Q3',4:'Q4-5',5:'Q4-5'})
off=P.dtype=='off'
for sn,col in {'social group':'sg','religion':'rel','MPCE (grouped)':'qt','care need in HH':'care_hh'}.items():
  for gn,gm in [('F',P.gender=='female'),('M',P.gender=='male')]:
    rows={}
    for cn,cm in {'all salaried':P.index==P.index,'KW broad':P.kw_broad,'WC (03)':P.wc03}.items():
        for v in sorted(P[col].dropna().unique()):
            r=wp(cm&gm&off&(P[col]==v))
            if r: rows[(cn,v)]=r
    print('## OFF DAY',sn,gn); print(pd.DataFrame(rows).T)
