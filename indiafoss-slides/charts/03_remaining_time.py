# coding: utf-8
"""Slide chart: the remaining weekly time budget of white-collar salaried workers.

Horizontal grouped bars of survey-weighted hours per week, by gender, for
Sleep, Talking & Chatting, Watching TV, Eating, Personal Care & Hygiene and
Resting & Relaxing. Data and computation mirror 03-90-hr-workweek/analysis.ipynb
(cells 0, 1, 7, 10); the plot is restyled for projector legibility.

Run from anywhere:
    /Users/jaidevd/conda/bin/python indiafoss-slides/charts/03_remaining_time.py
Writes indiafoss-slides/assets/03-remaining-time.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
import pandas as pd
import yaml

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent / "03-90-hr-workweek"
TUS = HERE.parent.parent.parent / "time-use-survey-2024" / "clean"
OUT = HERE.parent / "assets" / "03-remaining-time.png"

# ---------------------------------------------------------------- data (notebook cells 0-1)
df = pd.read_parquet(TUS / "per-tus-2024.parquet")
hdf = pd.read_parquet(TUS / "hh-tus-2024.parquet")
with open(PROJECT / "nic-white-collar.yaml") as fin:
    NIC = yaml.safe_load(fin).keys()

df = df[df["usual_principal_activity_status"] == "worked as regular salaried/ wage employee"]
df = df[df["age"] >= 15]
df = df[df["age"] <= 60]
df.dropna(subset=["activity_code"], inplace=True)


def get_time_spent(time_from, time_to):
    if time_from == time_to:
        return 24 * 60
    start_hour, start_min = map(int, time_from.split(":"))
    end_hour, end_min = map(int, time_to.split(":"))
    minutes = end_hour * 60 + end_min - start_hour * 60 - start_min
    if minutes > 0:
        return minutes
    return 24 * 60 + minutes


df["ts"] = df[["time_from", "time_to"]].apply(lambda x: get_time_spent(**x), axis=1)

cols = ["sector", "gender", "age", "marital_status", "education", "mult",
        "nic_2008_principal_activity"]
xdf = df.groupby(df.index)[cols].first()
df["ACT_CODE"] = df["activity_code"].astype(str).str.get(0).astype(int)
ydf = df.groupby([df.index, "ACT_CODE"])["ts"].sum().unstack().fillna(value=0)
ydf.columns = [f"ACT_{i}" for i in range(1, 10)]
pdf = pd.concat([xdf, ydf], axis=1)
pdf.index = pd.MultiIndex.from_tuples(pdf.index, names=df.index.names)
hh_info = hdf.loc[pdf.index.droplevel(-1).drop_duplicates(),
                  ["religion", "social_group", "total_monthly_ce",
                   "energy_cooking", "energy_lighting", "washing_type",
                   "sweeping_type", "dwelling_unit", "dwelling_unit_structure_type"]]
pdf = pdf.reset_index(-1).merge(
    hh_info, how="outer", left_index=True, right_index=True
).reset_index().set_index(pdf.index.names, verify_integrity=True)
wc = pdf[pdf["nic_2008_principal_activity"].isin(NIC)]

# ---------------------------------------------------------------- notebook cell 7
xdf2 = df.loc[wc.index]
TIME = xdf2.groupby([xdf2.index, "activity_code"])["ts"].sum().unstack().fillna(value=0) * 7 / 60

# ---------------------------------------------------------------- notebook cell 10
codes = {
    911: "Sleep",
    711: "Talking & Chatting",
    842: "Watching TV",
    921: "Eating",
    931: "Personal Care & Hygiene",
    850: "Resting & Relaxing",
}
social = TIME[list(codes.keys())].copy()
social[["gender", "mult"]] = wc.loc[social.index, ["gender", "mult"]]
socialtime = social.groupby("gender").apply(
    lambda x: pd.Series(
        (x[list(codes.keys())].values * x["mult"].values.reshape(-1, 1)).sum(axis=0)
        / x["mult"].sum(),
        index=list(codes.keys()),
    )
)
socialtime = socialtime.drop(["transgender"], axis=0)

print("Survey-weighted hours per week:")
for code, label in codes.items():
    print(f"  {label:<26s} female={socialtime.loc['female', code]:.4f}  "
          f"male={socialtime.loc['male', code]:.4f}")

# ---------------------------------------------------------------- style
BG = "#FFEFD5"  # papayawhip
from pathlib import Path as _P
for _f in sorted((_P(__file__).resolve().parent / "fonts").glob("Lora-*.ttf")):
    font_manager.fontManager.addfont(str(_f))
available = {f.name for f in font_manager.fontManager.ttflist}
for family in ("Lora", "Georgia"):
    if family in available:
        plt.rcParams["font.family"] = family
        break
print("font:", plt.rcParams["font.family"])

TICK = 14
LABEL = 14
VALUE = 13

TICK_LABELS = {
    911: "Sleep",
    711: "Talking &\nChatting",
    842: "Watching TV",
    921: "Eating",
    931: "Personal Care\n& Hygiene",
    850: "Resting &\nRelaxing",
}

# ---------------------------------------------------------------- plot
fig, ax = plt.subplots(figsize=(7.0, 5.9), dpi=200, facecolor=BG, layout="constrained")
ax.set_facecolor(BG)

y = np.arange(len(codes))
h = 0.38
series = [("female", "Women", "teal", -h / 2), ("male", "Men", "maroon", h / 2)]
for key, name, color, off in series:
    vals = socialtime.loc[key, list(codes.keys())].values
    ax.barh(y + off, vals, height=h, color=color, alpha=0.85, label=name, zorder=3)
    for yi, v in zip(y + off, vals):
        ax.text(v + 0.8, yi, f"{v:.1f}", va="center", ha="left",
                fontsize=VALUE, color=color, zorder=4)

ax.set_yticks(y, [TICK_LABELS[c] for c in codes], fontweight="bold")
ax.invert_yaxis()
ax.set_xlim(0, 66)
ax.set_xticks(range(0, 61, 10))
ax.tick_params(labelsize=TICK)
ax.tick_params(axis="y", length=0)
ax.set_xlabel("Hours Per Week", fontsize=LABEL, fontweight="bold")
ax.grid(True, axis="x", color="gray", linewidth=0.5, linestyle="dashed", zorder=0)
ax.set_axisbelow(True)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(loc="lower right", fontsize=TICK, frameon=False)

fig.savefig(OUT, facecolor=BG)
print("saved", OUT)
