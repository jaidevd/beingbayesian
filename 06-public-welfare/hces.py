import pandas as pd
from statsmodels.stats.weightstats import ttest_ind

EDU_COLS = ["books_1st", "books_2nd", "stationery", "fees", "coaching", "edu_other"]
HEALTH_COLS = [410, 411, 412, 413, 414, 420, 421, 422, 423, 424]
FOOD_COLS = [
    "cereals",
    "pulses",
    "sugar_salt",
    "dairy",
    "veg",
    "fruits",
    "meat",
    "oil",
    "spice",
    "bev",
    "cooked",
    "processed",
]


def load():
    df = pd.read_parquet("data/hh.parquet")
    services = pd.read_parquet("data/services.parquet")
    food = pd.read_parquet("data/food.parquet")
    health = pd.read_parquet("data/health.parquet")
    edu = pd.read_parquet("data/education.parquet")
    ration = pd.read_parquet("data/ration.parquet")
    ix = df.index
    for xdf in [services, food, health, edu, ration]:
        ix = ix.intersection(xdf.index)

    df = df.loc[ix]
    df["FOOD"] = food.loc[ix].sum(axis=1)
    df["EDUCATION"] = edu.loc[ix].sum(axis=1)
    df["HEALTH"] = health.loc[ix].sum(axis=1)

    return pd.concat([df, services, food, health, edu, ration], axis=1, verify_integrity=True)


def compare(df, group_cols, agg_cols, mult_col="multiplier"):
    return df.groupby(group_cols).apply(
        lambda x: (x[agg_cols] * x[mult_col].values.reshape(-1, 1)).sum(axis=0)
        / x[mult_col].sum()
    )


def ttest(x, cols, alternative="two-sided", treat_col="treat", mult_col="multiplier"):
    trix = x[x[treat_col]].index
    crix = x[~x[treat_col]].index
    pvals = {}
    for col in cols:
        _, p, _ = ttest_ind(
            x.loc[crix, col].fillna(0),
            x.loc[trix, col].fillna(0),
            weights=(x.loc[crix, mult_col], x.loc[trix, mult_col]),
            alternative=alternative,
        )
        pvals[col] = p
    return pd.Series(pvals)
