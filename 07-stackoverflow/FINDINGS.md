# What genAI did to Stack Overflow — findings so far

**One-sentence verdict.** Stack Overflow was already fading gently before ChatGPT, but genAI's arrival triggered a broad, structural collapse — ~90–95% across questions, contributors, and every technology alike — that emptied the commons of even its most expert, most trusted core, far faster and deeper than the old decline could ever explain.

---

## Data & method

- **Source:** the full Stack Overflow XML dump (archive at `/media/jaidevd/motherbox/archive/so/`). Posts converted to `posts_1.parquet` + `posts_2.parquet` — **60.4M posts, 24.2M questions**, July 2008 → December 2025.
- **Supporting tables parsed:** `PostLinks.xml` (duplicates, references), `Users.xml` (30.6M accounts: reputation, signup, last-access), plus the parquet's `OwnerUserId` / `LastEditorUserId` for contributor activity.
- **House chart style:** Lora + `papayawhip` + maroon/teal, one chart+script pair per finding.
- **Framing point:** we distinguish *magnitude* (unambiguous) from *causation* (coincident with genAI, not provable as sole cause — see Caveats).

---

## The three views

### View 1 — Questions
- Monthly questions peaked ~2014, drifted down mildly (~**−7%/yr** saturation), then **collapsed** after ChatGPT to ~4k/month (Dec 2025). *(`monthly_posts.png`, `impact.png`, `saturation.png`)*
- **Interrupted-time-series:** actual volume is **~5–7% of the pre-2022 trend projection — a ~14× shortfall**, ~2.3M "missing" questions. The break opens across the ChatGPT adoption ramp (a diffusion curve, not a single-date jump).
- **Duplicates are not the story:** only 679k questions (~1%) were ever flagged duplicate; removing them barely moves the curve. *(`monthly_posts_nondup.png`)*

### View 2 — Users
- **It's fewer people, not less per person:** posts-per-active-contributor fell only 3.2 → 2.0 → 1.4, while the *headcount* of active contributors fell **−94%**. *(`users.png`)*
- Correcting "contributor" to the real backbone (answerers + editors, not one-time askers):
  - **Answerers −92%**, **editors −99%**, askers −96% (peak → Dec 2025).
- **Readers are unmeasurable here:** signups actually *spiked* to 880k/mo in 2024, but **~99% of those accounts never post and never earn a point** — bot/drive-by, not reader interest. The dump has no visit log.
- **Reputation-tier survival** *(`survival.png`)*: a clean gradient — trust buffers the exodus, but even the **100k+ elite core fell from 83% → 39% active**; experts (10k–100k) lost 76%; casuals (<100) lost 99%. The core is hollowing, only slower.

### View 3 — Tags
- The tag ecosystem churned normally until ~2022, then every category collapsed. *(`tags.png`, `tag_categories.png`)*
- **By category:** languages −96%, frameworks −95%, servers −97%, **libraries −98%** (steepest — the "how do I use this API" questions an LLM answers best).

---

## Hypotheses tested — and what survived

| Hypothesis | Verdict | Evidence |
|---|---|---|
| "ChatGPT killed a healthy site" | ❌ overstated | decline began ~2014 (mild saturation) |
| "No real effect — it was dying anyway / just saturation" | ❌ refuted | actual runs ~14× below the pre-2022 trend |
| "It only killed junk / low-quality questions" | ❌ refuted | genuine (upvoted, non-duplicate) questions fell just as hard |
| "People just ran out of good questions" | ❌ refuted | see the two decoupling tests below |
| "It only killed the easiest questions / most elementary askers" | ❌ refuted | every asker-experience tier fell 91–96%; experts not spared |
| **"A broad, structural exodus coincident with genAI adoption"** | ✅ **supported** | every independent lens agrees (capstone) |

### Key supporting analyses
- **Genuine questions held until 2022** *(`good_v2.png`)*: age-fair "good" = upvoted + never-duplicate. ~36k/mo right up to ChatGPT, then a cliff. ⚠️ The "referenced-multiple-times-later" criterion is **age-censored** (reference rate 13.7% for 2013 questions vs 0.9% for 2024) and manufactures a false "slow death from 2011" — it measures age, not quality. Use the age-fair version.
- **Durable-tag decoupling** *(`durable_tags.png`)* — **the cleanest result:** across 44 durable technologies, the correlation between pre-ChatGPT growth and post-ChatGPT survival is **0.09 ≈ zero**. Flutter (+62%/yr), Dart (+50%), Rust (+29%), Python (+4%) retained ~4.1%; already-dying jQuery/AngularJS/PHP retained ~4.3%. **The collapse is orthogonal to the technology's real-world health** → not saturation, not tech-churn; a platform-level abandonment.
- **Asker-experience test** *(`asker_experience.png`)*: first-timer share of questions is **flat at ~24%**; experienced share rose only 10% → 16%. A broad exodus, not a selective cull of beginners.
- **Reputation as a Pareto distribution** *(`reputation.png`)*: active-user reputation is a stable heavy tail (**α ≈ 1.4, Gini ≈ 0.9**). Inequality was already extreme and rising through the 2010s; ChatGPT did **not** change the *shape* — it amputated the base (active/quarter 350k → 32k), leaving a high-reputation remnant (the 2025 cohort out-ranks even the inflated 2014 cohort). The network collapsed *homothetically* toward its core.

### Capstone
*(`capstone.png`)* — three independent signals (questions asked, active answerers, questions on still-growing tech), indexed to pre-ChatGPT = 100, all **converge and collapse to ~5% together**, ~15× below the "ordinary decline continued" counterfactual.

---

## Caveats & limitations (held honestly)

1. **Causation vs. correlation.** The break is *coincident with and consistent with* genAI adoption. Concurrent confounds — the 2023 moderator strike, Google ranking changes, Stack Overflow layoffs — can't be cleanly partitioned out. The magnitude and breadth are beyond doubt; sole attribution to ChatGPT is not provable from this data.
2. **Readers/lurkers are invisible.** No historical visit log; the only proxy (signups) is bot-contaminated post-2023. Any claim about read-*traffic* needs external data (SimilarWeb / Google Trends).
3. **genAI ⊋ ChatGPT.** GitHub Copilot (preview 2021, GA June 2022) predates ChatGPT, so part of the mild pre-2022 softening may already be genAI; ChatGPT was the phase change, not necessarily the first cause.
4. **Diversion vs. obviation.** We can't distinguish "asked the chatbot instead" from "never hit the problem because the AI wrote it right." Both are genAI effects; the thesis holds either way.
5. **Reputation is a Dec-2025 snapshot**, so cross-time *level* metrics (median/p99) are unreliable; the shape/concentration/survival claims are robust (the snapshot bias works against them).
6. **Tag counts are tag-mentions** (a multi-tag question counts once per tag); trends are robust to this. Some pre-GPT tag declines (jQuery, Objective-C) are legitimate churn, so per-tag drops mix churn + genAI — which is exactly why the *decoupling* test (correlation ≈ 0) is the clean argument.

---

## Reading frame
- **Nadia Eghbal, *Working in Public*** — casual vs. active contributors; the commons runs on "the desire to participate rather than money"; coordination cost vs. benefit. Our view 2 is the empirical answer to her question *"what has AI done to the desire to participate?"*
- **César Hidalgo, *Why Information Grows*** — knowledge networks, trust as the glue that lowers the cost of links. The reputation analysis answers *"does trust = repetition?"* — yes, and the trusted core is the last (but not immune) to leave.
- **Robert DeLine, *Code Talkers*** — programmers' information needs; "how do I use this function" (ChatGPT's sweet spot) vs. "why was this code written this way" (needs colleagues) — predicts libraries falling hardest.
- Notes in `research-notes/`.

---

## Chart & file inventory

| Finding | Chart | Script | Data |
|---|---|---|---|
| Monthly questions | `monthly_posts.png` | `monthly_posts_chart.py` | `monthly_posts.csv` |
| Non-duplicate overlay | `monthly_posts_nondup.png` | `monthly_posts_nondup_chart.py` | `monthly_posts_nondup.csv` |
| Questions vs trend (impact) | `impact.png` | `impact_chart.py` | `counterfactual.csv` |
| Saturation test (frozen genuine) | `saturation.png` | `saturation_chart.py` | `monthly_frozen.csv` |
| Genuine vs all | `genuine_vs_all.png` | `genuine_vs_all_chart.py` | `monthly_good_posts.csv` |
| "Good" definition + age artifact | `good_v2.png` | `good_v2_chart.py` | `monthly_good_v2.csv` |
| Users (contributors vs signups) | `users.png` | `users_chart.py` | `monthly_active_users.csv`, `monthly_signups.csv`, `monthly_editors.csv` |
| Reputation-tier survival | `survival.png` | `survival_chart.py` | `survival.csv` |
| Asker experience | `asker_experience.png` | `asker_chart.py` | `asker_experience.csv` |
| Reputation Pareto | `reputation.png` | `reputation_chart.py` | `reputation_pareto_stats.csv`, `reputation_ccdf.npz` |
| Tags over time | `tags.png` | `tags_chart.py` | `tag_month_counts.parquet` |
| Tag categories | `tag_categories.png` | `tag_categories_chart.py` | `tag_categories.csv` |
| Durable-tag decoupling | `durable_tags.png` | `durable_tags_chart.py` | `durable_tags.csv` |
| **Capstone** | `capstone.png` | `capstone_chart.py` | — |
