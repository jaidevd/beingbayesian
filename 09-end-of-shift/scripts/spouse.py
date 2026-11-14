"""The 'ideal worker's' household: link salaried men to their wives in the TUS 2024 and compare housework.
usage: python3 -I spouse.py <TUS clean dir> <P3.pkl from the main pipeline> <out.csv>
Pairs: head ('self') with 'spouse of head', and 'married child' with 'spouse of married child' (only where a household has exactly one such pair)."""
import sys, numpy as np, pandas as pd
R, P3, out = sys.argv[1:4]
k = ['fsu_serial_no', 'sample_hh_no', 'person_serial_no']; hh = k[:2]
cols = ['relation_to_hoh','gender','age','marital_status','usual_principal_activity_status','person_response_code','day_of_week','type_of_day',
        'time_from','time_to','major_minor_activity','activity_code','mult']
p = pd.read_parquet(R + '/per-tus-2024.parquet', columns=cols).reset_index()
p = p[p.major_minor_activity == 'major']
mins = lambda s: s.str[:2].astype(int) * 60 + s.str[3:5].astype(int)
a = (mins(p.time_from) - 240) % 1440; b = (mins(p.time_to) - 240) % 1440; b = np.where(b <= a, b + 1440, b)
p['dur'] = b - a; p['eve'] = np.clip(np.minimum(b, 1200) - np.maximum(a, 780), 0, None)
c = p.activity_code
p['dom'] = np.where((c >= 300) & (c < 400), p.dur, 0); p['dom_e'] = np.where((c >= 300) & (c < 400), p.eve, 0)
p['care'] = np.where((c >= 400) & (c < 500), p.dur, 0); p['paid'] = np.where((c >= 110) & (c <= 150), p.dur, 0)
p['leis'] = np.where((c >= 800) & (c < 900), p.dur, 0); p['leis_e'] = np.where((c >= 800) & (c < 900), p.eve, 0)
p['paid_e'] = np.where((c >= 110) & (c <= 150), p.eve, 0)
g = p.groupby(k).agg(rel=('relation_to_hoh', 'first'), sex=('gender', 'first'), age=('age', 'first'), status=('usual_principal_activity_status', 'first'),
                     resp=('person_response_code', 'first'), dow=('day_of_week', 'first'), dtype=('type_of_day', 'first'),
                     dom=('dom', 'sum'), dom_e=('dom_e', 'sum'), care=('care', 'sum'), paid=('paid', 'sum'), paid_e=('paid_e', 'sum'),
                     leis=('leis', 'sum'), leis_e=('leis_e', 'sum')).reset_index()
g = g[g.resp == 'cooperative']
print('persons', len(g), '| households', g.groupby(hh).ngroups, '| relations', g.rel.value_counts().to_dict())
def pairs(r1, r2):
    x = g[g.rel == r1]; y = g[g.rel == r2]
    ok = (x.groupby(hh).size() == 1) & (y.groupby(hh).size().reindex(x.groupby(hh).size().index) == 1)
    x = x.merge(ok[ok].reset_index()[hh], on=hh); y = y.merge(ok[ok].reset_index()[hh], on=hh)
    return x.merge(y, on=hh, suffixes=('_a', '_b'))
pr = pd.concat([pairs('self', 'spouse of head'), pairs('married child', 'spouse of married child')])
pr = pr[pr.sex_a != pr.sex_b]
m = pr.sex_a == 'male'
H = pr.copy()
for c_ in ['person_serial_no', 'rel', 'sex', 'age', 'status', 'dow', 'dtype', 'dom', 'dom_e', 'care', 'paid', 'paid_e', 'leis', 'leis_e']:
    H['h_' + c_] = np.where(m, pr[c_ + '_a'], pr[c_ + '_b']); H['w_' + c_] = np.where(m, pr[c_ + '_b'], pr[c_ + '_a'])
H['k_person'] = H.h_person_serial_no
H = H.rename(columns={'person_serial_no_a': 'pa', 'person_serial_no_b': 'pb'})
P = pd.read_pickle(P3)[k + ['w', 'kw_core', 'blue', 'grad', 'nss_region', 'sector']].rename(columns={'person_serial_no': 'k_person'})
H = H.merge(P, on=hh + ['k_person'])          # keeps husbands in our salaried (18+) sample
print('salaried husbands with a co-resident wife:', len(H), 'of', len(P[P.w > 0]), 'salaried people;', 'same day of week:', round((H.h_dow == H.w_dow).mean() * 100), '%')
H['wife'] = np.select([H.w_status.str.contains('domestic duties', na=False), H.w_status.str.contains('regular salaried', na=False)],
                      ['domestic duties only', 'regular salaried'], 'other (working or not)')
H['wife_in_work'] = ~H.w_status.str.contains('domestic duties|educational|rentier|disab|not able|others', na=False)
wd = (H.h_dtype == 'normal day')
kw = H.kw_core.fillna(False).astype(bool); bl = H.blue.fillna(False).astype(bool)
GROUPS = [('all salaried men with a wife (work day)', wd), ('knowledge work', wd & kw), ('blue-collar', wd & bl),
          ('wife on domestic duties only', wd & (H.wife == 'domestic duties only')), ('wife regular salaried', wd & (H.wife == 'regular salaried'))]
H['wife_dom_only'] = (H.wife == 'domestic duties only') * 100.0; H['wife_salaried'] = (H.wife == 'regular salaried') * 100.0
METRICS = [('wife_dom_only', 'wife on domestic duties only (%)'), ('wife_salaried', 'wife regular salaried (%)'),
           ('h_paid', 'husband paid work, day'), ('w_paid', 'wife paid work, day'), ('h_dom', 'husband housework, day'), ('w_dom', 'wife housework, day'),
           ('h_care', 'husband care, day'), ('w_care', 'wife care, day'), ('h_leis', 'husband leisure, day'), ('w_leis', 'wife leisure, day'),
           ('h_dom_e', 'husband housework, 5pm-midnight'), ('w_dom_e', 'wife housework, 5pm-midnight'),
           ('h_paid_e', 'husband paid work, 5pm-midnight'), ('w_paid_e', 'wife paid work, 5pm-midnight'),
           ('h_leis_e', 'husband leisure, 5pm-midnight'), ('w_leis_e', 'wife leisure, 5pm-midnight')]
# cluster bootstrap: resample FSUs within nss_region x sector strata (an approximation of the survey design)
fs = (H[hh[0]].astype(str) + '_' + H.nss_region.astype(str) + '_' + H.sector.astype(str)); fi, fu = pd.factorize(fs); F = len(fu)
st = pd.Series(fu).str.split('_').str[1:].str.join('_').to_numpy(); members = [np.flatnonzero(st == g_) for g_ in np.unique(st)]
rng = np.random.default_rng(7); B = 300; C = np.zeros((B, F))
for b_ in range(B):
    for mem in members: C[b_] += np.bincount(rng.choice(mem, len(mem)), minlength=F)
rows = []
for gname, m_ in GROUPS:
    x = H[m_]; fx = fi[m_.to_numpy()]
    if len(x) < 40: continue
    den = np.bincount(fx, weights=x.w.to_numpy(), minlength=F); dd = C @ den
    for col, lab in METRICS:
        num = np.bincount(fx, weights=(x.w * x[col]).to_numpy(), minlength=F)
        est = num.sum() / den.sum(); bs = (C @ num) / dd
        rows.append((gname, len(x), lab, round(est, 1), round(np.percentile(bs, 2.5), 1), round(np.percentile(bs, 97.5), 1)))
res = pd.DataFrame(rows, columns=['group', 'n', 'metric', 'estimate', 'lo95', 'hi95'])
res.to_csv(out, index=False)
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 200)
print(res.pivot_table(index='metric', columns='group', values='estimate', sort=False).to_string())
