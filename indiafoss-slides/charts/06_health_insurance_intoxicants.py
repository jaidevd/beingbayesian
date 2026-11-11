# coding: utf-8
"""Slide-legible rebuild of 06-health-insurance-intoxicants-panels.png.

Values come from the spec JSON written by 06-public-welfare/make_intox_panels.py
(HCES 2023-24, propensity-score matched, strata D & E, per-adult monthly spend);
--recompute reruns that script's pipeline verbatim instead (see note below).
Only the presentation changes: 7.0 x 5.9 in @ 200 dpi for a 700x590 slide box,
13pt+ text, no suptitle.

Run from anywhere:
    LORA_DIR=/path/to/lora/ttfs /Users/jaidevd/conda/bin/python \
        indiafoss-slides/charts/06_health_insurance_intoxicants.py [--recompute]
LORA_DIR must hold Lora-Regular.ttf and Lora-Bold.ttf (static, not variable);
~/Library/Fonts and ~/.local/share/fonts are also searched. Falls back to Georgia.
"""
import json
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.font_manager as fm  # noqa: E402
import pandas as pd  # noqa: E402

HERE = Path(__file__).resolve().parent
SRC = HERE.parent.parent / "06-public-welfare"
OUT = HERE.parent / "assets" / "06-health-insurance-intoxicants-panels.png"
sys.path.insert(0, str(SRC))
os.chdir(SRC)  # hces.load() and the sec-12 paths are relative to this dir
import hces  # noqa: E402


# ---- data -------------------------------------------------------------------
# Default source: the JSON spec that make_intox_panels.py wrote in the same run
# as the published chart, so plotted values are identical to the original.
# Re-running the pipeline on this machine (sklearn 1.6.1 / pandas 2.3.3, macOS)
# drifts by up to ~0.3 Rs/row (logistic-regression propensity scores move a few
# households across the D/E quintile boundary). Pass --recompute to plot the
# fresh pipeline output instead; the max deviation is printed either way.
SPEC = SRC / "assets" / "Health Insurance-Intoxicants-panels.json"
SECTORS = ["rural", "urban"]


def recompute():
    """Verbatim pipeline from make_intox_panels.py. Returns the `intox` frame."""
    INTOXICANT_ITEMS = {
        300: "pan leaf", 301: "pan finished", 302: "ingredients for pan", 310: "bidi",
        311: "cigarettes", 312: "leaf tobacco", 313: "snuff", 314: "hookah tobacco",
        315: "cheroot", 316: "gutka/zarda/kimam/surti", 317: "other tobacco products",
        320: "ganja", 321: "toddy", 322: "country liquor", 323: "beer",
        324: "foreign liquor/wine", 325: "other intoxicants",
    }

    idf = pd.read_parquet("../../hces-2023-24/data/sec-12.1-CSQ.parquet")["cons_total_value"].unstack()
    idf = pd.concat([idf, pd.read_parquet("../../hces-2023-24/data/sec-12.2-CSQ.parquet")["cons_total_value"].unstack()], axis=1, verify_integrity=True)  # noqa: E501
    idf = pd.concat([idf, pd.read_parquet("../../hces-2023-24/data/sec-12.3-CSQ.parquet")["cons_total_value"].unstack()], axis=1, verify_integrity=True)  # noqa: E501
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

    intox = hces.compare(psm, ["sector", "treat"], cols) * 52 / 12
    intox = intox.rename(INTOXICANT_ITEMS, axis=1)
    intox["Paan"] = intox.pop("pan leaf") + intox.pop("pan finished") + intox.pop("ingredients for pan")
    intox["Gutkha"] = intox.pop("gutka/zarda/kimam/surti")
    intox.columns = [c.title() for c in intox.columns]
    intox.drop(["Snuff", "Cheroot", "Ganja", "Hookah Tobacco"], axis=1, inplace=True)
    return intox


spec = json.loads(SPEC.read_text())
ordered_items = spec["row_order"]
saved = pd.DataFrame(
    {(s, t): {r["item"]: r[k] for r in spec["data"][s]}
     for s in SECTORS for t, k in ((False, "not_insured"), (True, "insured"))}
).T
saved.index.names = ["sector", "treat"]
if "--recompute" in sys.argv:
    intox = recompute()
    dev = (intox.loc[saved.index, ordered_items] - saved[ordered_items]).abs().max().max()
    print(f"recomputed; max |deviation| from saved spec = {dev:.4f} Rs", file=sys.stderr)
    assert intox.max(axis=0).sort_values().index.tolist() == ordered_items
else:
    intox = saved
    print("using saved spec values from", SPEC.name, file=sys.stderr)

# ---- presentation ------------------------------------------------------------
LABELS = {"Other Tobacco Products": "Other Tobacco"}  # only shortening applied

font_dirs = [os.environ.get("LORA_DIR", ""), Path(__file__).resolve().parent / "fonts", Path.home() / "Library/Fonts",
             Path.home() / ".local/share/fonts"]
for d in font_dirs:
    if d and all((Path(d) / f"Lora-{w}.ttf").exists() for w in ("Regular", "Bold")):
        for w in ("Regular", "Bold"):
            fm.fontManager.addfont(str(Path(d) / f"Lora-{w}.ttf"))
        plt.rcParams["font.family"] = "Lora"
        break
else:
    plt.rcParams["font.family"] = "Georgia"
print("font:", plt.rcParams["font.family"], file=sys.stderr)

BG = "#FFEFD5"  # papayawhip
SERIES = {False: ("Not insured", "maroon"), True: ("Insured", "teal")}
plt.rcParams.update({"font.size": 13, "xtick.labelsize": 13, "ytick.labelsize": 13,
                     "legend.fontsize": 13})
xmax = intox.max().max() * 1.08

fig, axes = plt.subplots(1, 2, figsize=(7.0, 5.9), dpi=200, sharey=True,
                         layout="constrained", facecolor=BG)
for ax, sector in zip(axes, SECTORS):
    panel = intox.xs(sector, level="sector").T.loc[ordered_items]
    y = range(len(panel))
    ax.hlines(y, panel.min(axis=1), panel.max(axis=1), color="0.72", lw=2.5, zorder=1)
    for treat, (lbl, color) in SERIES.items():
        ax.scatter(panel[treat], y, s=70, color=color, label=lbl, zorder=2)
    ax.set_yticks(list(y))
    ax.set_yticklabels([LABELS.get(i, i) for i in ordered_items], fontweight="bold")
    ax.set_title(sector.title(), fontsize=15, fontweight="bold")
    ax.set_xlim(0, xmax)
    ax.set_xticks([0, 20, 40, 60, 80])
    ax.set_ylim(-0.6, len(panel) - 0.4)
    ax.set_facecolor(BG)
    ax.set_axisbelow(True)
    ax.grid(color="0.8", lw=0.7, ls="--", zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(axis="y", length=0)

fig.supxlabel("Monthly spend (Rs. per adult)", fontsize=14, fontweight="bold")
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="outside upper center", ncol=2, frameon=False,
           fontsize=13, handletextpad=0.3, columnspacing=1.5)
fig.savefig(OUT, facecolor=BG)
print("saved", OUT, file=sys.stderr)
