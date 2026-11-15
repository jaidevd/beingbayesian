"""Total work (paid + housework + care) of salaried women and men on a normal work day, whole day and 5 pm to midnight.
usage: python3 -I total_work.py <work dir with P3.pkl/G2.pkl> <out.csv>   (cluster bootstrap over FSUs within state x sector strata)"""
import sys, os, numpy as np, pandas as pd
D, OUT = sys.argv[1:3]; sys.argv = [sys.argv[0], D, 'none']
exec(open(os.path.dirname(os.path.abspath(__file__)) + '/tab.py').read().split("if __name__")[0])
P = pd.read_pickle(D + '/P3.pkl').reset_index(drop=True); n = len(P)
key = P[k].copy(); key['i'] = np.arange(n); G = G.merge(key, on=k)
def mins(lo, hi, grp):
    x = G[(G.g == grp) & (G.slot >= lo) & (G.slot < hi)].groupby('i').size().reindex(range(n), fill_value=0).to_numpy() * 30
    return x
M = {}
for per, (lo, hi) in {'day': (0, 48), 'evening': (26, 40)}.items():
    M[(per, 'paid work')] = mins(lo, hi, 'paid work'); M[(per, 'housework')] = mins(lo, hi, 'domestic'); M[(per, 'care')] = mins(lo, hi, 'care')
    M[(per, 'commute')] = mins(lo, hi, 'commute')
    M[(per, 'unpaid')] = M[(per, 'housework')] + M[(per, 'care')]; M[(per, 'total work')] = M[(per, 'paid work')] + M[(per, 'unpaid')]
psu = (P.nss_region.astype(str) + '_' + P.sector + '_' + P.fsu_serial_no.astype(str)).to_numpy(); strata = (P.nss_region.astype(str) + '_' + P.sector).to_numpy()
codes, fidx = np.unique(psu, return_inverse=True); fstr = pd.Series(strata).groupby(fidx).first().to_numpy()
sl = {s: np.flatnonzero(fstr == s) for s in np.unique(fstr)}; rng = np.random.default_rng(7); B = 300
C = np.zeros((B, len(codes)))
for b in range(B):
    for ids in sl.values(): C[b] += np.bincount(rng.choice(ids, len(ids)), minlength=len(codes))
W = P.w.to_numpy(); work = (P.dtype == 'work').to_numpy()
IND5 = ['Manufacturing and construction','Trade, transport and hospitality','Knowledge services','Education, health and administration','Other industries']
COH = {'all salaried': np.ones(n, bool), **{g: (P.ind5 == g).to_numpy(bool) for g in IND5}}
rows = []; BS = {}
for cn, cm in COH.items():
    for sx, gm in [('women', (P.gender == 'female').to_numpy()), ('men', (P.gender == 'male').to_numpy())]:
        m = cm & gm & work; den = np.bincount(fidx[m], weights=W[m], minlength=len(codes))
        for (per, met), v in M.items():
            num = np.bincount(fidx[m], weights=(W * v)[m], minlength=len(codes)); bs = (C @ num) / (C @ den)
            BS[(cn, sx, per, met)] = (num.sum() / den.sum(), bs)
            rows.append((cn, sx, per, met, int(m.sum()), round(num.sum() / den.sum(), 1), round(np.percentile(bs, 2.5), 1), round(np.percentile(bs, 97.5), 1)))
for cn in COH:   # women minus men, same bootstrap draws
    for per in ('day', 'evening'):
        for met in ('total work', 'paid work', 'unpaid'):
            (ew, bw), (em, bm) = BS[(cn, 'women', per, met)], BS[(cn, 'men', per, met)]
            rows.append((cn, 'women minus men', per, met, 0, round(ew - em, 1), round(np.percentile(bw - bm, 2.5), 1), round(np.percentile(bw - bm, 97.5), 1)))
res = pd.DataFrame(rows, columns=['group', 'sex', 'period', 'metric', 'n', 'estimate', 'lo95', 'hi95']); res.to_csv(OUT, index=False)
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 200)
print(res[(res.sex == 'women minus men')].to_string(index=False))
