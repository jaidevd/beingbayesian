"""Paid work, housework and care of salaried women and men (education excluded) on a work day and on an off day.
usage: python3 -I weekend_work.py <work dir with P3.pkl/G2.pkl> <out.csv>   (cluster bootstrap over FSUs within region x sector strata)"""
import sys, os, numpy as np, pandas as pd
D, OUT = sys.argv[1:3]; sys.argv = [sys.argv[0], D, 'none']
exec(open(os.path.dirname(os.path.abspath(__file__)) + '/tab.py').read().split("if __name__")[0])
P = pd.read_pickle(D + '/P3.pkl').reset_index(drop=True); P = P[P.nic2 != 85].reset_index(drop=True); n = len(P)
key = P[k].copy(); key['i'] = np.arange(n); G = G.merge(key, on=k)
def mins(grp): return G[G.g == grp].groupby('i').size().reindex(range(n), fill_value=0).to_numpy() * 30
M = {'paid work': mins('paid work'), 'housework': mins('domestic'), 'care': mins('care')}
M['unpaid'] = M['housework'] + M['care']; M['total work'] = M['paid work'] + M['unpaid']
M['any paid work'] = (M['paid work'] > 0) * 100.0; M['any housework'] = (M['housework'] > 0) * 100.0
psu = (P.nss_region.astype(str) + '_' + P.sector + '_' + P.fsu_serial_no.astype(str)).to_numpy(); strata = (P.nss_region.astype(str) + '_' + P.sector).to_numpy()
codes, fidx = np.unique(psu, return_inverse=True); fstr = pd.Series(strata).groupby(fidx).first().to_numpy()
sl = {s: np.flatnonzero(fstr == s) for s in np.unique(fstr)}; rng = np.random.default_rng(7); B = 300
C = np.zeros((B, len(codes)))
for b in range(B):
    for ids in sl.values(): C[b] += np.bincount(rng.choice(ids, len(ids)), minlength=len(codes))
W = P.w.to_numpy(); rows = []; BS = {}
for dt in ('work', 'off'):
    for sx, gname in [('women', 'female'), ('men', 'male')]:
        m = ((P.gender == gname) & (P.dtype == dt)).to_numpy(); den = np.bincount(fidx[m], weights=W[m], minlength=len(codes))
        for met, v in M.items():
            num = np.bincount(fidx[m], weights=(W * v)[m], minlength=len(codes)); bs = (C @ num) / (C @ den); BS[(dt, sx, met)] = (num.sum() / den.sum(), bs)
            rows.append((dt, sx, met, int(m.sum()), round(num.sum() / den.sum(), 1), round(np.percentile(bs, 2.5), 1), round(np.percentile(bs, 97.5), 1)))
for dt in ('work', 'off'):
    for met in ('unpaid', 'housework', 'total work'):
        (ew, bw), (em, bm) = BS[(dt, 'women', met)], BS[(dt, 'men', met)]
        rows.append((dt, 'women minus men', met, 0, round(ew - em, 1), round(np.percentile(bw - bm, 2.5), 1), round(np.percentile(bw - bm, 97.5), 1)))
res = pd.DataFrame(rows, columns=['day', 'sex', 'metric', 'n', 'estimate', 'lo95', 'hi95']); res.to_csv(OUT, index=False)
pd.set_option('display.width', 250); print(res.to_string(index=False))
