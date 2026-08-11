import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd

fm.fontManager.addfont("/home/jaidevd/.local/share/fonts/Lora-Bold.ttf")
fm.fontManager.addfont("/home/jaidevd/.local/share/fonts/Lora-Regular.ttf")

r = pd.read_csv("monthly_good_posts.csv", index_col=0, parse_dates=True)

fig, ax = plt.subplots(figsize=(12, 4.5), dpi=300)
fig.patch.set_facecolor("papayawhip")
ax.set_facecolor("papayawhip")

ax.plot(r.index, r["all_questions"] / 1000, color="maroon", lw=1.8,
        label="All questions")
ax.fill_between(r.index, r["all_questions"] / 1000, color="maroon", alpha=0.10)
ax.plot(r.index, r["composite_good"] / 1000, color="teal", lw=1.6,
        label="Genuinely good questions")

# ChatGPT public launch
chatgpt = pd.Timestamp("2022-11-30")
ax.axvline(chatgpt, color="black", lw=1, ls="--")
ax.text(chatgpt - pd.Timedelta(days=40), ax.get_ylim()[1] * 0.96,
        "ChatGPT\nlaunches  ",
        fontfamily="Lora", fontsize=9, color="black", va="top", ha="right")

ax.set_title("Stack Overflow questions per month: all vs. genuinely good",
             fontfamily="Lora", fontweight="bold", fontsize=14)
ax.set_ylabel("Questions created (thousands)", fontfamily="Lora", fontweight="bold")
ax.set_xlabel("")

for lbl in ax.get_xticklabels() + ax.get_yticklabels():
    lbl.set_fontfamily("Lora")

ax.legend(prop=dict(family="Lora"), frameon=False, loc="upper left")
ax.grid(axis="y", color="gray", linewidth=0.3, linestyle="dashed")
ax.spines[["top", "right"]].set_visible(False)
ax.margins(x=0.01)
ax.set_ylim(bottom=0)

plt.tight_layout()
fig.savefig("genuine_vs_all.png", facecolor="papayawhip", bbox_inches="tight")
print("Wrote genuine_vs_all.png")
