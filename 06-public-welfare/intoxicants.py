# coding: utf-8
import hces
import yaml
import pandas as pd

df = hces.load()
INTOXICANTS = yaml.safe_load("""  - 300
  - 301
  - 302
  - 310
  - 311
  - 316
  - 312
  - 314
  - 315
  - 313
  - 317
  - 322
  - 324
  - 323
  - 321
  - 320
  - 325
""")
INTOXICANTS
files = get_ipython().getoutput('ls ../../hces-2023-24/data/sec-12*.parquet')
files
data = []
for file in files:
    data.append(pd.read_parquet(files))

data = [k['cons_total_value'].unstack() for k in data]
idf = data[0].fillna(value=0)[INTOXICANTS]

xdf = df[df['is_hospitalization'] == 4].copy()
xdf['treat'] = xdf['is_hhmem_pmjay']
xdf['treat'] = xdf['is_hhmem_pmjay'] == 1
xdf
idf = idf.loc[xdf.index]
ix = idf.index.intersection(xdf.index)
len(ix)
len(ix) / len(xdf)
xdf = xdf.loc[ix]
idf = idf.loc[ix]
xdf = pd.concat([xdf, idf], axis=1, verify_integrity=True)
xdf
hces.compare(xdf, ['treat'], INTOXICANTS)
hces.compare(xdf, ['treat'], INTOXICANTS).T
hces.compare(xdf, ['treat'], INTOXICANTS).T.sum(axis=0)
psm = hces.propensity_score_match(
        xdf,
        num_cols=["family_size", "n_children", "n_elderly"],
        cat_cols=[
            "sector",
            "nss_region",
            "employed_annual",
            "max_income_from",
            "hoh_religion",
            "caste",
        ],
    )
    psm = psm[psm["label"].isin(["D", "E"])]
psm = hces.propensity_score_match(
    xdf,
    num_cols=["family_size", "n_children", "n_elderly"],
    cat_cols=[
        "sector",
        "nss_region",
        "employed_annual",
        "max_income_from",
        "hoh_religion",
        "caste",
    ],
)
psm = psm[psm["label"].isin(["D", "E"])]
hces.compare(psm, ['treat'], INTOXICANTS).T
hces.compare(psm, ['treat'], INTOXICANTS).T.sum(axis=0)
hces.ttest(psm, INTOXICANTS)
