import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
import numpy as np
import pandas as pd

fm.fontManager.addfont("/home/jaidevd/.local/share/fonts/Lora-Bold.ttf")
fm.fontManager.addfont("/home/jaidevd/.local/share/fonts/Lora-Regular.ttf")

cls = pd.read_csv("tag_classification_extended.csv").set_index("tag")["cat"].to_dict()
s = pd.read_parquet("tag_month_counts.parquet")["n"]
s.index = s.index.set_levels(s.index.levels[0].to_timestamp(), level=0)
wide = s.unstack("tag").sort_index()            # months x tags
wide = wide.loc["2019-01-01":]

# top 5 tags per category (40 rows), ordered by category-collapse then volume
tot = wide.sum().sort_values(ascending=False)
cat_order = ["platforms","frameworks","tools-and-infrastructure","concepts",
             "languages","markup-and-styling","servers","databases-and-libraries"]
top = []
for c in cat_order:
    top += [t for t in tot.index if cls.get(t) == c][:5]

M = wide[top].T                                  # tags x months
base = M.loc[:, "2022-01-01":"2022-09-01"].mean(axis=1)
idx = M.div(base, axis=0) * 100
idx = idx.rolling(3, axis=1, center=True, min_periods=1).mean()   # no NaN edge columns

cmap = LinearSegmentedColormap.from_list("drain", ["#6b1f1f", "#e8c9a0", "papayawhip", "#5aa0a0", "teal"])
norm = TwoSlopeNorm(vmin=0, vcenter=100, vmax=170)

fig, ax = plt.subplots(figsize=(13, 12), dpi=300)
fig.patch.set_facecolor("papayawhip")
ax.set_facecolor("papayawhip")
months = idx.columns
im = ax.imshow(idx.values, aspect="auto", cmap=cmap, norm=norm,
               extent=[0, len(months), len(top), 0], interpolation="nearest")

# ChatGPT line
gpt_col = list(months).index(pd.Timestamp("2022-11-01"))
ax.axvline(gpt_col, color="black", lw=1.2, ls="--")
ax.text(gpt_col + 1.5, 2, "ChatGPT", fontfamily="Lora", fontsize=9, color="black", va="top")

# year x-ticks
yrs = pd.date_range("2019-01-01", months[-1], freq="YS")
ax.set_xticks([list(months).index(y) for y in yrs if y in months])
ax.set_xticklabels([y.year for y in yrs if y in months], fontfamily="Lora")

# individual tag labels INSIDE the cells (title-cased, on white)
ax.set_yticks([])
for i, t in enumerate(top):
    ax.text(0.6, i + 0.5, t.title(), ha="left", va="center", fontfamily="Lora",
            fontsize=8, color="black",
            bbox=dict(facecolor="white", alpha=0.92, edgecolor="none", pad=0.7))

# category separators + rotated Title-Cased band labels OUTSIDE the rectangle
ax.set_xlim(0, len(months))
cats_in_order = [cls[t] for t in top]
i = 0
while i < len(top):
    c = cats_in_order[i]; j = i
    while j < len(top) and cats_in_order[j] == c:
        j += 1
    if i:
        ax.axhline(i, color="papayawhip", lw=2.5)
    label = c.replace("-and-", " & ").replace("-", " ").title()
    ax.text(-len(months) * 0.022, (i + j) / 2, label, rotation=90,
            ha="center", va="center", fontfamily="Lora", fontsize=11,
            fontweight="bold", color="0.25", clip_on=False)
    i = j

ax.set_title("Every tag drains at once (top 5 per category): volume vs. each tag's 2022 level",
             fontfamily="Lora", fontweight="bold", fontsize=13.5, pad=14)
cb = fig.colorbar(im, ax=ax, shrink=0.5, pad=0.02, extend="both")
cb.set_label("% of 2022 volume", fontfamily="Lora")
for lbl in cb.ax.get_yticklabels(): lbl.set_fontfamily("Lora")
ax.tick_params(length=0)

plt.tight_layout()
fig.savefig("tag_heatmap.png", facecolor="papayawhip", bbox_inches="tight")
print("Wrote tag_heatmap.png")
