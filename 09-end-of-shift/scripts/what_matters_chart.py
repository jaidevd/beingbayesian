"""usage: python3 -I what_matters_chart.py <what-matters.csv> <out.png>"""
import sys, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.font_manager as fm, pandas as pd
src, out = sys.argv[1:3]
r = pd.read_csv(src); V = 'share still working at 5pm'
for f in ['Bold', 'Regular']: fm.fontManager.addfont(f"/home/jaidevd/.local/share/fonts/Lora-{f}.ttf")
plt.rcParams['font.family'] = 'Lora'; BG = 'papayawhip'
avg = float(r[r.factor == 'All salaried'][V].iloc[0])
fig, ax = plt.subplots(figsize=(8.6, 4.4)); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.spines[['top', 'right', 'left']].set_visible(False); ax.grid(axis='x', color='gray', linewidth=0.3, linestyle='dashed'); ax.set_axisbelow(True)
y = 0; ticks = []; labs = []
def header(txt, note=''):
    global y
    ax.text(-0.02, y, txt.upper(), transform=ax.get_yaxis_transform(), ha='right', va='center', fontsize=8.5, color='0.35', fontweight='bold')
    if note: ax.text(100.5, y, note, ha='right', va='center', fontsize=8, color='0.4', style='italic')
    y += 0.9
for fct, head, lab, col in [('Industry (simple)', 'Job', {'Education (schools and colleges)': 'Education (schools, colleges)', 'All other industries': 'All other industries'}, 'maroon'),
                            ('Employer (simple)', 'Employer', {'Public (government, autonomous)': 'Public', 'Private (company or firm)': 'Private'}, 'teal'),
                            ('Gender', 'Gender', {'Women': 'Women', 'Men': 'Men'}, 'teal')]:
    d = r[r.factor == fct]; header(head, f"explains {d['explains alone (%)'].iloc[0]:.0f}% of the variation")
    for i, (_, row) in enumerate(d.iterrows()):
        e, lo, hi = row[V], row.lo95, row.hi95
        ax.plot([lo, hi], [y, y], color=col, lw=2.4, alpha=0.7); ax.plot(e, y, 'o', color=col, ms=8)
        ax.text(min(hi + 1.5, 96), y, f'{e:.0f}%', va='center', fontsize=9, color='0.25'); ticks.append(y); labs.append(lab[row.level]); y += 1
    y += 0.5
ax.axvline(avg, color='black', lw=1.1, ls=':', zorder=1); ax.text(avg, -1.15, f'all salaried: {avg:.0f}%', ha='center', fontsize=9, fontweight='bold')
ax.set_yticks(ticks); ax.set_yticklabels(labs, fontsize=10); ax.tick_params(axis='y', length=0); ax.invert_yaxis(); ax.set_ylim(y - 0.9, -1.7)
ax.set_xlim(0, 101); ax.set_xlabel('% still working at 5 pm (dot = average, line = 95% interval)', fontsize=9, labelpad=8)
fig.suptitle('Outside Education, Three in Four Salaried People Are Still Working at 5 pm', fontweight='bold', fontsize=14, y=0.995)
fig.text(0.5, 0.925, 'Salaried people on a normal work day, by the three factors that explain the most.', ha='center', fontsize=9, color='0.3')
fig.text(0.01, 0.045, 'State, rural or urban and age matter less (each explains 2-4%); education level and household spending do not matter. All the factors tested together explain 25%.', fontsize=7, color='0.4')
fig.text(0.01, 0.015, 'Still working = between first and last paid work of the day, breaks of up to 4 hours included.', fontsize=7, color='0.4')
fig.text(0.99, 0.015, 'Source: NSO Time Use Survey 2024, weighted.', ha='right', fontsize=7, color='0.4')
fig.subplots_adjust(left=0.25, right=0.97, top=0.85, bottom=0.22)
fig.savefig(out, dpi=300, facecolor=BG, bbox_inches='tight')
