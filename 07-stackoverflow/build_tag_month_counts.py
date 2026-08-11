"""Full monthly question-count per tag, from the posts parquet (all-mention).

Outputs:
  tag_month_counts.parquet : (month, tag) -> number of questions created that month with that tag
  top10k_tags.csv          : the 10,000 highest-volume tags (used by the classifier)
"""
import pandas as pd, numpy as np

acc = None
for f in ["posts_1.parquet", "posts_2.parquet"]:
    df = pd.read_parquet(f, columns=["CreationDate", "PostTypeId", "Tags"])
    df = df[(df["PostTypeId"] == "1") & df["Tags"].notna()]
    month = pd.to_datetime(df["CreationDate"], format="ISO8601").dt.to_period("M")
    tags = df["Tags"].str.strip("<>").str.split("><")
    e = pd.DataFrame({"month": month.values.repeat(tags.str.len().values),
                      "tag": np.concatenate(tags.values)})
    g = e.groupby(["month", "tag"]).size()
    acc = g if acc is None else acc.add(g, fill_value=0)
    print(f, "done")

acc = acc.astype("int64")
acc.to_frame("n").to_parquet("tag_month_counts.parquet")

top = acc.groupby(level="tag").sum().sort_values(ascending=False).head(10000)
top.to_csv("top10k_tags.csv", header=["volume"])
print(f"wrote tag_month_counts.parquet ({len(acc):,} rows) and top10k_tags.csv")
