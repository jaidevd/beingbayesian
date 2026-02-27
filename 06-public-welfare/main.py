import hces
import pandas as pd

df = hces.load()
org = pd.read_parquet("../../hces-2023-24/data/sec-4.2-CSQ.parquet")

df["num_hhmem_publicedu"] = org.loc[df.index, "num_hhmem_publicedu"].fillna(0)
df["num_hhmem_privedu"] = org.loc[df.index, "num_hhmem_privedu"].fillna(0)
df["n_enrolled"] = df["num_hhmem_privedu"] + df["num_hhmem_publicedu"]

df[hces.FOOD_COLS] = df[hces.FOOD_COLS] / df["family_size"].values.reshape(-1, 1)
df["food"] = df[hces.FOOD_COLS].sum(axis=1)  # Food per capita

df["books"] = df.pop("books_1st").fillna(0) + df.pop("books_2nd").fillna(0)
hces.EDU_COLS.remove("books_1st")
hces.EDU_COLS.remove("books_2nd")
hces.EDU_COLS.append("books")

cooked_food = pd.read_parquet('../../hces-2023-24/data/sec-7.1-FDQ.parquet')
cooked_food = cooked_food['cons_total_value'].unstack()


hh_has_student = (df["n_enrolled"] != 0).values

df.loc[~hh_has_student, hces.EDU_COLS] = 0
df.loc[hh_has_student, hces.EDU_COLS] /= df.loc[hh_has_student, "n_enrolled"].values.reshape(-1, 1)
df["education"] = df[hces.EDU_COLS].sum(axis=1)


def run(xdf, name=""):
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
    if name == "Midday Meals":
        ix = psm[psm['treat']].index
        ix = cooked_food.index.intersection(ix)
        school_food_values = cooked_food.loc[ix, 281].fillna(0)
        psm.loc[psm["treat"], "cooked"] -= school_food_values
    x_edu = hces.compare(psm[psm["n_enrolled"] > 0], ["treat"], hces.EDU_COLS)
    x_food = hces.compare(psm, ["treat"], hces.FOOD_COLS)

    return pd.concat([x_food, x_edu], axis=1).reset_index()


DATA = []

# PDS

xdf = df.copy()
xdf["treat"] = (df["has_benefited_from_pmgky"] == "yes") | (df["used_ration_card"] == "yes")
out = run(xdf)
out["scheme"] = "PDS"
DATA.append(out)

# Health insurance safetynet

xdf = df[df["is_hospitalization"] == 4].copy()
xdf["treat"] = xdf["is_hhmem_pmjay"] == 1
out = run(xdf)
out["scheme"] = "Health Insurance"

DATA.append(out)

# Midday meals
xdf = df[(df["num_hhmem_publicedu"] > 0) & (df["n_children"] > 0)].copy()
xdf["treat"] = xdf["n_school_meals"] > 0
out = run(xdf, name="Midday Meals")
out["scheme"] = "Midday Meals"
DATA.append(out)

# LPG Subsidy

xdf = df[df["energy_source_cooking"] == "LPG"].copy()
xdf["treat"] = xdf["received_subsidy_lpg"] == 1

out = run(xdf)
out["scheme"] = "LPG Subsidy"
DATA.append(out)

# Free electricity
xdf = df[df["energy_source_lighting"].str.startswith("electricity")].copy()
xdf["treat"] = xdf["received_free_electricity"] == 1

out = run(xdf)
out["scheme"] = "Free Electricity"
DATA.append(out)


pd.concat(DATA, axis=0).to_parquet("data/main.parquet")
