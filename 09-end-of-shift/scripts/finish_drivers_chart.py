"""Dot plot of when salaried people stop working, outside education, by industry, employer and gender.
usage: python3 -I finish_drivers_chart.py <finish-drivers.csv> <out.png>
Dot = median finish, bar = middle half (25th to 75th percentile); dotted line = 5 pm. Reads the table written by finish_drivers.py."""
import sys, pandas as pd, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.font_manager as fm
CSV, OUT = sys.argv[1:3]
for f_ in ['Bold', 'Regular']: fm.fontManager.addfont(f"/home/jaidevd/.local/share/fonts/Lora-{f_}.ttf")
plt.rcParams['font.family'] = 'Lora'; BG = 'papayawhip'
d = pd.read_csv(CSV, dtype={'level': str}); d['level'] = d.level.astype(str)
d = d.rename(columns={'median finish': 'med', '% finishing after 5pm': 'after5'})
NIC = {'47': 'Retail', '56': 'Food service', '45': 'Motor vehicle trade and repair', '49': 'Land transport', '13': 'Textiles', '62': 'IT and programming', '64': 'Finance',
       '84': 'Public administration', '86': 'Health', '82': 'Office administration', '41': 'Building construction', '1': 'Agriculture', '97': 'Domestic work', '80': 'Security and investigation', '10': 'Food manufacturing', '14': 'Apparel manufacturing'}
ind = d[(d.factor == 'Industry (NIC)') & d.level.isin(NIC)].copy(); ind['label'] = ind.level.map(NIC); ind = ind.sort_values(['med', 'p75'], ascending=False)
emp = d[d.factor == 'Employer'].copy(); emp['label'] = emp.level.replace({'Other (co-op, trust, household)': 'Other (co-op, trust)', 'Proprietary / partnership': 'Proprietary or partnership'}); emp = emp.sort_values('med', ascending=False)
gen = d[d.factor == 'Gender'].copy(); gen['label'] = gen.level
allr = d[d.factor == 'Gender'].copy()
blocks = [('By industry', ind, 'maroon'), ('By employer', emp, 'teal'), ('By gender', gen, 'darkorange')]
rows = []; y = 0
for t, df, c in blocks:
    rows.append(('head', t, None, c)); [rows.append(('row', r.label, r, c)) for r in df.itertuples()]; rows.append(('gap', '', None, c))
rows = rows[:-1]; N = len(rows)
fig, ax = plt.subplots(figsize=(10.5, 0.33 * N + 2.2)); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.spines[['top', 'right', 'left']].set_visible(False); ax.grid(axis='x', color='gray', linewidth=0.3, linestyle='dashed'); ax.set_axisbelow(True)
tf = lambda h: f'{int((h - 1) % 12 + 1)}:{int(round((h % 1) * 60)):02d} {"am" if h < 12 else "pm"}'
yt = []; yl = []
for i, (kind, lab, r, c) in enumerate(rows):
    yy = N - i
    if kind == 'head': ax.text(12.9, yy, lab, fontweight='bold', fontsize=11, va='center', color=c)
    elif kind == 'row':
        ax.plot([r.p25, r.p75], [yy, yy], color=c, lw=5, alpha=0.35, solid_capstyle='butt'); ax.plot(r.med, yy, 'o', color=c, ms=8, zorder=5)
        ax.text(r.p75 + 0.15, yy, f'{tf(r.med)}  ({r.after5:.0f}% after 5 pm)', fontsize=8.3, va='center', color='0.25')
        yt.append(yy); yl.append(lab)
ax.set_yticks(yt); ax.set_yticklabels(yl, fontsize=9.5); ax.tick_params(axis='y', length=0)
ax.axvline(17, color='black', lw=1.2, ls=':', zorder=1); ax.text(17.05, N + 0.9, '5 pm', fontweight='bold', fontsize=10)
ax.set_xlim(12.8, 23.6); ax.set_ylim(0.3, N + 1.3)
ax.set_xticks(range(13, 23)); ax.set_xticklabels([f'{(h - 1) % 12 + 1} {"am" if h < 12 else "pm"}' for h in range(13, 23)], fontsize=9.5)
fig.suptitle('Outside Schools, the Day Ends at Very Different Hours by Industry', fontweight='bold', fontsize=14.5, y=0.995)
fig.text(0.5, 0.945, 'When salaried people stop paid work on a normal work day. Dot: median. Bar: middle half of people.', ha='center', fontsize=9, color='0.3')
fig.text(0.99, 0.004, 'Source: NSO Time Use Survey 2024, weighted. Industries from NIC codes, those with 400+ people shown. Education excluded.', ha='right', fontsize=7, color='0.4')
fig.subplots_adjust(left=0.22, right=0.985, top=0.915, bottom=0.07)
fig.savefig(OUT, dpi=300, facecolor=BG, bbox_inches='tight')
