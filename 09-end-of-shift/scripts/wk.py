import sys; A=sys.argv[1]; sys.argv=[sys.argv[0],A,'none']
exec(open(sys.argv[0].replace('wk.py','tab.py')).read().split("if __name__")[0])
ic=pd.read_csv(D+'/../conv/ICATUS-2016-Sheet1.csv',dtype=str); t3=ic[ic.CID.notna()].set_index('CID').Title.str[:46].to_dict()
GR=['paid work','commute','domestic','care','leisure/media','social/relig','eat/selfcare','learning','own-use prod','volunteer']
def wprof(mask):
    ids=P[mask]
    if len(ids)<40: return None
    W=ids.w.sum(); x=G.merge(ids[k+['w']],on=k)
    m=x.groupby('g').w.sum()/W*30; o={'n':len(ids)}
    for g_ in GR: o[g_]=round(m.get(g_,0))
    o['sleep']=round(m.get('sleep',0))
    pp=x[x.g.isin(GR)].drop_duplicates(k+['g']).groupby('g').w.sum()/W*100
    for g_ in ['paid work','domestic','care','leisure/media','social/relig','learning']: o['%'+g_[:6]]=round(pp.get(g_,0))
    return o
def tbl(day,splits=None):
    splits=splits or {'ALL':P.index==P.index,'F':P.gender=='female','M':P.gender=='male'}
    rows={}
    for cn,cm in COH.items():
        for sn,sm in splits.items():
            r=wprof(cm&sm&day)
            if r: rows[(cn,sn)]=r
    return pd.DataFrame(rows).T
cut=lambda m:m
off=P.dtype=='off'
print('##### OFF DAYS (type_of_day=other), any weekday'); print(tbl(off))
print('##### Calendar Sat/Sun, normal day (i.e. they work)'); print(tbl((P.cal=='SatSun')&(P.dtype=='work')))
print('##### Calendar Sun, other day'); print(tbl((P.day_of_week=='Sunday')&off))
print('##### Mon-Fri OFF days: share of all off days (weighted) by weekday')
for cn,cm in COH.items():
    ids=P[cm&off]; print(cn,(ids.groupby('day_of_week').w.sum()/ids.w.sum()*100).round(0).reindex(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']).to_dict())
print('##### share of salaried-day respondents on a normal day, Sat & Sun')
for cn,cm in COH.items():
    r={}
    for d in ['Saturday','Sunday']:
        ids=P[cm&(P.day_of_week==d)]; r[d]=round(ids[ids.dtype=='work'].w.sum()/ids.w.sum()*100)
    print(cn,r)
print('##### Top codes on off-days, awake time, F vs M')
for cn in ['all salaried','KW core','KW broad']:
    for gn,gm in [('F',P.gender=='female'),('M',P.gender=='male')]:
        ids=P[COH[cn]&gm&off]; x=G.merge(ids[k+['w']],on=k); W=ids.w.sum()
        s=(x.groupby('act').w.sum()/W*30).sort_values(ascending=False).head(12)
        print(cn,gn,[(int(a),t3.get(str(int(a)),'?')[:28],round(v)) for a,v in s.items() if int(a)!=911][:9])
