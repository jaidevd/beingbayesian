"""PLFS 2025: days worked in the reference week and weekly hours of salaried workers (education excluded),
and the usual activity of women and men aged 18-59.
usage: python3 -I plfs_days.py <CPERV1.csv> <out.csv>
Cohort A: current weekly status 'regular salaried' (acws 31), age 18+, current industry not education (NIC 85).
Days worked = days among the last seven with any hours worked (hr1..hr7); the file does not say which weekday.
Weights: mult/100 (shares and means only). Cluster bootstrap over first-stage units (state x sector x mfsu) within
state x sector strata, 300 draws, seed 7."""
import sys, numpy as np, pandas as pd
src, out = sys.argv[1:3]
H = ['hr%d' % i for i in range(1, 8)]
d = pd.read_csv(src, dtype=str, usecols=['sex', 'age', 'pas', 'acws', 'aind_cws', 'mult', 'tothrs_wrk', 'st', 'sec', 'mfsu'] + H)
d['w'] = d.mult.astype(float) / 100; d['age'] = d.age.astype(int)
for c in ['tothrs_wrk'] + H: d[c] = pd.to_numeric(d[c], errors='coerce')
d['sex'] = d.sex.map({'1': 'men', '2': 'women'})
d = d[d.sex.notna()].reset_index(drop=True)
psu = (d.st + '_' + d.sec + '_' + d.mfsu).to_numpy(); strata = (d.st + '_' + d.sec).to_numpy()
codes, fidx = np.unique(psu, return_inverse=True); fstr = pd.Series(strata).groupby(fidx).first().to_numpy()
sl = {s: np.flatnonzero(fstr == s) for s in np.unique(fstr)}; rng = np.random.default_rng(7); B = 300
C = np.zeros((B, len(codes)))
for b in range(B):
    for ids in sl.values(): C[b] += np.bincount(rng.choice(ids, len(ids)), minlength=len(codes))
W = d.w.to_numpy()
def est(mask, v):
    den = np.bincount(fidx[mask], weights=W[mask], minlength=len(codes)); num = np.bincount(fidx[mask], weights=(W * v)[mask], minlength=len(codes))
    bs = (C @ num) / (C @ den); return num.sum() / den.sum(), np.percentile(bs, 2.5), np.percentile(bs, 97.5)
days = (d[H].fillna(0) > 0).sum(axis=1).to_numpy()
coh = ((d.acws == '31') & (d.age >= 18) & (d.aind_cws.str[:2] != '85')).to_numpy()
rows = []
for sx in ('women', 'men', 'all'):
    m = coh & ((d.sex == sx).to_numpy() if sx != 'all' else True)
    n = int(m.sum())
    for lab, v in [('worked 7 days, %', (days == 7) * 100.0), ('worked 6 or more days, %', (days >= 6) * 100.0), ('worked 5 or fewer days, %', (days <= 5) * 100.0),
                   ('weekly hours, mean', d.tothrs_wrk.fillna(0).to_numpy()), ('worked more than 48 hours, %', (d.tothrs_wrk.fillna(0).to_numpy() > 48) * 100.0)]:
        e, lo, hi = est(m, v); rows.append(('A salaried workers, excl. education', sx, lab, n, round(e, 1), round(lo, 1), round(hi, 1)))
age = d.age.between(18, 59).to_numpy()
for sx in ('women', 'men'):
    m = age & (d.sex == sx).to_numpy(); n = int(m.sum())
    for lab, codes_ in [('regular salaried (usual status 31), %', ['31']), ('domestic duties (92, 93), %', ['92', '93']),
                        ('self-employed (11, 12), %', ['11', '12']), ('unpaid family helper (21), %', ['21'])]:
        e, lo, hi = est(m, d.pas.isin(codes_).to_numpy() * 100.0); rows.append(('B usual activity, age 18-59', sx, lab, n, round(e, 1), round(lo, 1), round(hi, 1)))
res = pd.DataFrame(rows, columns=['block', 'sex', 'item', 'n', 'estimate', 'lo95', 'hi95']); res.to_csv(out, index=False)
pd.set_option('display.width', 220); print(res.to_string(index=False))
