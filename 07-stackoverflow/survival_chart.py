import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd

fm.fontManager.addfont("/home/jaidevd/.local/share/fonts/Lora-Bold.ttf")
fm.fontManager.addfont("/home/jaidevd/.local/share/fonts/Lora-Regular.ttf")

r = pd.read_csv("survival.csv", index_col=0, parse_dates=True)
chatgpt = pd.Timestamp("2022-11-30")

# low reputation -> high: pale to deep (deep maroon = the trusted core)
COLORS = {"<100": "#cbb897", "100-1k": "darkgoldenrod", "1k-10k": "darkorange",
          "10k-100k": "teal", "100k+": "maroon"}
LABELS = {"<100": "< 100 rep (casual)", "100-1k": "100 – 1k",
          "1k-10k": "1k – 10k", "10k-100k": "10k – 100k (experts)",
          "100k+": "100k+ (elite core)"}

fig, ax = plt.subplots(figsize=(12, 5), dpi=300)
fig.patch.set_facecolor("papayawhip")
ax.set_facecolor("papayawhip")

for tier in ["<100", "100-1k", "1k-10k", "10k-100k", "100k+"]:
    lw = 2.4 if tier == "100k+" else 1.6
    ax.plot(r.index, r[tier] * 100, color=COLORS[tier], lw=lw, label=LABELS[tier])

ax.axvline(chatgpt, color="black", lw=1, ls="--")
ax.text(chatgpt + pd.Timedelta(days=25), 90, "ChatGPT",
        fontfamily="Lora", fontsize=9, color="black", va="top", ha="left")

ax.annotate("trust slows the exodus…\nthe elite core is stickiest",
            xy=(pd.Timestamp("2023-06-01"), 64),
            xytext=(pd.Timestamp("2023-05-01"), 88), fontfamily="Lora",
            fontsize=9.5, color="maroon",
            arrowprops=dict(arrowstyle="->", color="maroon", lw=1))
ax.annotate("…but even the 100k+ core\nfalls from 83% to 39% active",
            xy=(pd.Timestamp("2025-07-01"), 39),
            xytext=(pd.Timestamp("2024-01-01"), 60), fontfamily="Lora",
            fontsize=9.5, color="maroon",
            arrowprops=dict(arrowstyle="->", color="maroon", lw=1))

ax.set_title("Who left? The trusted core held longest — but it's hollowing out too",
             fontfamily="Lora", fontweight="bold", fontsize=13.5)
ax.set_ylabel("% of pre-ChatGPT contributors\nstill active",
              fontfamily="Lora", fontweight="bold")
ax.set_xlabel("")

for lbl in ax.get_xticklabels() + ax.get_yticklabels():
    lbl.set_fontfamily("Lora")

ax.legend(prop=dict(family="Lora", size=8.5), frameon=False, loc="upper right",
          title="Reputation tier (pre-ChatGPT)",
          title_fontproperties=dict(family="Lora", size=9, weight="bold"))
ax.grid(axis="y", color="gray", linewidth=0.3, linestyle="dashed")
ax.spines[["top", "right"]].set_visible(False)
ax.margins(x=0.01)
ax.set_ylim(0, 100)
ax.set_xlim(pd.Timestamp("2021-01-01"), r.index.max())

plt.tight_layout()
fig.savefig("survival.png", facecolor="papayawhip", bbox_inches="tight")
print("Wrote survival.png")
