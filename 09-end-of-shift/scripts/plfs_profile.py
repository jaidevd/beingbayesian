"""PLFS 2025 (calendar-year person file): profile of the 'ideal worker' cohort.
usage: python3 -I plfs_profile.py <cperv12025.csv> <out.csv>
Cohort: age 18-34 and graduate or above (gedu_lvl 12, 13). Weights: mult/100 (used for shares and medians only)."""
import sys, numpy as np, pandas as pd
src, out = sys.argv[1], sys.argv[2]
cols = ['sec','sex','age','gedu_lvl','pas','etyp_pas','ocu_pas','ind_pas','job_pas','leave_pas','ssec_pas','wrkr_pas',
        'tothrs_wrk','ern_reg','hr1','hr2','hr3','hr4','hr5','hr6','hr7','mult']
d = pd.read_csv(src, usecols=cols, dtype=str)
for c in d.columns:
    if c not in ('ind_pas', 'ocu_pas'): d[c] = pd.to_numeric(d[c], errors='coerce')
d['w'] = d.mult / 100
d = d[(d.age >= 18) & d.sex.isin([1, 2])].copy()
d['sx'] = d.sex.map({1: 'men', 2: 'women'})
d['grad'] = d.gedu_lvl.isin([12, 13])
d['young'] = d.age <= 34
def status(p):
    if p == 31: return 'regular wage/salaried'
    if p in (11, 12, 21): return 'self-employed / unpaid family'
    if p in (41, 42, 51, 52): return 'casual labour'
    if p in (81, 82): return 'unemployed'
    if p == 91: return 'student'
    if p in (92, 93): return 'domestic duties'
    return 'other not working'
d['status'] = d.pas.map(status)
hrs = d[[f'hr{i}' for i in range(1, 8)]]
d['days'] = (hrs.fillna(0) > 0).sum(axis=1)
nic2 = d.ind_pas.fillna('').str.zfill(5).str[:2]
def ind(x):
    if not x.isdigit(): return 'unknown'
    x = int(x)
    if 10 <= x <= 33: return 'manufacturing'
    if 45 <= x <= 47: return 'trade'
    if 49 <= x <= 53: return 'transport & storage'
    if 58 <= x <= 63: return 'IT, media, telecom'
    if 64 <= x <= 66: return 'finance & insurance'
    if 68 <= x <= 82: return 'real estate, professional & admin services'
    if x == 84: return 'public administration'
    if x == 85: return 'education'
    if 86 <= x <= 88: return 'health & social work'
    return 'other'
d['industry'] = nic2.map(ind)
d['occ'] = d.ocu_pas.fillna('').str.zfill(3).str[0].map({'1': 'managers', '2': 'professionals', '3': 'technicians & associate prof.', '4': 'clerical',
    '5': 'service & sales', '6': 'skilled agriculture', '7': 'craft trades', '8': 'plant & machine operators', '9': 'elementary'})
def emp(e):
    if e in (5, 6, 7): return 'public (govt, PSU, autonomous)'
    if e == 8: return 'private company'
    if e in (1, 2, 3, 4): return 'proprietary / partnership'
    return 'other (co-op, trust, households)'
d['employer'] = d.etyp_pas.map(emp)
def wmed(x, w, q=0.5):
    m = x.notna(); x, w = x[m].to_numpy(), w[m].to_numpy(); o = np.argsort(x); x, w = x[o], w[o]
    return x[np.searchsorted(np.cumsum(w), q * w.sum())]
def wshare(mask, w): return float((w * mask).sum() / w.sum() * 100)
rows = []
def add(block, group, sx, item, val): rows.append((block, group, sx, item, round(val, 1)))
cohorts = {'age 18-34': d.young, 'age 18-34, graduate+': d.young & d.grad}
for cn, cm in cohorts.items():
    for sx in ['men', 'women']:
        x = d[cm & (d.sx == sx)]
        for s in ['regular wage/salaried', 'self-employed / unpaid family', 'casual labour', 'unemployed', 'student', 'domestic duties', 'other not working']:
            add('A usual status (% of cohort)', cn, sx, s, wshare(x.status == s, x.w))
        add('A usual status (% of cohort)', cn, sx, 'labour force participation', wshare(x.pas.between(11, 82), x.w))
r = d[d.young & d.grad & (d.pas == 31)]
allr = d[(d.pas == 31)]
for cn, x0 in [('regular wage, age 18-34 graduate+', r), ('regular wage, all 18+', allr)]:
    for sx in ['men', 'women', 'all']:
        x = x0 if sx == 'all' else x0[x0.sx == sx]
        if sx == 'all': add('B who they are', cn, sx, 'women (% of group)', wshare(x.sx == 'women', x.w))
        for k_, col in [('employer', 'employer'), ('occupation', 'occ'), ('industry', 'industry')]:
            for v in x[col].dropna().unique():
                add('B who they are', cn, sx, f'{k_}: {v}', wshare(x[col] == v, x.w))
        e = x[x.ern_reg > 0]
        add('C pay, security, hours', cn, sx, 'median monthly earnings (Rs)', wmed(e.ern_reg, e.w))
        add('C pay, security, hours', cn, sx, 'earnings p25 (Rs)', wmed(e.ern_reg, e.w, .25))
        add('C pay, security, hours', cn, sx, 'earnings p75 (Rs)', wmed(e.ern_reg, e.w, .75))
        add('C pay, security, hours', cn, sx, 'no written contract (%)', wshare(x.job_pas == 1, x.w))
        add('C pay, security, hours', cn, sx, 'not eligible for paid leave (%)', wshare(x.leave_pas == 2, x.w))
        add('C pay, security, hours', cn, sx, 'no social security benefit (%)', wshare(x.ssec_pas == 8, x.w))
        sec = (x.job_pas > 1) & (x.leave_pas == 1) & (x.ssec_pas.between(1, 7))
        add('C pay, security, hours', cn, sx, 'secure job: contract + paid leave + social security (%)', wshare(sec, x.w))
        add('C pay, security, hours', cn, sx, 'enterprise with 20+ workers (%)', wshare(x.wrkr_pas == 4, x.w))
        add('C pay, security, hours', cn, sx, 'median hours worked in last 7 days', wmed(x.tothrs_wrk, x.w))
        add('C pay, security, hours', cn, sx, 'worked 60+ hours (%)', wshare(x.tothrs_wrk >= 60, x.w))
        add('C pay, security, hours', cn, sx, 'worked 48+ hours (%)', wshare(x.tothrs_wrk >= 48, x.w))
        add('C pay, security, hours', cn, sx, 'worked all 7 days (%)', wshare(x.days == 7, x.w))
        add('C pay, security, hours', cn, sx, 'worked 6 or 7 days (%)', wshare(x.days >= 6, x.w))
res = pd.DataFrame(rows, columns=['block', 'group', 'sex', 'item', 'value'])
res.to_csv(out, index=False)
print('persons 18+', len(d), '| young graduates', int((d.young & d.grad).sum()), '| of whom regular wage', len(r))
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 500)
for b in res.block.unique():
    print('\n##', b); print(res[res.block == b].pivot_table(index=['group', 'item'], columns='sex', values='value', sort=False).to_string())
