"""Women's labour force participation in PLFS 2025 (calendar-year person file) and, for trend, PLFS 2023-24.
usage: python3 -I plfs_women.py <cperv12025.csv> <perv1.dta (2023-24)> <out.csv>
LFPR/WPR are shares of the age group. UPS = usual principal status only; UPSS = principal or subsidiary status
(the official 'usual status' measure). Weights: mult/100 (2025), mult/100 or /200 (2023-24)."""
import sys, numpy as np, pandas as pd
src25, src24, out = sys.argv[1:4]
c25 = ['sec','sex','age','marst','gedu_lvl','pas','has_sas','sas','rea','mult']
a = pd.read_csv(src25, usecols=c25, dtype=str)
for c in a.columns: a[c] = pd.to_numeric(a[c], errors='coerce')
a['w'] = a.mult / 100; a['year'] = '2025'
b = pd.read_stata(src24, convert_categoricals=False)
b = b.rename(columns={'b1q3_perv1':'sec','b4q5_perv1':'sex','b4q6_perv1':'age','b4q7_perv1':'marst','b4q8_perv1':'gedu_lvl',
                      'b5pt1q3_perv1':'pas','b5pt1q7_perv1':'has_sas','b5pt2q3_perv1':'sas','b5pt3q12_perv1':'rea'})
for c in ['sec','sex','age','marst','gedu_lvl','pas','has_sas','sas','rea','mult_perv1','NSS_perv1','NSC_perv1']: b[c] = pd.to_numeric(b[c], errors='coerce')
b['w'] = np.where(b.NSS_perv1 == b.NSC_perv1, b.mult_perv1 / 100, b.mult_perv1 / 200); b['year'] = '2023-24'
d = pd.concat([a[['year','sec','sex','age','marst','gedu_lvl','pas','has_sas','sas','rea','w']], b[['year','sec','sex','age','marst','gedu_lvl','pas','has_sas','sas','rea','w']]])
d = d[d.sex.isin([1, 2]) & (d.age >= 15)].copy()
d['sx'] = d.sex.map({1: 'men', 2: 'women'}); d['place'] = d.sec.map({1: 'rural', 2: 'urban'})
emp_p = d.pas.between(11, 72); lf_p = d.pas.between(11, 82)
emp_s = (d.has_sas == 1) & d.sas.between(11, 72)
d['lf_ups'] = lf_p; d['wk_ups'] = emp_p; d['lf_upss'] = lf_p | emp_s; d['wk_upss'] = emp_p | emp_s
d['regular'] = d.pas == 31
d['edu'] = pd.cut(d.gedu_lvl, [0, 4, 7, 8, 10, 11, 13], labels=['not literate / no schooling', 'below secondary', 'secondary', 'higher secondary', 'diploma/certificate', 'graduate+'])
d['ageb'] = pd.cut(d.age, [14, 19, 24, 29, 34, 44, 59, 120], labels=['15-19', '20-24', '25-29', '30-34', '35-44', '45-59', '60+'])
d['mar'] = d.marst.map({1: 'never married', 2: 'married', 3: 'widowed / divorced', 4: 'widowed / divorced'})
def sh(x, col): return float((x.w * x[col]).sum() / x.w.sum() * 100)
rows = []
def add(block, year, sx, group, item, val, n): rows.append((block, year, sx, group, item, round(val, 1), n))
for y in ['2023-24', '2025']:
    dy = d[d.year == y]
    for sx in ['men', 'women']:
        for place, m in [('all', dy.sx == sx), ('rural', (dy.sx == sx) & (dy.place == 'rural')), ('urban', (dy.sx == sx) & (dy.place == 'urban'))]:
            x = dy[m]
            for meas in ['lf_upss', 'lf_ups', 'wk_upss']: add('A headline, age 15+', y, sx, place, meas, sh(x, meas), len(x))
            add('A headline, age 15+', y, sx, place, 'regular wage as % of all', sh(x, 'regular'), len(x))
y25 = d[d.year == '2025']
for sx in ['men', 'women']:
    x0 = y25[y25.sx == sx]
    for col, lab in [('edu', 'education (age 25-59)'), ('ageb', 'age band'), ('mar', 'marital status (age 25-59)'), ('place', 'sector (age 25-59)')]:
        x1 = x0[x0.age.between(25, 59)] if col != 'ageb' else x0
        for v, x in x1.groupby(col, observed=True):
            add('B women/men by group (2025, UPSS LFPR %)', '2025', sx, lab, str(v), sh(x, 'lf_upss'), len(x))
    # who is employed: type of work
    e = x0[x0.wk_ups]
    for lab, m in [('regular wage', e.pas == 31), ('casual labour', e.pas.isin([41, 42, 51, 52])), ('own account / employer', e.pas.isin([11, 12])), ('unpaid family helper', e.pas == 21)]:
        add('C employed (UPS) by type, % of employed', '2025', sx, 'all', lab, float((e.w * m).sum() / e.w.sum() * 100), len(e))
# why are women out? main reason for principal status 'domestic duties' (92, 93), age 15-59
dom = y25[y25.pas.isin([92, 93]) & y25.age.between(15, 59)]
R = {1: 'lacked training/qualification/age', 2: 'no work at a convenient location', 3: 'health/age', 4: 'wants to continue study', 5: 'social reasons',
     6: 'financially well-off', 7: 'child care / home making', 9: 'others'}
for sx in ['women', 'men']:
    x = dom[dom.sx == sx]; x = x[x.rea.notna()]
    if len(x) > 50:
        for k_, v in R.items(): add('D why in domestic duties, age 15-59 (% of group)', '2025', sx, 'all', v, float((x.w * (x.rea == k_)).sum() / x.w.sum() * 100), len(x))
res = pd.DataFrame(rows, columns=['block', 'year', 'sex', 'group', 'item', 'value', 'n'])
res.to_csv(out, index=False)
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 500)
for blk in res.block.unique():
    print('\n##', blk); t = res[res.block == blk]
    print(t.pivot_table(index=['group', 'item'], columns=['year', 'sex'], values='value', sort=False).to_string())
