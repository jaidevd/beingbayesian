import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd

fm.fontManager.addfont("/home/jaidevd/.local/share/fonts/Lora-Bold.ttf")
fm.fontManager.addfont("/home/jaidevd/.local/share/fonts/Lora-Regular.ttf")

g = pd.read_csv("monthly_frozen.csv", index_col=0, parse_dates=True)
cf = pd.read_csv("frozen_saturation_trend.csv", index_col=0, parse_dates=True)["trend"]
ramp0, ramp1 = pd.Timestamp("2022-11-01"), pd.Timestamp("2024-06-01")

fig, ax = plt.subplots(figsize=(12, 4.5), dpi=300)
fig.patch.set_facecolor("papayawhip")
ax.set_facecolor("papayawhip")

# ChatGPT adoption ramp (not a single date)
ax.axvspan(ramp0, ramp1, color="gray", alpha=0.13, lw=0)
ax.text(ramp0, 104, " ChatGPT adoption\n ramp (3.5, 4, ...)",
        fontfamily="Lora", fontsize=8.5, color="0.35", va="top", ha="left")

ax.plot(g.index, g["genuine_fast"] / 1000, color="maroon", lw=1.7,
        label="Genuine questions (accepted ≤90 days, frozen)")
fit = cf[cf.index >= "2014-01-01"]
ax.plot(fit.index, fit / 1000, color="teal", lw=1.5, ls="--",
        label="Smooth 'running-out-of-questions' trend (−7%/yr, 2014–21)")
post = g["genuine_fast"][g.index >= ramp0] / 1000
ax.fill_between(post.index, post, cf[cf.index >= ramp0] / 1000,
                color="teal", alpha=0.15)

ax.annotate("genuine questions fall ~14x\nbelow the saturation trend",
            xy=(pd.Timestamp("2024-10-01"), 9),
            xytext=(pd.Timestamp("2018-09-01"), 30),
            fontfamily="Lora", fontsize=9.5, color="teal",
            arrowprops=dict(arrowstyle="->", color="teal", lw=1))

ax.set_title("Even genuine questions collapse far below the saturation trend",
             fontfamily="Lora", fontweight="bold", fontsize=13)
ax.set_ylabel("Genuine questions / month (000s)",
              fontfamily="Lora", fontweight="bold")
ax.set_xlabel("")

for lbl in ax.get_xticklabels() + ax.get_yticklabels():
    lbl.set_fontfamily("Lora")

ax.legend(prop=dict(family="Lora", size=8.5), frameon=False, loc="lower left")
ax.grid(axis="y", color="gray", linewidth=0.3, linestyle="dashed")
ax.spines[["top", "right"]].set_visible(False)
ax.margins(x=0.01)
ax.set_ylim(0, 112)
ax.set_xlim(pd.Timestamp("2013-06-01"), g.index.max())

plt.tight_layout()
fig.savefig("saturation.png", facecolor="papayawhip", bbox_inches="tight")
print("Wrote saturation.png")
