# coding: utf-8
"""Two-panel dumbbell chart of absolute per-adult monthly intoxicant spend.

One panel per sector (rural | urban). In each panel, every row is an intoxicant
item with two points: insured (health-insurance beneficiary) vs non-insured
households. Styling mirrors assets/Health Insurance-Intoxicants.png.
"""
import json
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import hces

INTOXICANT_ITEMS = {
    300: "pan leaf", 301: "pan finished", 302: "ingredients for pan", 310: "bidi",
    311: "cigarettes", 312: "leaf tobacco", 313: "snuff", 314: "hookah tobacco",
    315: "cheroot", 316: "gutka/zarda/kimam/surti", 317: "other tobacco products",
    320: "ganja", 321: "toddy", 322: "country liquor", 323: "beer",
    324: "foreign liquor/wine", 325: "other intoxicants",
}

idf = pd.read_parquet("../../hces-2023-24/data/sec-12.1-CSQ.parquet")["cons_total_value"].unstack()
idf = pd.concat([idf, pd.read_parquet("../../hces-2023-24/data/sec-12.2-CSQ.parquet")["cons_total_value"].unstack()], axis=1, verify_integrity=True)
idf = pd.concat([idf, pd.read_parquet("../../hces-2023-24/data/sec-12.3-CSQ.parquet")["cons_total_value"].unstack()], axis=1, verify_integrity=True)
idf = idf.fillna(0)[list(INTOXICANT_ITEMS.keys())]
df = hces.load()
ix = df.index.intersection(idf.index)
df = pd.concat([df.loc[ix], idf.loc[ix]], axis=1)

xdf = df.copy()
xdf["treat"] = (xdf["is_benefit_healthscheme"] == 1) | (xdf["is_hhmem_pmjay"] == 1)
psm = hces.propensity_score_match(
    xdf,
    num_cols=["family_size", "n_children", "n_elderly"],
    cat_cols=["sector", "nss_region", "employed_annual", "max_income_from", "hoh_religion", "caste"],
)
psm = psm[psm["label"].isin(["D", "E"])]
cols = list(INTOXICANT_ITEMS.keys())
psm[cols] /= (psm["family_size"] - psm["n_children"]).values.reshape(-1, 1)

# Absolute, per-adult, monthly weighted means grouped by sector & treat.
intox = hces.compare(psm, ["sector", "treat"], cols) * 52 / 12
intox = intox.rename(INTOXICANT_ITEMS, axis=1)
intox["Paan"] = intox.pop("pan leaf") + intox.pop("pan finished") + intox.pop("ingredients for pan")
intox["Gutkha"] = intox.pop("gutka/zarda/kimam/surti")
intox.columns = [c.title() for c in intox.columns]
intox.drop(["Snuff", "Cheroot", "Ganja", "Hookah Tobacco"], axis=1, inplace=True)

# Shared row order (ascending by overall max across panels & series) so rows align.
ordered_items = intox.max(axis=0).sort_values(ascending=True).index.tolist()

fm.fontManager.addfont("/home/jaidevd/.local/share/fonts/Lora-Bold.ttf")
fm.fontManager.addfont("/home/jaidevd/.local/share/fonts/Lora-Regular.ttf")

SECTORS = ["rural", "urban"]
SERIES = {False: ("Not insured", "maroon"), True: ("Insured", "teal")}
xmax = intox.max().max() * 1.08

fig, axes = plt.subplots(1, 2, figsize=(11, 5), dpi=300, sharey=True)
for ax, sector in zip(axes, SECTORS):
    panel = intox.xs(sector, level="sector").T.loc[ordered_items]
    y = range(len(panel))
    ax.hlines(y, panel.min(axis=1), panel.max(axis=1), color="0.75", lw=2, zorder=1)
    for treat, (lbl, color) in SERIES.items():
        ax.scatter(panel[treat], y, s=55, color=color, label=lbl, zorder=2)
    ax.set_yticks(list(y))
    ax.set_yticklabels(ordered_items, fontfamily="Lora", fontweight="bold", fontsize=8)
    ax.set_title(sector.title(), fontfamily="Lora", fontweight="bold")
    ax.set_xlabel("Monthly spend (Rs. per adult)", fontfamily="Lora", fontweight="bold")
    ax.set_xlim(0, xmax)
    ax.set_facecolor("papayawhip")
    ax.set_axisbelow(True)
    ax.grid(axis="y", color="0.85", lw=0.6, zorder=0)

axes[1].legend(title="Health insurance", prop=dict(family="Lora"),
               title_fontproperties=dict(family="Lora"), loc="lower right")
fig.suptitle("Health Insurance & Addiction", fontfamily="Lora",
             fontweight="bold", fontsize=16, y=1.02)
fig.set_facecolor("papayawhip")
plt.tight_layout()
fig.savefig("assets/Health Insurance-Intoxicants-panels.png", facecolor="papayawhip", bbox_inches="tight")
print("saved chart")

# JSON spec
spec = {
    "id": "health-insurance-intoxicants-panels",
    "chart": {"type": "dumbbell", "panels": SECTORS,
              "series": [{"name": "Not insured", "color": "maroon"},
                         {"name": "Insured", "color": "teal"}]},
    "row_order": ordered_items,
    "data": {
        sector: [
            {"item": item,
             "not_insured": round(float(intox.loc[(sector, False), item]), 4),
             "insured": round(float(intox.loc[(sector, True), item]), 4)}
            for item in ordered_items
        ]
        for sector in SECTORS
    },
}
with open("assets/Health Insurance-Intoxicants-panels.json", "w") as f:
    json.dump(spec, f, indent=2)
print("saved spec")
