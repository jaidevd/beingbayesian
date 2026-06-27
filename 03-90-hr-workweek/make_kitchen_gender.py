# coding: utf-8
"""Standalone left panel of 'The Great Indian Kitchen': Kitchen Time by Gender.

Horizontal grouped bar chart of weekly hours spent on cooking activities by
gender (white-collar salaried workers, aged 15-60), survey-weighted.
Source: analysis.ipynb, left subplot (axbar).
"""
import json
import pandas as pd
import yaml
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_parquet("../../time-use-survey-2024/clean/per-tus-2024.parquet")
hdf = pd.read_parquet("../../time-use-survey-2024/clean/hh-tus-2024.parquet")
with open("nic-white-collar.yaml") as fin:
    NIC = yaml.safe_load(fin).keys()

df = df[df["usual_principal_activity_status"] == "worked as regular salaried/ wage employee"]
df = df[(df["age"] >= 15) & (df["age"] <= 60)]
df.dropna(subset=["activity_code"], inplace=True)


def get_time_spent(time_from, time_to):
    if time_from == time_to:
        return 24 * 60
    sh, sm = map(int, time_from.split(":"))
    eh, em = map(int, time_to.split(":"))
    m = eh * 60 + em - sh * 60 - sm
    return m if m > 0 else 24 * 60 + m


df["ts"] = df[["time_from", "time_to"]].apply(lambda x: get_time_spent(**x), axis=1)
cols = ["sector", "gender", "age", "marital_status", "education", "mult", "nic_2008_principal_activity"]
xdf = df.groupby(df.index)[cols].first()
df["ACT_CODE"] = df["activity_code"].astype(str).str.get(0).astype(int)
ACT_COLS = [f"ACT_{i}" for i in range(1, 10)]
ydf = df.groupby([df.index, "ACT_CODE"])["ts"].sum().unstack().fillna(0)
ydf.columns = ACT_COLS
pdf = pd.concat([xdf, ydf], axis=1)
pdf.index = pd.MultiIndex.from_tuples(pdf.index, names=df.index.names)
hh_info = hdf.loc[pdf.index.droplevel(-1).drop_duplicates(),
                  ["religion", "social_group", "total_monthly_ce", "energy_cooking",
                   "energy_lighting", "washing_type", "sweeping_type", "dwelling_unit",
                   "dwelling_unit_structure_type"]]
pdf = pdf.reset_index(-1).merge(hh_info, how="outer", left_index=True, right_index=True).reset_index().set_index(pdf.index.names, verify_integrity=True)
wc = pdf[pdf["nic_2008_principal_activity"].isin(NIC)]

xdf2 = df.loc[wc.index]
TIME = xdf2.groupby([xdf2.index, "activity_code"])["ts"].sum().unstack().fillna(0) * 7 / 60
meals = TIME[[c for c in TIME if str(c).startswith("31")]]
wc = pd.concat([wc, meals], axis=1)

ACTIVITY_LABELS = ["Preparing Meals / Snacks", "Serving", "Cleaning Up After",
                   "Storing / Preserving", "Other"]
mealtime = wc.groupby("gender").apply(
    lambda x: (x[meals.columns] * x["mult"].values.reshape(-1, 1)).sum(axis=0) / x["mult"].sum()
)
mealtime = mealtime.drop(["transgender"], axis=0)
mealtime.columns = ACTIVITY_LABELS
long = mealtime.stack().reset_index()
long.columns = ["gender", "activity", "time"]

def render(path, figsize, dpi, base_fontsize):
    plt.rcParams.update({"font.size": base_fontsize})
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi, facecolor="papayawhip")
    sns.barplot(long, x="time", y="activity", hue="gender",
                palette=["teal", "maroon"], ax=ax, alpha=0.8)
    ax.grid(True, axis="x", color="gray", linewidth=0.5, linestyle="dashed")
    ax.set_xlabel("Hours Per Week", fontweight="bold", fontsize=base_fontsize * 1.1)
    ax.set_ylabel("Cooking Activities", fontweight="bold", fontsize=base_fontsize * 1.1)
    ax.tick_params(labelsize=base_fontsize)
    ax.set_facecolor("papayawhip")
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(fontsize=base_fontsize, title="Gender", title_fontproperties={"weight": "bold"})
    ax.set_title("Gender in the Kitchen", fontweight="bold", fontsize=base_fontsize * 1.5)
    fig.tight_layout()
    fig.savefig(path, facecolor="papayawhip", bbox_inches="tight")
    plt.close(fig)


render("assets/kitchen-time-by-gender.png", figsize=(6, 4), dpi=100, base_fontsize=10)
render("assets/kitchen-time-by-gender-slide.png", figsize=(12, 6.75), dpi=300, base_fontsize=18)
print("saved chart")

spec = {
    "id": "kitchen-time-by-gender",
    "source": {
        "notebook": "03-90-hr-workweek/analysis.ipynb",
        "parent_figure": "The Great Indian Kitchen (left panel)",
        "dataset": "Time Use Survey 2024 (India), activity codes 31x",
    },
    "chart": {
        "type": "grouped_bar_horizontal",
        "title": "Gender in the Kitchen",
        "background_color": "papayawhip",
        "axes": {"x": {"label": "Hours Per Week"}, "y": {"label": "Cooking Activities"}},
        "series": [{"name": "female", "color": "teal"}, {"name": "male", "color": "maroon"}],
        "bar_alpha": 0.8,
        "grid": {"axis": "x", "color": "gray", "linewidth": 0.3, "linestyle": "dashed"},
        "spines_hidden": ["top", "right"],
    },
    "metric": {
        "name": "Average weekly hours on cooking activities",
        "unit": "hours per week",
        "population": "White-collar (NIC white-collar) regular salaried/wage workers, aged 15-60",
        "weighting": "Survey multiplier-weighted mean per gender (transgender excluded)",
        "definition": "Daily minutes on TUS activity codes 311-319 summed per person, scaled to weekly (x7/60), averaged within gender with survey weights.",
    },
    "data": {
        "categories": ACTIVITY_LABELS,
        "values": [
            {"activity": a,
             "female": round(float(mealtime.loc["female", a]), 4),
             "male": round(float(mealtime.loc["male", a]), 4)}
            for a in ACTIVITY_LABELS
        ],
    },
}
with open("assets/kitchen-time-by-gender.json", "w") as f:
    json.dump(spec, f, indent=2)
print("saved spec")
