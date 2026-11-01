import sys, pandas as pd, numpy as np
D=sys.argv[1]
c=['usual_principal_activity_status','person_response_code','enterprise_type','time_from','time_to']
r=pd.read_parquet('/home/jaidevd/src/time-use-survey-2024/clean/per-tus-2024.parquet',columns=c)
r=r[r.usual_principal_activity_status.fillna('').str.contains('regular salaried')&(r.person_response_code=='cooperative')].reset_index()
k=['fsu_serial_no','sample_hh_no','person_serial_no']
mn=lambda s:s.str[:2].astype(int)*60+s.str[3:5].astype(int)
a=(mn(r.time_from)-240)%1440; b=(mn(r.time_to)-240)%1440; b=np.where(b<=a,b+1440,b); r['dur']=b-a
m=r[r.enterprise_type.notna()].groupby(k+['enterprise_type']).dur.sum().reset_index()
top=m.sort_values('dur').groupby(k).tail(1).set_index(k).enterprise_type
mp={'Government/local body':'public','Autonomous Bodies':'public','Public/Private limited company':'private corporate','proprietary':'private small','partnership':'private small'}
lab=top.map(lambda x: mp.get(x,'other')).rename('emp').reset_index()
lab.to_parquet(D+'/employer.parquet'); print(lab.emp.value_counts())
