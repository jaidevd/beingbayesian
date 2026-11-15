"""What makes a difference to who is still working at 5 pm (normal work day, salaried, TUS 2024).
usage: python3 -I what_matters.py <work dir with P3.pkl/G2.pkl/employer.parquet> <out.csv>
'Still working at 5 pm' = 5 pm falls between a person's first and last paid-work half hour (breaks up to 4 hours included).
Each level: weighted share and 95% interval from a cluster bootstrap over FSUs within state x sector strata.
Also reports, for each factor, the share of the variation in 'still working at 5 pm' that the factor explains on its own
and what it adds on top of all the others (weighted linear probability models)."""
import sys, os, numpy as np, pandas as pd, statsmodels.formula.api as smf
D, OUT = sys.argv[1:3]; sys.argv = [sys.argv[0], D, 'none']
exec(open(os.path.dirname(os.path.abspath(__file__)) + '/tab.py').read().split("if __name__")[0])
P = pd.read_pickle(D + '/P3.pkl').reset_index(drop=True); n = len(P)
P = P.merge(pd.read_parquet(D + '/employer.parquet'), on=k, how='left')
key = P[k].copy(); key['i'] = np.arange(n); g = G.merge(key, on=k)
w_ = g[g.g == 'paid work']; slot = np.zeros((n, 48), bool); slot[w_.i.values, w_.slot.values] = True
P['at5'] = on_the_clock(slot)[:, 26].astype(float)
P['employer'] = P.emp.map({'public': 'Public (government, autonomous)', 'private corporate': 'Private company', 'private small': 'Proprietary / partnership', 'other': 'Other (co-op, trust, household)'})
P['gend'] = P.gender.map({'female': 'Women', 'male': 'Men'})
P['place'] = P.sector
P['age_'] = P.ageb.map({'<25': 'Under 25', '25-34': '25 to 34', '35-49': '35 to 49', '50+': '50 and over'})
P['caste'] = P.sg.map({'General': 'General', 'OBC': 'OBC', 'SC': 'SC', 'ST': 'ST'})
P['edu'] = np.where(P.grad, 'Graduate', 'Not a graduate')
P['spend'] = P.q.map({1: 'Poorest fifth', 2: 'Second', 3: 'Middle', 4: 'Fourth', 5: 'Richest fifth'})
P['mar'] = np.where(P.married == 'married', 'Married', 'Not married')
P['dow'] = np.where(P.day_of_week.isin(['Saturday', 'Sunday']), P.day_of_week, 'Monday to Friday')
nic = P.nic2.astype('Int64')
def indus(x):
    if pd.isna(x): return None
    x = int(x)
    return {85: 'Education', 86: 'Health', 84: 'Public administration', 64: 'Finance', 62: 'IT and programming', 47: 'Retail'}.get(x, 'Manufacturing' if 10 <= x <= 33 else None)
P['industry'] = nic.map(indus)
P['ind2'] = np.where(nic == 85, 'Education (schools and colleges)', 'All other industries')
P['emp2'] = P.emp.map({'public': 'Public (government, autonomous)', 'private corporate': 'Private (company or firm)', 'private small': 'Private (company or firm)'})
work = (P.dtype == 'work').to_numpy()
FACT = [('ind2', 'Industry (simple)', ['Education (schools and colleges)', 'All other industries']), ('emp2', 'Employer (simple)', ['Public (government, autonomous)', 'Private (company or firm)']),
        ('industry', 'Industry', ['Education', 'Health', 'Public administration', 'Finance', 'Manufacturing', 'IT and programming', 'Retail']),
        ('employer', 'Employer', ['Public (government, autonomous)', 'Other (co-op, trust, household)', 'Private company', 'Proprietary / partnership']),
        ('gend', 'Gender', ['Women', 'Men']), ('place', 'Place', ['Rural', 'Urban']),
        ('age_', 'Age', ['50 and over', '35 to 49', '25 to 34', 'Under 25']), ('caste', 'Social group', ['ST', 'SC', 'OBC', 'General']),
        ('edu', 'Education', ['Graduate', 'Not a graduate']), ('spend', 'Household spending', ['Poorest fifth', 'Second', 'Middle', 'Fourth', 'Richest fifth']),
        ('mar', 'Marital status', ['Married', 'Not married']), ('dow', 'Day of the week', ['Monday to Friday', 'Saturday', 'Sunday'])]
# bootstrap
psu = (P.nss_region.astype(str) + '_' + P.sector + '_' + P.fsu_serial_no.astype(str)).to_numpy(); strata = (P.nss_region.astype(str) + '_' + P.sector).to_numpy()
codes, fidx = np.unique(psu, return_inverse=True); fstr = pd.Series(strata).groupby(fidx).first().to_numpy()
sl = {s: np.flatnonzero(fstr == s) for s in np.unique(fstr)}; rng = np.random.default_rng(7); B = 300; BSC = np.zeros((B, len(codes)))
for b in range(B):
    for ids in sl.values(): BSC[b] += np.bincount(rng.choice(ids, len(ids)), minlength=len(codes))
W = P.w.to_numpy(); y = P.at5.to_numpy()
def level(mask):
    m = mask & work; den = np.bincount(fidx[m], weights=W[m], minlength=len(codes)); num = np.bincount(fidx[m], weights=(W * y)[m], minlength=len(codes))
    bs = (BSC @ num) / (BSC @ den) * 100; return int(m.sum()), num.sum() / den.sum() * 100, np.percentile(bs, 2.5), np.percentile(bs, 97.5)
# variance explained
M = P[work & P.employer.notna()].copy(); M['nic_f'] = M.nic2.astype('Int64').astype(str); M['st'] = M.state.astype(str)
M['ind2'] = np.where(M.nic2 == 85, 'edu', 'other'); M['emp2'] = M.employer.map({'Public (government, autonomous)': 'public', 'Private company': 'private', 'Proprietary / partnership': 'private'})
T = {'industry': 'C(nic_f)', 'employer': 'C(employer)', 'gend': 'C(gend)', 'place': 'C(place)', 'age_': 'C(age_)', 'caste': 'C(caste)', 'edu': 'C(edu)', 'spend': 'C(spend)', 'mar': 'C(mar)', 'dow': 'C(dow)', 'state': 'C(st)'}
T2 = {'ind2': 'C(ind2)', 'emp2': 'C(emp2)'}
r2 = lambda f: smf.wls('at5 ~ ' + f, data=M, weights=M.w).fit().rsquared
full = r2(' + '.join(T.values())); alone = {a: r2(t) for a, t in T.items()}
unique = {a: full - r2(' + '.join(v for b_, v in T.items() if b_ != a)) for a in T}
MM = M[M.emp2.notna()]
alone.update({a: smf.wls('at5 ~ ' + t, data=MM, weights=MM.w).fit().rsquared for a, t in T2.items()}); unique.update({a: np.nan for a in T2})
rows = []
for col, lab, levels in FACT:
    for lv in levels:
        n_, e, lo, hi = level((P[col] == lv).to_numpy())
        rows.append((lab, lv, n_, round(e, 1), round(lo, 1), round(hi, 1), round(alone[col] * 100, 1), round(unique[col] * 100, 1)))
n_, e, lo, hi = level(np.ones(n, bool)); rows.append(('All salaried', 'All salaried', n_, round(e, 1), round(lo, 1), round(hi, 1), None, None))
st = P.groupby('state').apply(lambda d: pd.Series({'n': int(((d.dtype == 'work')).sum()), 'v': np.average(d[d.dtype == 'work'].at5, weights=d[d.dtype == 'work'].w) * 100})); st = st[st.n >= 300]
rows.append(('State', 'lowest of %d states with 300+ people' % len(st), int(st.n.loc[st.v.idxmin()]), round(st.v.min(), 1), None, None, round(alone['state'] * 100, 1), round(unique['state'] * 100, 1)))
rows.append(('State', 'highest', int(st.n.loc[st.v.idxmax()]), round(st.v.max(), 1), None, None, round(alone['state'] * 100, 1), round(unique['state'] * 100, 1)))
res = pd.DataFrame(rows, columns=['factor', 'level', 'n', 'share still working at 5pm', 'lo95', 'hi95', 'explains alone (%)', 'adds to all others (%)']); res.to_csv(OUT, index=False)
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 100); print(res.to_string(index=False)); print('all factors together explain', round(full * 100, 1), '% of the variation')
