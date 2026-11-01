import sys, numpy as np, pandas as pd
D=sys.argv[1]; R='/home/jaidevd/src/time-use-survey-2024/clean/'
p=pd.read_parquet(D+'/sal_rows.parquet'); k=['fsu_serial_no','sample_hh_no','person_serial_no']
mj=p[p.major_minor_activity=='major'].copy()
mj['n']=mj.dur//30; mj['s0']=mj.a//30
g=mj.loc[mj.index.repeat(mj.n)].copy()
g['slot']=g.s0+g.groupby(level=0).cumcount(); g['slot']%=48
g['act']=g.activity_code.astype('Int64')
g=g[k+['slot','act','where_activity_performed','paid_unpaid_status']]
# person table
pp=p.groupby(k).first().reset_index()[k+['sector','nss_region','relation_to_hoh','gender','age','marital_status','education','nic_2008_principal_activity','day_of_week','type_of_day','mult']]
pp['w']=pp.mult/100
pp['state']=(pp.nss_region.astype(str).str.zfill(3).str[:2])
h=pd.read_parquet(R+'hh-tus-2024.parquet',columns=['sector','hh_size','total_monthly_ce','social_group','religion','special_care_needed_in_hh','caregiver_available_in_hh','mult']).reset_index()
h['mpce']=h.total_monthly_ce/h.hh_size
def wq(df):
    o=df.sort_values('mpce'); c=o.mult.cumsum()/o.mult.sum()
    return pd.Series(np.minimum((c*5).apply(np.ceil),5).values,index=o.index)
h['q']=h.groupby('sector',group_keys=False).apply(wq)
pp=pp.merge(h[['fsu_serial_no','sample_hh_no','social_group','religion','special_care_needed_in_hh','caregiver_available_in_hh','hh_size','q']],on=['fsu_serial_no','sample_hh_no'],how='left')
pp['nic2']=pp.nic_2008_principal_activity.astype('Int64')
print(pp.nic2.isna().sum(), pp.q.isna().sum(), len(pp))
print(pp.nic2.value_counts().sort_index().to_string())
pp.to_parquet(D+'/persons.parquet'); g.to_parquet(D+'/grid.parquet'); print(len(g), g.groupby(k).size().describe())
