"""What drives when salaried people stop working, outside education (NIC 85 excluded).
usage: python3 -I finish_drivers.py <work dir with P3.pkl/G2.pkl/employer.parquet> <out.csv>
Outcome = clock hour at which a person's last paid-work half hour ends (normal work days, people with paid work).
For every factor: weighted median finish by level, and the share of the variation in finish time the factor explains alone
and adds on top of all the others (weighted linear models, R-squared). Also the same for 'start of day' as a factor."""
import sys, os, numpy as np, pandas as pd, statsmodels.formula.api as smf
D, OUT = sys.argv[1:3]; sys.argv = [sys.argv[0], D, 'none']
exec(open(os.path.dirname(os.path.abspath(__file__)) + '/tab.py').read().split("if __name__")[0])
P = pd.read_pickle(D + '/P3.pkl').reset_index(drop=True); n = len(P)
P = P.merge(pd.read_parquet(D + '/employer.parquet'), on=k, how='left')
key = P[k].copy(); key['i'] = np.arange(n); g = G.merge(key, on=k)
w_ = g[g.g == 'paid work']; slot = np.zeros((n, 48), bool); slot[w_.i.values, w_.slot.values] = True
has = slot.any(1); first = np.where(has, np.argmax(slot, axis=1), -1); last = np.where(has, 47 - np.argmax(slot[:, ::-1], axis=1), -1)
P['finish'] = 4 + (last + 1) * 0.5; P['start'] = 4 + first * 0.5
P['hours'] = slot.sum(1) / 2
P['employer'] = P.emp.map({'public': 'Public', 'private corporate': 'Private company', 'private small': 'Proprietary / partnership', 'other': 'Other (co-op, trust, household)'})
P['gend'] = P.gender.map({'female': 'Women', 'male': 'Men'}); P['place'] = P.sector
P['age_'] = P.ageb.map({'<25': 'Under 25', '25-34': '25 to 34', '35-49': '35 to 49', '50+': '50 and over'})
P['caste'] = P.sg; P['edu'] = np.where(P.grad, 'Graduate', 'Not a graduate')
P['spend'] = P.q.map({1: 'Poorest fifth', 2: 'Second', 3: 'Middle', 4: 'Fourth', 5: 'Richest fifth'})
P['mar'] = np.where(P.married == 'married', 'Married', 'Not married')
P['dow'] = np.where(P.day_of_week.isin(['Saturday', 'Sunday']), P.day_of_week, 'Monday to Friday')
P['ind5'] = ind5(P) if 'ind5' in globals() else None
M = P[(P.dtype == 'work') & has & (P.nic2 != 85) & P.employer.notna()].copy()
M['nic_f'] = M.nic2.astype('Int64').astype(str); M['st'] = M.state.astype(str); M['startb'] = pd.cut(M.start, [0, 7, 8, 9, 10, 11, 25]).astype(str)
def wq(x, w, q=.5):
    o = np.argsort(x); x, w = x[o], w[o]; return x[min(np.searchsorted(np.cumsum(w), q * w.sum()), len(x) - 1)]
T = {'Industry (2-digit NIC)': 'C(nic_f)', 'Employer': 'C(employer)', 'Gender': 'C(gend)', 'State': 'C(st)', 'Place': 'C(place)', 'Age': 'C(age_)',
     'Social group': 'C(caste)', 'Education': 'C(edu)', 'Household spending': 'C(spend)', 'Marital status': 'C(mar)', 'Day of the week': 'C(dow)'}
r2 = lambda f, d=M: smf.wls('finish ~ ' + f, data=d, weights=d.w).fit().rsquared
full = r2(' + '.join(T.values())); alone = {a: r2(t) for a, t in T.items()}
uniq = {a: full - r2(' + '.join(v for b, v in T.items() if b != a)) for a in T}
fs = lambda h: f'{int((h - 1) % 12 + 1)}:{int(round((h % 1) * 60)):02d} {"am" if h < 12 else "pm"}'
print('n', len(M), 'median finish', fs(wq(M.finish.values, M.w.values)), 'full-model R2', round(full * 100, 1))
rows = []
for a, t in T.items(): rows.append((a, '', len(M), None, round(alone[a] * 100, 1), round(uniq[a] * 100, 1)))
print('\nfactor, explains alone %, adds to all others %'); [print(f'{r[0]:26s} {r[4]:5.1f} {r[5]:5.1f}') for r in sorted(rows, key=lambda r: -r[4])]
cols = [('Employer', 'employer'), ('Gender', 'gend'), ('Place', 'place'), ('Age', 'age_'), ('Social group', 'caste'), ('Education', 'edu'), ('Household spending', 'spend'), ('Marital status', 'mar'), ('Day of the week', 'dow')]
out = []
for lab, c in cols:
    for lv, d in M.groupby(c):
        out.append((lab, lv, len(d), wq(d.finish.values, d.w.values), wq(d.finish.values, d.w.values, .25), wq(d.finish.values, d.w.values, .75), np.average(d.finish > 17, weights=d.w) * 100))
ind = M.groupby('nic_f')
for nic, d in ind:
    if len(d) >= 400: out.append(('Industry (NIC)', nic, len(d), wq(d.finish.values, d.w.values), wq(d.finish.values, d.w.values, .25), wq(d.finish.values, d.w.values, .75), np.average(d.finish > 17, weights=d.w) * 100))
res = pd.DataFrame(out, columns=['factor', 'level', 'n', 'median finish', 'p25', 'p75', '% finishing after 5pm'])
res['median'] = res['median finish'].map(fs); res['middle half'] = res.p25.map(fs) + ' to ' + res.p75.map(fs)
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 200)
print(res[['factor', 'level', 'n', 'median', 'middle half', '% finishing after 5pm']].round(1).to_string(index=False))
# start-of-day and hours
print('\nstart alone R2', round(r2('C(startb)') * 100, 1), ' hours worked alone R2', round(smf.wls('finish ~ hours', data=M, weights=M.w).fit().rsquared * 100, 1))
print('corr(start, finish)', round(np.corrcoef(M.start, M.finish)[0, 1], 2), 'corr(hours, finish)', round(np.corrcoef(M.hours, M.finish)[0, 1], 2))
res.round(2).to_csv(OUT, index=False)
# adjusted gaps (minutes) from the all-factor model
mod = smf.wls('finish ~ ' + ' + '.join(T.values()), data=M, weights=M.w).fit()
print('\nadjusted gaps in finish time (minutes, all factors held equal):')
for nm, pat in [('Women vs men', 'gend'), ('Employer', 'employer'), ('Urban vs rural', 'place'), ('Age', 'age_'), ('Social group', 'caste')]:
    for kx, v in mod.params.items():
        if f'({pat})' in kx: print(f'  {kx:50s} {v * 60:6.0f}')
print('raw women-men gap (min):', round((wq(M[M.gend == "Women"].finish.values, M[M.gend == "Women"].w.values) - wq(M[M.gend == "Men"].finish.values, M[M.gend == "Men"].w.values)) * 60), '; mean gap', round((np.average(M[M.gend == "Women"].finish, weights=M[M.gend == "Women"].w) - np.average(M[M.gend == "Men"].finish, weights=M[M.gend == "Men"].w)) * 60))
