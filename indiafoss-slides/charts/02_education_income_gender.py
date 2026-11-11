"""Education vs. average monthly income, by gender and work status (PLFS 2023-24).

Projector-legible regeneration of the chart in 02-gig-economy/gig-final.ipynb
(cells 0-6). Data loading and categorisation are copied from the notebook, but the
means are survey-weighted by `subsample_multiplier` (the notebook used plain, unweighted
means, which is wrong for PLFS). In this extract NSS != NSC on every row, so PLFS's
official combined weight (MULT/200) is proportional to the raw multiplier and gives
identical means.

Run from anywhere:
    /Users/jaidevd/conda/bin/python3 indiafoss-slides/charts/02_education_income_gender.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
import pandas as pd  # noqa: E402
import yaml  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]  # beingbayesian/
OUT = ROOT / "indiafoss-slides" / "assets" / "02-education-income-gender.png"


def resolve_lfs(path: Path) -> Path:
    """Return a readable path; if `path` is an un-smudged git-lfs pointer, use the local LFS object."""
    head = path.read_bytes()[:200]
    if not head.startswith(b"version https://git-lfs"):
        return path
    oid = next(line.split(":", 1)[1] for line in head.decode().splitlines() if line.startswith("oid sha256:"))
    obj = ROOT / ".git" / "lfs" / "objects" / oid[:2] / oid[2:4] / oid
    if not obj.exists():
        raise FileNotFoundError(f"{path} is an LFS pointer and object {oid} is not in the local LFS store")
    return obj


# ---------------------------------------------------------------- data (gig-final.ipynb cells 0-5)
with open(ROOT / "plfs" / "perv1.map.yaml", "r") as fin:
    schema = yaml.safe_load(fin)
df = pd.read_parquet(resolve_lfs(ROOT / "02-gig-economy" / "data" / "gig-economy.parquet"))

codes = {v: k for k, v in schema["b6q5_perv1"]["categories"].items()}
SELF_EMPLOYED = [11, 12, 21, 61, 62]
SALARIED = [31, 71, 72]
CASUAL = [41, 42, 51]
UNEMPLOYED = [81]
df["cws"] = df["current_weekly_status_code"].map(codes).fillna("99").astype(int)
df["wf_status"] = "Not in Workforce"
df.loc[df["cws"].isin(SELF_EMPLOYED), "wf_status"] = "Self Employed"
df.loc[df["cws"].isin(SALARIED), "wf_status"] = "Salaried"
df.loc[df["cws"].isin(CASUAL), "wf_status"] = "Casual Labour"
df.loc[df["cws"].isin(UNEMPLOYED), "wf_status"] = "Unemployed"

df.loc[df["general_education"] == "others", "general_education"] = "literate without formal schooling: others"
df["broad_edu"] = df["general_education"]
df.loc[df["general_education"].str.startswith("literate without formal schooling"), "broad_edu"] = (
    "literate without formal schooling"
)
educat = pd.CategoricalDtype(
    ["not literate", "literate without formal schooling", "below primary",
     "primary", "secondary", "middle", "higher secondary", "diploma/certificate course",
     "graduate", "postgraduate and above"],
    ordered=True)
df["broad_edu"] = df["broad_edu"].astype(educat)


W = "subsample_multiplier"
MIN_N = 30  # minimum respondents for a plotted point
df["casual_monthly_wage"] = df[[c for c in df if c.startswith("wage_earned_")]].sum(axis=1) * 4


def wmean(x, col):
    v, w = x[col].astype("float64"), x[W].astype("float64")  # int32 product overflows
    return (v * w).sum() / w.sum() if w.sum() > 0 else float("nan")


def income_table(sub):
    cols = {"Casual Labour": "casual_monthly_wage", "Salaried": "weekly_salaried_earnings",
            "Self Employed": "weekly_self_employed_earnings"}
    t = pd.DataFrame({
        status: sub[sub["wf_status"] == status].groupby("broad_edu", observed=False)[[col, W]]
                   .apply(wmean, col)
        for status, col in cols.items()})
    n = pd.DataFrame({
        status: sub[sub["wf_status"] == status].groupby("broad_edu", observed=False).size()
        for status in cols})
    t = t.where(n >= MIN_N)  # hide points resting on too few respondents
    return t.iloc[:-1]  # drop 'postgraduate and above', as in the notebook


pdf_income_male = income_table(df[df["gender"] == "male"])
pdf_income_female = income_table(df[df["gender"] == "female"])
# drop education levels with no plottable point for either gender
_keep = pdf_income_male.notna().any(axis=1) | pdf_income_female.notna().any(axis=1)

# ---------------------------------------------------------------- plot
BG = "#FFEFD5"  # papayawhip
COLORS = {"Casual Labour": "maroon", "Salaried": "darkgoldenrod", "Self Employed": "teal"}
LABELS = ["Illiterate", "No formal schooling", "Below Primary", "Primary", "Secondary",
          "Middle School", "Higher Sec.", "Diploma", "Graduate"]
LABELS = [lab for lab, k in zip(LABELS, _keep) if k]
pdf_income_male, pdf_income_female = pdf_income_male[_keep], pdf_income_female[_keep]
from pathlib import Path as _P
for _f in sorted((_P(__file__).resolve().parent / "fonts").glob("Lora-*.ttf")):
    font_manager.fontManager.addfont(str(_f))
if any("Lora" in f.name for f in font_manager.fontManager.ttflist):
    plt.rcParams["font.family"] = "Lora"
plt.rcParams.update({"font.size": 13, "xtick.labelsize": 13, "ytick.labelsize": 13, "legend.fontsize": 13})

fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True, figsize=(7.0, 5.9), dpi=200,
                         layout="constrained")
fig.patch.set_facecolor(BG)
x = range(len(LABELS))
for ax, data, title in zip(axes, [pdf_income_male, pdf_income_female], ["Men", "Women"]):
    for col in data:
        ax.plot(x, data[col] / 1000, "-o", label=col, color=COLORS[col], linewidth=2.2, markersize=6.5, alpha=0.9)
    ax.set_facecolor(BG)
    ax.set_title(title, fontsize=15, fontweight="bold", loc="left")
    ax.grid(axis="y", linestyle="dashed", color="#bbbbbb", linewidth=0.8)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

axes[0].set_ylim(0, 22)
axes[0].set_yticks([0, 5, 10, 15, 20], ["0", "5k", "10k", "15k", "20k"])
axes[1].set_xticks(list(x), LABELS, rotation=35, ha="right", rotation_mode="anchor")
fig.supylabel("Average monthly income (Rs)", fontsize=14, fontweight="bold")
axes[1].set_xlabel("Education", fontsize=14, fontweight="bold")
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="outside upper center", ncol=3, frameon=False, fontsize=13,
           handlelength=1.6, columnspacing=1.2)

fig.savefig(OUT, dpi=200, facecolor=BG)
print(f"saved {OUT}")
print("Men\n", pdf_income_male.round(0).to_string())
print("Women\n", pdf_income_female.round(0).to_string())
