"""Chart for 'the evening differs by gender': evening housework, women against men, in every split.
usage: python3 -I second_shift_charts.py <work dir with P2.pkl/G2.pkl> <splits-ci.csv> <out dir>
Writes evening-splits.png."""
import sys, re, numpy as np, pandas as pd, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.font_manager as fm
D, SPL, OUT = sys.argv[1:4]
for f in ['Bold', 'Regular']: fm.fontManager.addfont(f"/home/jaidevd/.local/share/fonts/Lora-{f}.ttf")
plt.rcParams['font.family'] = 'Lora'; BG = 'papayawhip'; WC, MC = 'maroon', 'teal'
sys.argv = [sys.argv[0], D, 'none']
exec(open(__import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/tab.py').read().split("if __name__")[0])
P3 = pd.read_pickle(D + '/P3.pkl')
# splits dot plot
s = pd.read_csv(SPL); s = s[(s.cohort == 'all salaried') & (s.day == 'work') & (s.split != 'care need in HH')]
def parse(t): m = re.match(r'\s*(\d+)\s*\[(\d+)-(\d+)\]', str(t)); return tuple(int(v) for v in m.groups())
rows = []
ORDER = [('sector', 'Place', ['Rural', 'Urban']), ('age', 'Age', ['<25', '25-34', '35-49', '50+']), ('marital', 'Marital status', ['not married', 'married']),
         ('social group', 'Social group', ['General', 'OBC', 'SC', 'ST']), ('religion', 'Religion', ['Hinduism', 'Islam', 'Christianity', 'other']),
         ('MPCE (grouped)', 'Household spending', ['Q1-2', 'Q3', 'Q4-5'])]
NAMES = {'Q1-2': 'Poorest 40%', 'Q3': 'Middle 20%', 'Q4-5': 'Richest 40%', 'Hinduism': 'Hindu', 'Islam': 'Muslim', 'Christianity': 'Christian', 'other': 'Other religion', '<25': 'Under 25', '25-34': '25 to 34', '35-49': '35 to 49', '50+': '50 and over', 'not married': 'Not married', 'married': 'Married'}
fig, ax = plt.subplots(figsize=(8.6, 8.8)); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.spines[['top', 'right', 'left']].set_visible(False); ax.grid(axis='x', color='gray', linewidth=0.3, linestyle='dashed'); ax.set_axisbelow(True)
y = 0; ytk = []; ylb = []
for sp, head, vals in ORDER:
    ax.text(-0.02, y - 0.1, head.upper(), transform=ax.get_yaxis_transform(), ha='right', va='center', fontsize=8, color='0.45', fontweight='bold')
    y += 0.9
    for v in vals:
        for g_, col, off in [('F', WC, -0.12), ('M', MC, 0.12)]:
            r = s[(s.split == sp) & (s.value == v) & (s.gender == g_)]
            if r.empty: continue
            e, lo, hi = parse(r.iloc[0].domestic)
            ax.plot([lo, hi], [y + off] * 2, color=col, lw=1.6, alpha=0.7); ax.plot(e, y + off, 'o', color=col, ms=7)
            if g_ == 'F': fe = e
            else: ax.text(104, y, f'{fe / e:.0f}x', ha='right', va='center', fontsize=9, color='0.3', fontweight='bold')
        ytk.append(y); ylb.append(NAMES.get(v, v)); y += 1
    y += 0.6
ax.set_yticks(ytk); ax.set_yticklabels(ylb, fontsize=9.5); ax.tick_params(axis='y', length=0); ax.invert_yaxis()
ax.set_xlim(0, 106); ax.set_xlabel('minutes (dot = average, line = 95% interval)', fontsize=9)
ax.plot([], [], 'o', color=WC, label='Women'); ax.plot([], [], 'o', color=MC, label='Men'); fig.legend(frameon=False, loc='lower center', ncol=2, fontsize=10, bbox_to_anchor=(0.5, 0.025))
fig.suptitle('In All 19 Groups, Women Do 4 to 12 Times the Evening Housework', fontweight='bold', fontsize=14, y=0.985)
fig.text(0.5, 0.94, 'Minutes of housework between 5 pm and midnight for salaried women and men on a normal work day; the multiple is women over men.', ha='center', fontsize=9, color='0.3')
fig.text(0.99, 0.005, 'Source: NSO Time Use Survey 2024, weighted.', ha='right', fontsize=7, color='0.4')
fig.subplots_adjust(left=0.24, right=0.97, top=0.9, bottom=0.12)
fig.savefig(OUT + '/evening-splits.png', dpi=300, facecolor=BG, bbox_inches='tight')
