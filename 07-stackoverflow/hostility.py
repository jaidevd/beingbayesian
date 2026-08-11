import pandas as pd, numpy as np

frames = []
for f in ["posts_1.parquet", "posts_2.parquet"]:
    df = pd.read_parquet(f, columns=["Id", "OwnerUserId", "CreationDate",
                                     "PostTypeId", "ClosedDate", "Score",
                                     "AnswerCount"]).dropna(subset=["OwnerUserId"])
    frames.append(pd.DataFrame({
        "owner": pd.to_numeric(df["OwnerUserId"]).astype("int64").values,
        "date": pd.to_datetime(df["CreationDate"], format="ISO8601").values,
        "pt": df["PostTypeId"].values,
        "closed": df["ClosedDate"].notna().values,
        "score": pd.to_numeric(df["Score"]).fillna(0).values,
        "ans": pd.to_numeric(df["AnswerCount"]).fillna(0).values}))
    print(f, "loaded")
d = pd.concat(frames, ignore_index=True)
d = d.sort_values(["owner", "date"], kind="stable")
d["prior"] = d.groupby("owner", sort=False).cumcount()
d["total"] = d.groupby("owner", sort=False)["owner"].transform("size")

q = d[d["pt"] == "1"].copy()
q["month"] = pd.PeriodIndex(pd.to_datetime(q["date"]), freq="M")
q["downvoted"] = q["score"] < 0
q["ignored"] = q["ans"] == 0
q["rejected"] = q["closed"] | q["downvoted"]   # ACTIVE hostility (not supply-driven)
q["punished"] = q["rejected"] | q["ignored"]   # rejection + neglect

# --- aggregate friction rates over time (all questions) ---
g = q.groupby("month").agg(n=("pt", "size"), closed=("closed", "mean"),
                           downvoted=("downvoted", "mean"),
                           ignored=("ignored", "mean")).copy()
g.index = g.index.to_timestamp()
g.to_csv("hostility_rates.csv")

# --- the newcomer gauntlet: first post is a question ---
fq = q[q["prior"] == 0].copy()
fq["returned"] = fq["total"] > 1
fq["year"] = pd.to_datetime(fq["date"]).dt.year
coh = fq.groupby("year").agg(
    newcomers=("returned", "size"),
    rejected_rate=("rejected", "mean"),
    closed_rate=("closed", "mean"),
    downvoted_rate=("downvoted", "mean"),
    ignored_rate=("ignored", "mean"),
    ret_all=("returned", "mean"),
    ret_rejected=("returned", lambda s: s[fq.loc[s.index, "rejected"]].mean()),
    ret_ok=("returned", lambda s: s[~fq.loc[s.index, "rejected"]].mean()),
)
coh.to_csv("hostility_cohorts.csv")
print("\nFirst-question newcomers by cohort year:")
print(coh.round(3).to_string())
