import sys, numpy as np, pandas as pd
R='/home/jaidevd/src/time-use-survey-2024/clean/'; O=sys.argv[1]
cols=['sector','nss_region','relation_to_hoh','gender','age','marital_status','education','usual_principal_activity_status',
 'nic_2008_principal_activity','day_of_week','type_of_day','person_response_code','activity_srl_no','time_from','time_to',
 'major_minor_activity','activity_code','paid_unpaid_status','where_activity_performed','mult']
p=pd.read_parquet(R+'per-tus-2024.parquet',columns=cols)
p=p[p.usual_principal_activity_status.fillna('').str.contains('regular salaried')]
p=p[p.person_response_code=='cooperative'].reset_index()
print('persons',p.groupby(['fsu_serial_no','sample_hh_no','person_serial_no']).ngroups, 'rows',len(p))
def mins(s): return s.str[:2].astype(int)*60+s.str[3:5].astype(int)
a=(mins(p.time_from)-240)%1440; b=(mins(p.time_to)-240)%1440
b=np.where(b<=a,b+1440,b); p['a']=a; p['b']=b; p['dur']=b-a
print(p.dur.describe(), (p.a%30!=0).mean())
# per-person total minutes check (major only)
k=['fsu_serial_no','sample_hh_no','person_serial_no']
mj=p[p.major_minor_activity=='major']
tot=mj.groupby(k).dur.sum(); print(tot.describe()); print((tot==1440).mean())
p.to_parquet(O+'/sal_rows.parquet')
