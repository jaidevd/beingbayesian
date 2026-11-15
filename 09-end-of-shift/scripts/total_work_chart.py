"""usage: python3 -I total_work_chart.py <total-work.csv> <out.png>"""
import sys, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.font_manager as fm, pandas as pd
src, out = sys.argv[1:3]
r = pd.read_csv(src); r = r[r.group == 'all salaried'].set_index(['sex', 'period', 'metric'])
for f in ['Bold', 'Regular']: fm.fontManager.addfont(f"/home/jaidevd/.local/share/fonts/Lora-{f}.ttf")
plt.rcParams['font.family'] = 'Lora'; BG = 'papayawhip'
S = [('paid work', 'paid work', 'teal'), ('housework', 'housework', 'maroon'), ('care', 'care', '#C62828')]
fig, axs = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={'width_ratios': [1.15, 1]}); fig.patch.set_facecolor(BG)
for ax, per, ttl, xmax in [(axs[0], 'day', 'Whole day', 11.8), (axs[1], 'evening', 'After 5 pm', 3.2)]:
    ax.set_facecolor(BG); ax.spines[['top', 'right', 'left']].set_visible(False); ax.grid(axis='x', color='gray', linewidth=0.3, linestyle='dashed'); ax.set_axisbelow(True)
    for y, sx in enumerate(['women', 'men']):
        left = 0
        for key, lab, col in S:
            v = r.loc[(sx, per, key), 'estimate'] / 60
            ax.barh(y, v, left=left, color=col, height=0.6, label=lab if (per == 'day' and y == 0) else None)
            if v > (0.55 if per == 'day' else 0.17): ax.text(left + v / 2, y, f'{v:.1f}', ha='center', va='center', color='white', fontweight='bold', fontsize=9)
            left += v
        tot = r.loc[(sx, per, 'total work'), 'estimate'] / 60
        ax.text(left + 0.1, y, f'{tot:.1f} h', va='center', fontsize=11, fontweight='bold')
    d = r.loc[('women minus men', per, 'total work')]
    ax.text(0.0, 1.0, f'Women work {d.estimate:.0f} minutes more [{d.lo95:.0f}-{d.hi95:.0f}]', transform=ax.get_yaxis_transform(), fontsize=10, color='maroon', fontweight='bold', va='center', ha='left') if False else None
    ax.set_title(f'{ttl}: women work {d.estimate:.0f} minutes more', fontweight='bold', fontsize=11, loc='left', pad=8)
    ax.set_yticks([0, 1]); ax.set_yticklabels(['Women', 'Men'], fontsize=11, fontweight='bold'); ax.tick_params(axis='y', length=0)
    ax.set_xlim(0, xmax); ax.set_ylim(1.6, -0.6); ax.set_xlabel('hours', fontsize=9)
fig.suptitle('Salaried Women Work Longer Days, and the Extra Is Unpaid', fontweight='bold', fontsize=15, y=0.99)
fig.text(0.5, 0.89, 'Paid work, housework and care on a normal work day for all salaried women and men; commuting is not counted.', ha='center', fontsize=9, color='0.3')
fig.legend(*axs[0].get_legend_handles_labels(), frameon=False, ncol=3, fontsize=9, loc='lower center', bbox_to_anchor=(0.5, 0.0))
fig.text(0.99, 0.005, 'Source: NSO Time Use Survey 2024, weighted.', ha='right', fontsize=7, color='0.4')
fig.subplots_adjust(left=0.08, right=0.97, top=0.78, bottom=0.2, wspace=0.18)
fig.savefig(out, dpi=300, facecolor=BG, bbox_inches='tight')
