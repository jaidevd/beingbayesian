"""usage: python3 -I weekend_chart.py <weekend-work.csv> <out.png>"""
import sys, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.font_manager as fm, pandas as pd
src, out = sys.argv[1:3]
r = pd.read_csv(src).set_index(['day', 'sex', 'metric'])
for f in ['Bold', 'Regular']: fm.fontManager.addfont(f"/home/jaidevd/.local/share/fonts/Lora-{f}.ttf")
plt.rcParams['font.family'] = 'Lora'; BG = 'papayawhip'
S = [('paid work', 'paid work', 'teal'), ('housework', 'housework', 'maroon'), ('care', 'care', '#C62828')]
ROWS = [(0, 'work', 'women'), (1, 'work', 'men'), (2.9, 'off', 'women'), (3.9, 'off', 'men')]
fig, ax = plt.subplots(figsize=(10, 4.6)); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.spines[['top', 'right', 'left']].set_visible(False); ax.grid(axis='x', color='gray', linewidth=0.3, linestyle='dashed'); ax.set_axisbelow(True)
for y, dt, sx in ROWS:
    left = 0
    for key, lab, col in S:
        v = r.loc[(dt, sx, key), 'estimate'] / 60
        ax.barh(y, v, left=left, color=col, height=0.7, label=lab if y == 0 else None)
        if v > 0.55: ax.text(left + v / 2, y, f'{v:.1f}', ha='center', va='center', color='white', fontweight='bold', fontsize=10)
        left += v
    ax.text(left + 0.1, y, f"{r.loc[(dt, sx, 'total work'), 'estimate'] / 60:.1f} h", va='center', fontsize=12, fontweight='bold')
ax.set_yticks([y for y, _, _ in ROWS]); ax.set_yticklabels([s.capitalize() for _, _, s in ROWS], fontsize=11, fontweight='bold'); ax.tick_params(axis='y', length=0)
for y, t in [(0.5, 'On a work day'), (3.4, 'On a day off')]: ax.text(-0.075, y, t, transform=ax.get_yaxis_transform(), rotation=90, ha='right', va='center', fontsize=12, fontweight='bold', color='0.25')
ho = {sx: r.loc[('off', sx, 'any housework'), 'estimate'] for sx in ('women', 'men')}
ux = {sx: r.loc[('off', sx, 'unpaid'), 'estimate'] / 60 for sx in ('women', 'men')}
ax.text(8.0, 3.4, f"{ho['women']:.0f}% of women do housework\non a day off, against {ho['men']:.0f}% of men", fontsize=10.5, color='maroon', fontweight='bold', va='center')
ax.set_xlim(0, 11.5); ax.set_ylim(4.5, -0.6); ax.set_xlabel('hours in the day', fontsize=10)
fig.suptitle('A Day Off Is Not Off for Women', fontweight='bold', fontsize=16, y=1.0)
fig.text(0.5, 0.925, 'Women still work twice as many hours as men, because the unpaid work does not take a weekend.', ha='center', fontsize=10, color='0.3')
fig.legend(*ax.get_legend_handles_labels(), frameon=False, ncol=3, fontsize=10, loc='lower center', bbox_to_anchor=(0.5, -0.03))
fig.text(0.99, -0.03, 'Salaried workers outside education, 18+. Commuting not counted.\nSource: NSO Time Use Survey 2024, weighted.', ha='right', fontsize=7, color='0.4')
fig.subplots_adjust(left=0.14, right=0.97, top=0.85, bottom=0.17)
fig.savefig(out, dpi=300, facecolor=BG, bbox_inches='tight')
