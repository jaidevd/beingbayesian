import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.weightstats import ttest_ind
import string

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

    df["FOOD"] = food.sum(axis=1).fillna(0)
    df["EDUCATION"] = edu.sum(axis=1).fillna(0)
    df["HEALTH"] = health.sum(axis=1).fillna(0)

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


def propensity_score_match(df, num_cols, cat_cols, treat_col="treat", pscore_bins=5,
                           pscore_labels=None):
    xdf = df.copy()
    xdf["pscore"] = pd.NA
    xdf["support"] = False
    xdf["label"] = pd.Series(pd.NA, index=xdf.index, dtype="object")

    required_cols = list(dict.fromkeys(num_cols + cat_cols + [treat_col]))
    fit_ix = xdf.dropna(subset=required_cols).index
    if len(fit_ix) == 0:
        return xdf

    fit_df = xdf.loc[fit_ix]
    y = fit_df[treat_col].astype(int)
    if y.nunique() < 2:
        raise ValueError(f"`{treat_col}` must contain both treatment (1) and control (0) rows.")

    X_cat = pd.get_dummies(fit_df[cat_cols], drop_first=True)

    scaler = StandardScaler()
    X_num = pd.DataFrame(
        scaler.fit_transform(fit_df[num_cols]),
        columns=num_cols,
        index=fit_ix,
    )

    X = pd.concat([X_num, X_cat], axis=1)

    model = LogisticRegression(max_iter=5000)
    model.fit(X, y)
    xdf.loc[fit_ix, "pscore"] = model.predict_proba(X)[:, 1]

    treat_mask = y == 1
    control_mask = ~treat_mask

    fit_pscore = xdf.loc[fit_ix, "pscore"].astype(float)
    treat_min = fit_pscore.loc[treat_mask].min()
    treat_max = fit_pscore.loc[treat_mask].max()
    control_min = fit_pscore.loc[control_mask].min()
    control_max = fit_pscore.loc[control_mask].max()

    lo = max(treat_min, control_min)
    hi = min(treat_max, control_max)
    xdf.loc[fit_ix, "support"] = fit_pscore.between(lo, hi, inclusive="both")

    supported_ix = xdf.index[xdf["support"]]
    supported_scores = xdf.loc[supported_ix, "pscore"].astype(float)
    if supported_scores.nunique() >= 2:
        if pscore_labels is None:
            pscore_labels = list(string.ascii_uppercase[:pscore_bins])
        xdf.loc[supported_ix, "label"] = pd.qcut(
            supported_scores, pscore_bins, labels=pscore_labels, duplicates="drop"
        ).astype(str)

    return xdf
