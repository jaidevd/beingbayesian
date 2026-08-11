"""Cohort-frozen 'genuine' questions + the saturation counterfactual trend.

Feeds saturation_chart.py.  Needs posts parquet + parse_postlinks.py output.
  genuine_fast = got an accepted answer within 90 days AND not closed within 90 days
                 (age-fair: measurable identically for every cohort)
  trend        = log-linear fit to 2014-2021 genuine volume, projected forward
"""
import pandas as pd, numpy as np

# global Id -> creation-date map (all posts), to date each accepted answer
ids, dates, qframes = [], [], []
for f in ["posts_1.parquet", "posts_2.parquet"]:
    df = pd.read_parquet(f, columns=["Id", "CreationDate", "PostTypeId",
                                     "AcceptedAnswerId", "ClosedDate"])
    idv = pd.to_numeric(df["Id"]).astype("int64").values
    cd = pd.to_datetime(df["CreationDate"], format="ISO8601").values
    ids.append(idv); dates.append(cd)
    m = df["PostTypeId"].values == "1"
    qframes.append(pd.DataFrame({
        "qid": idv[m], "qdate": cd[m],
        "acc": pd.to_numeric(df["AcceptedAnswerId"]).values[m],
        "closed": pd.to_datetime(df["ClosedDate"], format="ISO8601").values[m]}))

s = pd.Series(np.concatenate(dates), index=np.concatenate(ids))
s = s[~s.index.duplicated()]
q = pd.concat(qframes, ignore_index=True)

t_acc = (s.reindex(q["acc"].values).values - q["qdate"].values) / np.timedelta64(1, "D")
t_close = (q["closed"].values - q["qdate"].values) / np.timedelta64(1, "D")
accepted_90 = np.isfinite(t_acc) & (t_acc >= 0) & (t_acc <= 90)
closed_90 = np.isfinite(t_close) & (t_close >= 0) & (t_close <= 90)
genuine = accepted_90 & ~closed_90

g = pd.DataFrame({"month": pd.PeriodIndex(pd.to_datetime(q["qdate"]), freq="M"),
                  "genuine_fast": genuine, "all_q": 1}) \
    .groupby("month").agg(all_questions=("all_q", "sum"),
                          genuine_fast=("genuine_fast", "sum"))
g.index = g.index.to_timestamp()
g.to_csv("monthly_frozen.csv")

# saturation trend: log-linear on 2014-2021 genuine volume, projected across the series
pre = g["genuine_fast"][(g.index >= "2014-01-01") & (g.index < "2022-01-01")]
b = np.polyfit(np.arange(len(pre)), np.log(pre.values), 1)
tt = (g.index.year - pre.index[0].year) * 12 + (g.index.month - pre.index[0].month)
pd.Series(np.exp(np.polyval(b, tt)), index=g.index).to_csv(
    "frozen_saturation_trend.csv", header=["trend"])
print("pre-trend %.1f%%/yr" % ((np.exp(b[0]) ** 12 - 1) * 100))
