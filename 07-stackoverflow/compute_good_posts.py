"""Monthly counts of all / composite-good / canonical questions.

Feeds genuine_vs_all_chart.py.  Needs posts parquet + parse_postlinks.py outputs.
  composite_good = never closed & never duplicated & has accepted answer &
                   top-quartile score within its creation-year cohort
  canonical      = a question others were duplicated to, or linked to >= 5 times
"""
import pandas as pd, numpy as np

dup_src = set(np.load("duplicate_ids.npy").tolist())
dup_tgt = set(np.load("dup_target_ids.npy").tolist())
z = np.load("link_in_counts.npz")
linked5 = set(z["ids"][z["counts"] >= 5].tolist())
canonical_ids = dup_tgt | linked5

frames = []
for f in ["posts_1.parquet", "posts_2.parquet"]:
    df = pd.read_parquet(f, columns=["Id", "CreationDate", "PostTypeId",
                                     "AcceptedAnswerId", "ClosedDate", "Score"])
    df = df[df["PostTypeId"] == "1"]
    dt = pd.to_datetime(df["CreationDate"], format="ISO8601")
    frames.append(pd.DataFrame({
        "Id": pd.to_numeric(df["Id"]).values,
        "month": dt.dt.to_period("M").values, "year": dt.dt.year.values,
        "score": pd.to_numeric(df["Score"]).values,
        "accepted": df["AcceptedAnswerId"].notna().values,
        "closed": df["ClosedDate"].notna().values}))
q = pd.concat(frames, ignore_index=True)

thr = q.groupby("year")["score"].quantile(0.75)
top_q = q["score"].values >= q["year"].map(thr).values
not_dup = ~q["Id"].isin(dup_src).values
composite = (~q["closed"].values) & not_dup & q["accepted"].values & top_q
canonical = q["Id"].isin(canonical_ids).values

res = pd.DataFrame({
    "all_questions": q.groupby("month").size(),
    "composite_good": q[composite].groupby("month").size(),
    "canonical_good": q[canonical].groupby("month").size(),
}).fillna(0).astype("int64")
res.index = res.index.to_timestamp()
res.to_csv("monthly_good_posts.csv")
print(res.sum())
