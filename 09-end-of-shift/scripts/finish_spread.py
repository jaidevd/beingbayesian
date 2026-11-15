"""How spread out the end of the working day is, with 5 pm as a reference line.
usage: python3 -I finish_spread.py <work dir with P3.pkl/G2.pkl/employer.parquet> <out.csv> <out.png>
End of the day = end of a person's last paid-work half hour (normal work days, people with paid work).
Left: share of all salaried people finishing in each half hour. Right: share who have finished by each time, for three
mutually exclusive groups, with 95% cluster-bootstrap bands (FSUs resampled within state x sector strata)."""
import sys, os, numpy as np, pandas as pd, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.font_manager as fm
D, OUTCSV, OUTPNG = sys.argv[1:4]; sys.argv = [sys.argv[0], D, 'none']
exec(open(os.path.dirname(os.path.abspath(__file__)) + '/tab.py').read().split("if __name__")[0])
P = pd.read_pickle(D + '/P3.pkl').reset_index(drop=True); n = len(P)
P = P.merge(pd.read_parquet(D + '/employer.parquet'), on=k, how='left')
key = P[k].copy(); key['i'] = np.arange(n); g = G.merge(key, on=k)
w_ = g[g.g == 'paid work']; slot = np.zeros((n, 48), bool); slot[w_.i.values, w_.slot.values] = True
has = slot.any(1); last = np.where(has, 47 - np.argmax(slot[:, ::-1], axis=1), -1)
ok = ((P.dtype == 'work') & has).to_numpy(); end_slot = last                     # end of slot s = 04:00 + (s+1) * 30 min
edu = (P.nic2 == 85).fillna(False).to_numpy(bool); pub = (P.emp == 'public').to_numpy(bool); prv = P.emp.isin(['private corporate', 'private small']).to_numpy(bool)
GROUPS = [('Education (schools, colleges)', edu, 'maroon'), ('Public employers, outside education', pub & ~edu, 'darkorange'), ('Private employers, outside education', prv & ~edu, 'teal')]
W = P.w.to_numpy()
psu = (P.nss_region.astype(str) + '_' + P.sector + '_' + P.fsu_serial_no.astype(str)).to_numpy(); strata = (P.nss_region.astype(str) + '_' + P.sector).to_numpy()
codes, fidx = np.unique(psu, return_inverse=True); fstr = pd.Series(strata).groupby(fidx).first().to_numpy()
sl = {s: np.flatnonzero(fstr == s) for s in np.unique(fstr)}; rng = np.random.default_rng(7); B = 300; BSC = np.zeros((B, len(codes)))
for b in range(B):
    for ids in sl.values(): BSC[b] += np.bincount(rng.choice(ids, len(ids)), minlength=len(codes))
SL = np.arange(0, 48)                       # slots whose end is the finish time
def clock(s): return 4 + (s + 1) * 0.5      # hour of day at which slot s ends
def cdf(mask):
    m = mask & ok; den = np.bincount(fidx[m], weights=W[m], minlength=len(codes)); out = []
    for s in range(12, 46):                  # finish at or before slot s ends
        num = np.bincount(fidx[m], weights=(W * (end_slot <= s))[m], minlength=len(codes)); bs = (BSC @ num) / (BSC @ den) * 100
        out.append((clock(s), num.sum() / den.sum() * 100, np.percentile(bs, 2.5), np.percentile(bs, 97.5)))
    return np.array(out), int(m.sum())
rows = []; curves = {}
for name, mask, col in GROUPS + [('All salaried', np.ones(n, bool), 'black')]:
    c, nn = cdf(mask); curves[name] = (c, nn, col)
    for t, e, lo, hi in c: rows.append((name, nn, t, round(e, 1), round(lo, 1), round(hi, 1)))
pd.DataFrame(rows, columns=['group', 'n', 'finished by (hour)', 'share finished (%)', 'lo95', 'hi95']).to_csv(OUTCSV, index=False)
# histogram for all salaried: share finishing in each half hour
m = ok; hist = np.array([(W * (end_slot == s))[m].sum() for s in range(48)]) / W[m].sum() * 100
for f in ['Bold', 'Regular']: fm.fontManager.addfont(f"/home/jaidevd/.local/share/fonts/Lora-{f}.ttf")
plt.rcParams['font.family'] = 'Lora'; BG = 'papayawhip'
fig, axs = plt.subplots(1, 2, figsize=(12.4, 5.2), gridspec_kw={'width_ratios': [1.15, 1]}); fig.patch.set_facecolor(BG)
for ax in axs:
    ax.set_facecolor(BG); ax.spines[['top', 'right']].set_visible(False); ax.grid(axis='y', color='gray', linewidth=0.3, linestyle='dashed'); ax.set_axisbelow(True)
    ax.set_xticks(range(12, 25, 2)); ax.set_xticklabels([f'{(h - 1) % 12 + 1} {"pm" if h < 24 else "am"}' for h in range(12, 25, 2)]); ax.set_xlim(11.5, 24.2)
ax = axs[0]; xs = np.array([clock(s) for s in range(48)]); before = xs <= 17.0
ax.bar(xs[before] - 0.25, hist[before], width=0.46, color='teal', alpha=0.8, label='finish at or before 5 pm')
ax.bar(xs[~before] - 0.25, hist[~before], width=0.46, color='darkorange', alpha=0.85, label='finish after 5 pm')
sh_before = hist[before].sum(); ax.axvline(17, color='black', lw=1.2, ls=':'); ax.text(17.1, hist.max() * 1.06, '5 pm', fontweight='bold', fontsize=10)
tf = lambda h: f'{int((h - 1) % 12 + 1)}:{int(round((h % 1) * 60)):02d} pm'
o = np.argsort(end_slot[m]); cs = np.cumsum(W[m][o]) / W[m].sum(); med = clock(end_slot[m][o][np.searchsorted(cs, .5)]); p25 = clock(end_slot[m][o][np.searchsorted(cs, .25)]); p75 = clock(end_slot[m][o][np.searchsorted(cs, .75)])
ax.set_xlim(11.0, 24.2); ax.set_ylim(0, hist.max() * 1.18)
ax.text(11.2, hist.max() * 1.02, f'{sh_before:.0f}% have finished\nby 5 pm', fontsize=10, fontweight='bold', color='teal', va='top')
ax.text(20.2, hist.max() * 0.80, f'{100 - sh_before:.0f}% finish after 5 pm,\nhalf of all people between\n{tf(p25)} and {tf(p75)}', fontsize=10, fontweight='bold', color='darkorange', va='top')
ax.set_ylabel('% of salaried people finishing in that half hour', fontsize=9); ax.set_title('When the working day ends: all salaried people', fontweight='bold', fontsize=11, loc='left')
ax = axs[1]
for name, (c, nn, col) in curves.items():
    if name == 'All salaried': continue
    ax.fill_between(c[:, 0], c[:, 2], c[:, 3], color=col, alpha=0.18, lw=0); ax.plot(c[:, 0], c[:, 1], color=col, lw=2.6, label=name)
ax.axvline(17, color='black', lw=1.2, ls=':'); ax.text(17.1, 95, '5 pm', fontweight='bold', fontsize=10)
for name, (c, nn, col) in curves.items():
    if name == 'All salaried': continue
    v = c[np.argmin(np.abs(c[:, 0] - 17)), 1]; ax.plot([17], [v], 'o', color=col, ms=7); ax.text(16.85, v, f'{v:.0f}%', ha='right', va='center', fontsize=9.5, fontweight='bold', color=col)
ax.set_ylim(0, 102); ax.set_ylabel('% who have finished for the day', fontsize=9); ax.set_title('How quickly people finish, by job and employer', fontweight='bold', fontsize=11, loc='left')
ax.legend(frameon=False, fontsize=9, loc='lower right')
fig.suptitle('Salaried India Stops Work Across a Spread of Hours, Not at 5 pm', fontweight='bold', fontsize=15, y=0.995)
fig.text(0.5, 0.925, 'End of the last paid-work half hour on a normal work day, salaried people who did paid work. Dotted line: 5 pm.', ha='center', fontsize=9, color='0.3')
fig.text(0.01, 0.005, 'Bands: 95% cluster bootstrap by FSU. Groups on the right do not overlap.', fontsize=7, color='0.4'); fig.text(0.99, 0.005, 'Source: NSO Time Use Survey 2024, weighted.', ha='right', fontsize=7, color='0.4')
fig.subplots_adjust(left=0.06, right=0.97, top=0.86, bottom=0.11, wspace=0.17)
fig.savefig(OUTPNG, dpi=300, facecolor=BG, bbox_inches='tight')
print('share finished by 5pm', round(sh_before, 1), 'median', med, 'p25', p25, 'p75', p75)
for name, (c, nn, col) in curves.items():
    v = c[np.argmin(np.abs(c[:, 0] - 17))]; print(name, nn, 'by 5pm', [round(x) for x in v[1:]], 'by 4pm', round(c[np.argmin(np.abs(c[:, 0] - 16)), 1]), 'by 7pm', round(c[np.argmin(np.abs(c[:, 0] - 19)), 1]))
