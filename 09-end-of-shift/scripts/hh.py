import sys; A=sys.argv[1]; sys.argv=[sys.argv[0],A,'none']
exec(open(sys.argv[0].replace('hh.py','tab.py')).read().split("if __name__")[0])
import yaml
wc03=set(int(str(k)) for k in yaml.safe_load(open(D+'/nic-white-collar.yaml')).keys())
P['wc03']=P.nic2.isin(wc03)&P.age.between(15,60)
COH2={'all salaried':P.index==P.index,'KW core':P.kw_core,'KW broad':P.kw_broad,'WC (03 essay)':P.wc03}
P['rel']=P.religion.where(P.religion.isin(['Hinduism','Islam','Christianity']),'other')
P['sg']=P.social_group.map({'scheduled tribe':'ST','scheduled caste':'SC','other backward class':'OBC','others':'General'})
P['qq']=P.q.map({1:'Q1 (poorest)',2:'Q2',3:'Q3',4:'Q4',5:'Q5 (richest)'})
P['care_hh']=np.where(P.special_care_needed_in_hh.astype(str).str.lower().str.startswith('y'),'care-needing member','none')
print(P.special_care_needed_in_hh.value_counts(dropna=False).to_dict())
SPL={'social group':'sg','religion':'rel','MPCE quintile':'qq','care need in HH':'care_hh'}
def run(day,lo,hi,cols,gender=None):
    for sn,col in SPL.items():
        rows={}
        for cn,cm in COH2.items():
            for v in sorted(P[col].dropna().unique()):
                m=cm&(P[col]==v)&day
                if gender: m&=P.gender==gender
                r=prof(m,lo,hi)
                if r: rows[(cn,v)]=r
        d=pd.DataFrame(rows).T; d['n']=d.n.astype(int); print('##',sn); print(d[cols])
c1=['n','paid work','domestic','care','leisure/media','%work@5pm','%work@7pm']
print('######## WORK DAY, 17:00-24:00, ALL'); run(P.dtype=='work',26,40,c1)
print('######## WORK DAY, 17:00-24:00, WOMEN'); run(P.dtype=='work',26,40,c1,'female')
print('######## WORK DAY, 17:00-24:00, MEN'); run(P.dtype=='work',26,40,c1,'male')
P.to_pickle(D+'/P3.pkl')
