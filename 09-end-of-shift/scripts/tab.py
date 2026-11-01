import sys, numpy as np, pandas as pd
D=sys.argv[1]; pd.set_option('display.width',250); pd.set_option('display.max_columns',40); pd.set_option('display.max_rows',300)
P=pd.read_pickle(D+'/P2.pkl'); G=pd.read_pickle(D+'/G2.pkl')
k=['fsu_serial_no','sample_hh_no','person_serial_no']
def grp(a):
    if 110<=a<=150: return 'paid work'
    if a in (181,182): return 'commute'
    if a<200: return 'other emp'
    if a<300: return 'own-use prod'
    if a<400: return 'domestic'
    if a<500: return 'care'
    if a<600: return 'volunteer'
    if a<700: return 'learning'
    if a<800: return 'social/relig'
    if a<900: return 'leisure/media'
    if a==911: return 'sleep'
    return 'eat/selfcare'
G['g']=G.act.map(lambda a: grp(int(a)) if pd.notna(a) else 'unk')
G=G.drop(columns=['w'])
COH={'all salaried':P.index==P.index,'KW broad':P.kw_broad,'KW core':P.kw_core,'blue (mfg/constr/trade/transp)':P.blue,'non-graduate':~P.grad}
def prof(mask,lo,hi):
    ids=P[mask]
    if len(ids)<40: return None
    W=ids.w.sum(); x=G.merge(ids[k+['w']],on=k); y=x[(x.slot>=lo)&(x.slot<hi)]
    m=(y.groupby('g').w.sum()/W*30)
    out={'n':len(ids)}
    for g_ in ['paid work','commute','domestic','care','leisure/media','social/relig','eat/selfcare','sleep','learning']: out[g_]=round(m.get(g_,0))
    # employed share at slots
    for s,l in [(26,'5pm'),(28,'6pm'),(30,'7pm'),(32,'8pm'),(34,'9pm')]:
        z=x[(x.slot==s)&(x.g=='paid work')]; out['%work@'+l]=round(z.w.sum()/W*100)
    return out
def table(splits,dt,lo,hi,base=None):
    rows={}
    for cn,cm in COH.items():
        for sn,sm in splits.items():
            mm=cm&sm&(P.dtype==dt if dt else True)
            if base is not None: mm&=base
            r=prof(mm,lo,hi)
            if r: rows[(cn,sn)]=r
    return pd.DataFrame(rows).T
if __name__=='__main__':
    which=sys.argv[2]
    one={'ALL':P.index==P.index}
    gen={'F':P.gender=='female','M':P.gender=='male'}
    if which=='q1gender': print(table({**one,**gen},'work',26,40))
    if which=='q1other':
        sp={'rural':P.sector=='Rural','urban':P.sector=='Urban','<25':P.ageb=='<25','25-34':P.ageb=='25-34','35-49':P.ageb=='35-49','50+':P.ageb=='50+','married':P.married=='married','not married':P.married=='not married'}
        for gname,gm in [('F',P.gender=='female'),('M',P.gender=='male')]:
            print('###',gname); print(table(sp,'work',26,40,gm)[['n','paid work','commute','domestic','care','leisure/media','social/relig','%work@5pm','%work@7pm','%work@8pm']])
