"""usage: python3 -I spouse_chart.py <spouse-housework.csv> <out.png>"""
import sys, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.font_manager as fm, pandas as pd
src, out = sys.argv[1:3]
r = pd.read_csv(src).set_index(['group', 'metric']).estimate
for f in ['Bold', 'Regular']: fm.fontManager.addfont(f"/home/jaidevd/.local/share/fonts/Lora-{f}.ttf")
plt.rcParams['font.family'] = 'Lora'; BG = 'papayawhip'
G = [('all salaried men with a wife (work day)', 'All salaried men with a wife'), ('knowledge work', 'Husband in knowledge work'),
     ('wife on domestic duties only', 'Wife on domestic duties only'), ('wife regular salaried', 'Wife in a regular salaried job')]
S = [('paid', 'paid work', 'teal'), ('dom', 'housework', 'maroon'), ('care', 'care', '#C62828'), ('leis', 'leisure and media', 'darkorange')]
fig, ax = plt.subplots(figsize=(10, 6.4)); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.spines[['top', 'right', 'left']].set_visible(False); ax.grid(axis='x', color='gray', linewidth=0.3, linestyle='dashed'); ax.set_axisbelow(True)
y = 0; ticks = []; labs = []
for gk, gl in G:
    ax.text(-0.02, y - 0.55, gl, transform=ax.get_yaxis_transform(), ha='right', va='center', fontweight='bold', fontsize=10.5)
    for who, pre in [('Husband', 'husband'), ('Wife', 'wife')]:
        left = 0
        for key, lab, col in S:
            v = r[(gk, f'{pre} {"paid work" if key=="paid" else "housework" if key=="dom" else "care" if key=="care" else "leisure"}, day')] / 60
            ax.barh(y, v, left=left, color=col, height=0.8, label=lab if (y == 0) else None)
            if v > 0.45: ax.text(left + v / 2, y, f'{v:.1f}', ha='center', va='center', fontsize=8.5, color='white', fontweight='bold')
            left += v
        unpaid = (r[(gk, f'{pre} housework, day')] + r[(gk, f'{pre} care, day')]) / 60
        ax.text(left + 0.12, y, f'unpaid at home: {unpaid:.1f} h', va='center', fontsize=8.5, color='0.3')
        ticks.append(y); labs.append(who); y += 1
    y += 0.9
ax.set_yticks(ticks); ax.set_yticklabels(labs, fontsize=9.5); ax.invert_yaxis(); ax.set_xlim(0, 14.2)
ax.set_xlabel('hours per day (sleep and other time not shown)', fontsize=9)
ax.tick_params(axis='y', length=0)
fig.suptitle("The Ideal Worker's Day, and His Wife's", fontweight='bold', fontsize=15, y=0.985)
fig.text(0.5, 0.925, 'Average day of a salaried man on a work day and of his wife, both answering for the same weekday.', ha='center', fontsize=9, color='0.3')
fig.legend(*ax.get_legend_handles_labels(), frameon=False, ncol=4, fontsize=9, loc='lower center', bbox_to_anchor=(0.5, 0.045))
fig.text(0.01, 0.005, 'Knowledge work is approximated from NIC industry codes and a graduate degree.', fontsize=7, color='0.4')
fig.text(0.99, 0.005, 'Source: NSO Time Use Survey 2024, weighted.', ha='right', fontsize=7, color='0.4')
fig.subplots_adjust(left=0.27, right=0.97, top=0.88, bottom=0.17)
fig.savefig(out, dpi=300, facecolor=BG, bbox_inches='tight')
