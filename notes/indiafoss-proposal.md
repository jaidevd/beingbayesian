# IndiaFOSS Proposal — *Being Bayesian*

**Session type:** Talk (30 min) · Main track, or Open Data devroom
**Level:** Beginner–Intermediate

---

## 1. Title

**Primary**

> **Being Bayesian: Stress-Testing India's Loudest Stories with Open Data and FOSS**

**Alternatives**

- Priors, Updated: A Citizen's Guide to Auditing the Headlines with Public Microdata
- What Would You Have to Give Up? Interrogating India's Narratives with Open Data
- The Citizen's Data Audit: Checking the Stories We're Sold with India's Open Microdata

---

## 2. Proposal description

Every day, social media, the news and even the government sell you loud stories
and extreme opinions. Digital transformation experts say that quick commerce is
killing kirana stores. Enthusiastic startup bros say that gig work is liberating
India's poor and uneducated. Captains of industry believe that the only way to
make it in this market is to work 90 hours every week. Influencers disguised as
amateur economists say that welfare measures are making people lazy, and almost
everyone in the world says that AI is going to change everything.

The only thing more exhausting than listening to these stories is trying to
debunk them. The programmer Alberto Brandolini coined the "Bullshit Asymmetry
Principle", which states that the amount of energy needed to refute bullshit is
an order of magnitude bigger than that needed to produce it. Fighting
misinformation and propaganda is not only an incredibly hard, uphill task, it is
practically Sisyphean. No one person can win against the flood of tiny attention
spans, clickbait and virality.

But, in this talk, I'll convince you that being a Sisyphus is not only
liberating, but also incredibly rewarding. Moreover, as FOSS and open-data
enthusiasts, we are uniquely positioned to fight misinformation. India quietly
publishes some of the richest microdata in the world — and the National Sample
Survey, vast as it is, is only a fraction of what's out there. Armed with this
data and a Jupyter notebook, we can dismantle even the loudest stories. It turns
out, for instance, that the dreaded link between free public healthcare and
"wasteful" spending on tobacco comes down to a difference of about two rupees a
month — while the genuine effects of welfare hide in places no headline thinks
to look, like an LPG subsidy quietly turning into a child's tuition.

For two years I have been doing exactly that in my newsletter. This talk is
about the data-driven process of investigating plausible-sounding claims that
may end up being dubious: taking the prior everyone repeats, getting public
evidence, updating your own beliefs and finally publishing not just the results,
but also all the data and code to support reproducibility.

I'll be taking specific examples that have dominated the popular discourse around
technology, the economy and culture — sometimes with a clean answer, and
sometimes with a more uncomfortable one. Asking what a 90-hour week would
actually cost a salaried, white-collar Indian — in sleep, in time with family,
in the unpaid care work that women already shoulder — settles the argument far
better than any motivational LinkedIn post. And once in a while the most honest
finding is that the data refuses to answer at all: our labour surveys have no way
to even define a "gig worker", which should give anyone celebrating their
liberation some pause. But threaded through all the examples is the unglamorous,
reusable part: where this open data actually lives, why it's so painful to use
(it arrives as disconnected tables of cryptic codes that you have to stitch
together and decode before any of it means a thing), how to wrangle it with the
FOSS stack, and how to publish an analysis others can *check* — because a
debunking you can't reproduce is just another opinion.

This is neither a statistics lecture nor a series of hot takes. It's an argument
that good-faith, reproducible, open-data analysis is civic infrastructure — and
exercising it is our civic duty.

---

## 3. Key takeaways

I want people to leave with two things: the **tech** to do this, and a little of
the **knack** for it.

**The tech**

- Where India's open microdata actually lives, and how to work with it — the
  part the tutorials skip. The friction isn't the file format; it's that the
  data arrives as separate household, person and item-level tables full of
  cryptic numeric codes, and getting to a single honest, nationally
  representative number means stitching those tables together, decoding the
  government's code books, and choosing the right unit of analysis.
- A repeatable, FOSS-only workflow for taking a claim apart end to end — and the
  discipline of *showing your work* by publishing the cleaned, denormalized data
  and the code that produced it, so the next person doesn't have to start from
  the raw dump.

**The knack**

- A storytelling framework you can reuse on any dubious claim: surround the
  reader in the **Prior** everyone shares, slip in the **Trigger** you're
  reacting to, apply plain **Skepticism** (a back-of-the-envelope sniff test, no
  data yet), then bring out the **Investigation** — and land on a **Posterior**
  that genuinely shifts your worldview.
- The investigator's temperament: extend the benefit of the doubt before you
  reach for the data (Hanlon's razor), then hold your own analysis to the same
  merciless, beyond-reproach standard you're demanding of theirs — if you're not
  sure of something, don't say it.
- Knowing when to stop: sometimes the most honest — and most powerful — finding
  is that the data simply cannot answer the question.
- Why a p-value never changed anyone's mind: how to carry an insight the last
  mile from analysis to *impression*, by pairing cold, careful numbers with a
  sincere, human story.
