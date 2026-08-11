import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd

fm.fontManager.addfont("/home/jaidevd/.local/share/fonts/Lora-Bold.ttf")
fm.fontManager.addfont("/home/jaidevd/.local/share/fonts/Lora-Regular.ttf")

c = pd.read_csv("hostility_cohorts.csv", index_col=0)
censor0 = 2022.5  # beyond here retention (less time) + ignored (answerer collapse) are censored

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5), dpi=300)
fig.patch.set_facecolor("papayawhip")

# Panel 1: the rising cost of a first question
ax1.plot(c.index, c["rejected_rate"] * 100, color="maroon", lw=2, marker="o", ms=3,
         label="actively rejected (closed or downvoted)")
ax1.plot(c.index, c["ignored_rate"] * 100, color="slategray", lw=1.6, ls="--", marker="s", ms=2.5,
         label="ignored / no answer (partly supply-driven)")
ax1.axvline(2018, color="teal", lw=1, ls=":")
ax1.text(2018.1, 46, "SO 'Be Nice'\nreforms (2018)", fontfamily="Lora",
         fontsize=8.5, color="teal", va="top")
ax1.axvspan(censor0, 2025.5, color="gray", alpha=0.12, lw=0)
ax1.annotate("~1 in 5 newcomers rebuffed\nby 2017 — years before ChatGPT",
             xy=(2017, 18.2), xytext=(2008.5, 30), fontfamily="Lora",
             fontsize=9, color="maroon",
             arrowprops=dict(arrowstyle="->", color="maroon", lw=1))
ax1.set_title("The cost of asking a first question rose for a decade",
              fontfamily="Lora", fontweight="bold", fontsize=12.5)
ax1.set_ylabel("% of first-time askers", fontfamily="Lora", fontweight="bold")
ax1.legend(prop=dict(family="Lora", size=8.5), frameon=False, loc="upper left")
ax1.set_ylim(0, 50)

# Panel 2: and it drove newcomers away
ax2.plot(c.index, c["ret_ok"] * 100, color="teal", lw=2, marker="o", ms=3,
         label="first question well-received")
ax2.plot(c.index, c["ret_rejected"] * 100, color="maroon", lw=2, marker="o", ms=3,
         label="first question rejected")
ax2.fill_between(c.index, c["ret_rejected"] * 100, c["ret_ok"] * 100,
                 color="maroon", alpha=0.12)
ax2.axvspan(censor0, 2025.5, color="gray", alpha=0.12, lw=0)
ax2.text(2023.2, 72, "recent cohorts\ncensored", fontfamily="Lora",
         fontsize=8, color="0.4", va="top")
ax2.annotate("newcomer return rate\nfell 58% to 42% before AI",
             xy=(2022, 42), xytext=(2013.5, 30), fontfamily="Lora",
             fontsize=9, color="teal",
             arrowprops=dict(arrowstyle="->", color="teal", lw=1))
ax2.set_title("Rejected newcomers came back less — and fewer came back each year",
              fontfamily="Lora", fontweight="bold", fontsize=12)
ax2.set_ylabel("% who ever posted again", fontfamily="Lora", fontweight="bold")
ax2.legend(prop=dict(family="Lora", size=8.5), frameon=False, loc="lower left")
ax2.set_ylim(0, 100)

for ax in (ax1, ax2):
    ax.set_facecolor("papayawhip")
    ax.grid(axis="y", color="gray", linewidth=0.3, linestyle="dashed")
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_xlim(2008.5, 2025.5)
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_fontfamily("Lora")

plt.tight_layout()
fig.savefig("hostility.png", facecolor="papayawhip", bbox_inches="tight")
print("Wrote hostility.png")
