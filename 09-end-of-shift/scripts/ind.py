import sys; sys.argv=[sys.argv[0],sys.argv[1],'none']
exec(open(sys.argv[0].replace('ind.py','tab.py')).read().split("if __name__")[0])
grad_=P.grad
ind={'IT/telecom/media 58-63':P.nic2.between(58,63),'finance/insur 64-66':P.nic2.between(64,66),'prof/sci/tech 69-75':P.nic2.between(69,75),'public admin 84':P.nic2==84,'education 85':P.nic2==85,'health 86':P.nic2==86,'office/support 82':P.nic2==82,'retail 47':P.nic2==47,'mfg 10-33':P.nic2.between(10,33),'security/invest 80':P.nic2==80}
rows={}
for n,m in ind.items():
    for gn,gm in [('all grad+',grad_),('all non-grad',~grad_)]:
        r=prof(m&gm&(P.dtype=='work'),26,40)
        if r: rows[(n,gn)]=r
print(pd.DataFrame(rows).T[['n','paid work','commute','domestic','care','leisure/media','%work@5pm','%work@6pm','%work@7pm','%work@8pm']])
# median finish: last paid-work slot end
x=G.merge(P[P.dtype=='work'][k+['w','kw_core','kw_broad','blue','gender']],on=k)
w=x[x.g=='paid work']; last=w.groupby(k).slot.max().rename('last').reset_index().merge(P[k+['w','kw_core','kw_broad','blue','gender','nic2','grad']],on=k)
def wmed(df): 
    o=df.sort_values('last'); c=o.w.cumsum()/o.w.sum(); return o['last'][c>=.5].iloc[0]
def fmt(s): t=((s+1)*30+240)%1440; return f'{t//60:02d}:{t%60:02d}'
for nm,m in [('all',last['last']>=0),('KW core',last.kw_core),('KW broad',last.kw_broad),('blue',last.blue)]:
    d=last[m]; print(nm,'median end of last paid-work slot',fmt(wmed(d)),'; share finishing by 17:00', round(d[d['last']<=25].w.sum()/d.w.sum()*100),'%; by 18:00',round(d[d['last']<=27].w.sum()/d.w.sum()*100),'%')
