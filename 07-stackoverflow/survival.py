import pandas as pd, numpy as np

# 1. user-quarter activity (posted anything)
parts = []
for f in ["posts_1.parquet", "posts_2.parquet"]:
    df = pd.read_parquet(f, columns=["OwnerUserId", "CreationDate"]).dropna(subset=["OwnerUserId"])
    o = pd.to_numeric(df["OwnerUserId"]).astype("int64").values
    q = pd.to_datetime(df["CreationDate"], format="ISO8601").dt.to_period("Q")
    parts.append(pd.DataFrame({"u": o, "q": q.values}).drop_duplicates())
    print(f, "done")
ua = pd.concat(parts).drop_duplicates()

# 2. reputation (final snapshot) -> tiers
u = pd.read_parquet("users.parquet", columns=["Id", "Reputation"])
rep = pd.Series(pd.to_numeric(u["Reputation"]).values, index=u["Id"].values)

# 3. baseline cohort: active pre-ChatGPT (2022 Q1-Q3)
base_q = [pd.Period("2022Q1"), pd.Period("2022Q2"), pd.Period("2022Q3")]
cohort = ua.loc[ua["q"].isin(base_q), "u"].unique()
crep = rep.reindex(cohort)
bins = [-1, 99, 999, 9999, 99999, 10**12]
labels = ["<100", "100-1k", "1k-10k", "10k-100k", "100k+"]
tier = pd.cut(crep.values, bins=bins, labels=labels)
cohort_df = pd.DataFrame({"u": cohort, "tier": tier}).dropna(subset=["tier"])
size = cohort_df["tier"].value_counts()
print("\ncohort sizes by tier:\n", size)

# 4. quarterly retention: fraction of each tier still active
cset = set(cohort_df["u"].values)
uac = ua[ua["u"].isin(cset)].merge(cohort_df, on="u")
act = uac.groupby(["q", "tier"], observed=True)["u"].nunique().unstack("tier")
ret = (act / size).reindex(columns=labels)
ret = ret.loc[pd.Period("2021Q1"):pd.Period("2025Q4")]
ret.index = ret.index.to_timestamp()
ret.to_csv("survival.csv")
print("\nretention (fraction of pre-GPT cohort active):")
print(ret.loc[["2022-07-01", "2023-07-01", "2024-07-01", "2025-07-01"]].round(3))
