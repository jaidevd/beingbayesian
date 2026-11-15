"""usage: python3 -I spouse_chart.py <spouse-housework.csv> <out.png>"""
import sys, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.font_manager as fm, pandas as pd
src, out = sys.argv[1:3]
r = pd.read_csv(src).set_index(['group', 'metric']).estimate
for f in ['Bold', 'Regular']: fm.fontManager.addfont(f"/home/jaidevd/.local/share/fonts/Lora-{f}.ttf")
plt.rcParams['font.family'] = 'Lora'; BG = 'papayawhip'
A = 'all salaried men with a wife (work day)'
G = [('wife on domestic duties only', f"Wife not in paid work ({r[(A, 'wife on domestic duties only (%)')]:.0f}% of couples)"),
     ('wife regular salaried', f"Wife in a regular salaried job ({r[(A, 'wife regular salaried (%)')]:.0f}%)")]
S = [('paid', 'paid work', 'teal', 'paid work'), ('dom', 'housework', 'maroon', 'housework'), ('care', 'care', '#C62828', 'care')]
fig, ax = plt.subplots(figsize=(10, 4.4)); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.spines[['top', 'right', 'left']].set_visible(False); ax.grid(axis='x', color='gray', linewidth=0.3, linestyle='dashed'); ax.set_axisbelow(True)
y = 0; ticks = []; labs = []
for gk, gl in G:
    ax.text(-0.015, y - 0.62, gl, transform=ax.get_yaxis_transform(), ha='right', va='center', fontweight='bold', fontsize=10.5)
    for who, pre in [('Husband', 'husband'), ('Wife', 'wife')]:
        left = 0
        for key, lab, col, mk in S:
            v = r[(gk, f'{pre} {mk}, day')] / 60
            ax.barh(y, v, left=left, color=col, height=0.8, label=lab if y == 0 else None)
            if v > 0.5: ax.text(left + v / 2, y, f'{v:.1f}', ha='center', va='center', fontsize=9, color='white', fontweight='bold')
            left += v
        sfx = ''
        if who == 'Wife' and gk == 'wife on domestic duties only': sfx = ', almost all unpaid'
        if who == 'Wife' and gk == 'wife regular salaried': sfx = f", {left - hus_total:.1f} h more than he does"
        if who == 'Husband': hus_total = left
        ax.text(left + 0.12, y, f'{left:.1f} h of work{sfx}', va='center', fontsize=10, fontweight='bold')
        ticks.append(y); labs.append(who); y += 1
    y += 0.9
ax.set_yticks(ticks); ax.set_yticklabels(labs, fontsize=10); ax.tick_params(axis='y', length=0)
ax.invert_yaxis(); ax.set_xlim(0, 15.5); ax.set_xlabel('hours of work in a normal work day', fontsize=9)
fig.suptitle('Two Full Working Days, Only One Paid', fontweight='bold', fontsize=15, y=0.985)
fig.text(0.5, 0.905, 'Paid work, housework and care of a salaried husband and his wife, for nine in ten couples; commuting is not counted.', ha='center', fontsize=9, color='0.3')
fig.legend(*ax.get_legend_handles_labels(), frameon=False, ncol=3, fontsize=9, loc='lower center', bbox_to_anchor=(0.5, 0.025))
fig.text(0.99, 0.005, 'Source: NSO Time Use Survey 2024, weighted.', ha='right', fontsize=7, color='0.4')
fig.subplots_adjust(left=0.30, right=0.97, top=0.83, bottom=0.2)
fig.savefig(out, dpi=300, facecolor=BG, bbox_inches='tight')
