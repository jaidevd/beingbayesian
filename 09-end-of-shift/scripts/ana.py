import sys, numpy as np, pandas as pd
D=sys.argv[1]; pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
P=pd.read_parquet(D+'/persons.parquet'); G=pd.read_parquet(D+'/grid.parquet')
k=['fsu_serial_no','sample_hh_no','person_serial_no']
grad={'graduate','post graduate and above','diploma/certificate course(graduation & above)'}
P['grad']=P.education.isin(grad)
IND5=['Manufacturing and construction','Trade, transport and hospitality','Knowledge services','Education, health and administration','Other industries']
def ind5(x):   # a clean partition of the NIC-2008 divisions
    if pd.isna(x): return IND5[4]
    x=int(x)
    if 10<=x<=33 or 41<=x<=43: return IND5[0]
    if 45<=x<=56: return IND5[1]
    if 58<=x<=66 or 69<=x<=75: return IND5[2]
    if 84<=x<=88: return IND5[3]
    return IND5[4]
P['ind5']=P.nic2.map(ind5)
P['dtype']=np.where(P.type_of_day=='normal day','work','off')
P['cal']=np.where(P.day_of_week.isin(['Saturday','Sunday']),'SatSun','MonFri')
P['ageb']=pd.cut(P.age,[0,24,34,49,120],labels=['<25','25-34','35-49','50+'])
P['married']=np.where(P.marital_status=='currently married','married','not married')
P['wk']=P.sector  # alias
ic=pd.read_csv(D+'/../conv/ICATUS-2016-Sheet1.csv',dtype=str)
div={'1':'employment','2':'own-use goods','3':'unpaid domestic','4':'unpaid care','5':'volunteer','6':'learning','7':'social/community/religion','8':'leisure/media/sport','9':'self-care'}
t3=ic[ic.CID.notna()].set_index('CID').Title.str[:55].to_dict()
G=G.merge(P[k+['w']],on=k); G['d1']=(G.act//100).astype('Int64').astype(str).map(div)
G['emp']=G.act.between(110,150)
def sel(name):
    return {'all':P.index==P.index,**{g:P.ind5==g for g in IND5},'nongrad':~P.grad}[name]
def run(mask,lo,hi,label,top=0):
    ids=P[mask][k+['w']]; g=G.merge(ids[k],on=k); w=ids.w.sum()
    g=g[(g.slot>=lo)&(g.slot<hi)]
    m=g.groupby('d1').w.sum()/w*30/ (1)   # minutes per person within window
    return m, ids
print('N salaried',len(P)); print(P.groupby(['dtype','cal']).size().unstack())
for c in ['all']+IND5+['nongrad']:
    m=sel(c); print(c,m.sum(),'work',(m&(P.dtype=='work')).sum(),'off',(m&(P.dtype=='off')).sum(),'wtd share female',round(np.average(P[m].gender=='female',weights=P[m].w),3),'urban',round(np.average(P[m].sector=='Urban',weights=P[m].w),3))
P.to_pickle(D+'/P2.pkl'); G.to_pickle(D+'/G2.pkl')
