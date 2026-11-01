import sys, numpy as np, pandas as pd
D=sys.argv[1]; pd.set_option('display.width',250); pd.set_option('display.max_columns',40); pd.set_option('display.max_rows',200)
P=pd.read_pickle(D+'/P2.pkl'); G=pd.read_pickle(D+'/G2.pkl')
k=['fsu_serial_no','sample_hh_no','person_serial_no']
ic=pd.read_csv(D+'/../conv/ICATUS-2016-Sheet1.csv',dtype=str); t3=ic[ic.CID.notna()].set_index('CID').Title.str[:48].to_dict()
def cohort(c): return {'all':P.index==P.index,'kw_broad':P.kw_broad,'kw_core':P.kw_core,'blue':P.blue}[c]
def emp_share(ids,slots,g):
    # weighted share in employment (110-150) at each slot
    x=g[g.slot.isin(slots)]; return {s:(x[(x.slot==s)&x.emp].w.sum()/ids.w.sum()) for s in slots}
def block(c,dt,extra=None,lo=26,hi=40):
    m=cohort(c)&(P.dtype==dt)
    if extra is not None: m&=extra
    ids=P[m]; g=G.merge(ids[k],on=k,suffixes=('','_x'))
    if 'w_x' in g: g=g.drop(columns='w_x')
    return ids,g
def report(c,dt,extra=None,name='',lo=26,hi=40):
    ids,g=block(c,dt,extra); W=ids.w.sum()
    if len(ids)<30: return f'{name}: n={len(ids)} too thin'
    gw=g[(g.slot>=lo)&(g.slot<hi)]
    mins=(gw.groupby('d1').w.sum()/W*30).round(0)
    part=(gw.groupby('d1').apply(lambda x:x.drop_duplicates(k).w.sum())/W*100).round(0)
    es=emp_share(ids,[26,28,30,32,34],g)
    return name,len(ids),mins.sort_values(ascending=False).to_dict(),es
def top3(c,dt,lo,hi,extra=None,n=8):
    ids,g=block(c,dt,extra); W=ids.w.sum(); gw=g[(g.slot>=lo)&(g.slot<hi)]
    s=(gw.groupby('act').w.sum()/W*30).sort_values(ascending=False).head(n)
    return [(int(a),t3.get(str(int(a)),'?'),round(v)) for a,v in s.items()]
if __name__=='__main__':
    print('=== evening 17:00-24:00 on WORK days: minutes per person by ICATUS division; employed-share at 17,18,19,20,21')
    for c in ['all','kw_broad','kw_core','blue']:
        for gname,ex in [('all',None),('F',P.gender=='female'),('M',P.gender=='male')]:
            r=report(c,'work',ex,f'{c}/{gname}'); print(r)
    print('--- top 3-digit evening work-day',)
    for c in ['all','kw_core']:
        for gname,ex in [('F',P.gender=='female'),('M',P.gender=='male')]: print(c,gname,top3(c,'work',26,40,ex))
    print('=== exactly 17:00-17:30 on work days: share by division')
    for c in ['all','kw_core']:
        ids,g=block(c,'work'); x=g[g.slot==26]; print(c,(x.groupby('d1').w.sum()/ids.w.sum()*100).round(0).sort_values(ascending=False).to_dict())
        print('  top codes',[(int(a),t3.get(str(int(a)),'?'),round(v/ids.w.sum()*100)) for a,v in x.groupby('act').w.sum().sort_values(ascending=False).head(6).items()])
