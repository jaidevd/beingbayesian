Here’s the rebuilt storyboard around the **actual prior**:

> **ChatGPT did not kill Stack Overflow. At most, it was beating an already dead horse.**

That gives the piece a much cleaner Bayesian arc.

## 1. Opening — The programmer you used to be

Start with the Stephenson quote, the command line, the intern, and your own impatience with avoidable incompetence.

Then turn it on yourself: your old Stack Overflow profile, the embarrassing questions, the better answers, the friend whose boss had answered all the previous interns.

**Purpose:** establish Stack Overflow as part of the lived texture of programming, not yet as an economic institution.

End roughly where your draft currently does:

> Stack Overflow has been, for the better part of the last twenty years, quite central to software engineering.

No analysis yet.

## 1b. The shape of the thing — a tempting intuition

Close the opening on the power-law hook (the new movement at the end of `prior.md`): your own reputation of 3,144 is already the 99.68th percentile, ~100k users sit above you, and the peak is near 1.5 million.

The observation: reputation, like wealth, is a power law — influence concentrated in a vanishing fraction.

Then the seductive line — stated as a **prior**, not a finding:

> It's not hard, then, for LLMs to destroy the astronomically long tail.

Plant it as an intuition to be tested, not a conclusion. §10 returns to it and overturns it.

(Numbers verified against the dump: 1,521,625 max; 99,000 above 3,144; 99.68th percentile. Two honesty notes for the prose — ~84% of all accounts sit at reputation 1, so "a third of a percent above" leans on a mostly-inactive denominator; and 3,144 → 1.5M is ~2.7 orders of magnitude, not quite three. Also decide which "long tail" you mean — users-by-reputation vs. the tail of questions/knowledge — or connect them explicitly, since reputation is *earned by* answering the question tail.)

---

# PRIOR — The horse was already dead

## 2. Stack Overflow had been going downhill forever

Now state your belief explicitly.

Everyone says ChatGPT killed Stack Overflow. You don't buy it.

You remember:

* increasingly hostile moderation;
* questions being closed as duplicates;
* newcomers complaining about being unwelcome;
* Google increasingly surfacing old answers instead of requiring new questions;
* the feeling that most obvious programming questions had already been asked.

Then show the first data.

**Chart: monthly questions, 2008–2025.**

And initially it vindicates you:

> Stack Overflow didn't peak in 2022. It peaked around 2014.

For nearly a decade before ChatGPT, questions were already declining.

This is the moment to say some version of:

> ChatGPT hadn't murdered Stack Overflow. It had shown up at the deathbed and taken credit.

That's the Prior.

---

# TRIGGER — But the curve looks strange

## 3. Look again at 2022

The trigger isn't merely “questions fell.”

It's the **change in slope**.

The decline from 2014–2022 is gentle. After 2022, it becomes catastrophic. 

This should bother you without yet changing your mind.

Perhaps the old decline simply accelerated. Perhaps the remaining corpus finally saturated. Perhaps programming moved elsewhere.

So you investigate.

---

# SKEPTICISM — Give the old-death hypothesis every advantage

## 4. Stack Overflow really did have serious pre-existing problems

This is where the newcomer work belongs.

Tell the hostility story without caricature:

* newcomer rejection rose from ~5% to ~18%;
* retention fell from 58% to ~42% before ChatGPT;
* rejection consistently predicted lower return;
* SO knew there was a problem and tried to correct it after 2018.

This is important because it **strengthens your prior**.

You weren't imagining Stack Overflow's deterioration.

The platform had spent years making participation expensive.

A good line to aim toward:

> If Stack Overflow died, there were plenty of suspects who arrived before Sam Altman did.

---

## 5. The saturation hypothesis

Perhaps Stack Overflow was a victim of its own success.

Twenty million-plus questions later, maybe most reusable programming questions had simply been answered.

This is intuitively strong. SO's whole purpose was to create a permanent archive. A successful archive should eventually reduce the need to add to itself.

Now test it.

---

# INVESTIGATION — The prior starts breaking

## 6. Useful questions weren't disappearing

Bring in the age-fair “genuine questions” analysis.

Upvoted, non-duplicate questions remain surprisingly steady until 2022. 

This is the first serious blow to the prior.

Yes, total volume had been declining.

But the productive core of new knowledge creation hadn't been slowly approaching zero.

> The horse was old. It was not dead.

That sentence could be a major turning point.

---

## 7. Maybe ChatGPT merely removed the rubbish

Test the easiest rescue hypothesis.

Quickly dispatch:

* duplicates;
* low-quality questions;
* novice askers;
* experienced askers.

All collapse.

Do this briskly—probably one paragraph and perhaps a compact figure rather than four separate charts.

The point is not that every group falls by precisely the same amount.

The point is that **the shock refuses to stay confined to the expendable fringe**. 

---

## 8. Maybe the technologies themselves died

Now bring out one of the strongest results.

Rust growing. Flutter booming. jQuery declining. PHP mature.

After ChatGPT, it scarcely matters.

Pre-GPT tag growth has essentially no relationship with post-GPT survival: (r \approx 0.09). 

**Chart: durable-tags decoupling.**

This should be the point at which your original hypothesis becomes genuinely difficult to maintain.

> Stack Overflow wasn't merely losing yesterday's technologies. It was losing questions about tomorrow's technologies too.

Whatever happened was platform-wide.

---

## 9. The causal question

Now you can introduce the PNAS paper.

Don't make it a literature review.

Something like:

> By this point I had independently rediscovered something researchers had already attacked with better causal machinery.

Their quasi-experimental work attributes a substantial initial decline to ChatGPT.

Your analysis then extends the picture through 2025 and shows that the initial shock does not recover—it becomes vastly deeper.

This is where your prior finally breaks:

> I had mistaken a long decline for an explanation of the collapse.

---

# SECOND INVESTIGATION — What exactly died?

## 10. Not just questions: the community

Switch lenses from output to people.

Questions collapse.

So do:

* answerers;
* editors;
* newcomers;
* even the highest-reputation core.

This matters because a searchable archive can survive with fewer new questions.

A **community cannot survive without people returning to maintain and replenish it**.

Introduce reputation concentration here — and **pay off the long-tail hook from §1b**. The tempting intuition ("LLMs destroy the long tail") gets overturned, in a more interesting way than it was posed:

* the power-law **shape is preserved** — α ≈ 1.4, Gini ≈ 0.92, stable before and after ChatGPT;
* the distribution **contracts homothetically** — it shrinks along its own curve;
* even the **head** falls — the 100k+ elite go from 83% to 39% active.

So AI didn't pick off the tail. It shrank the whole commons at once. What it destroyed wasn't the long tail but the **process that generates the entire distribution** — the occasions to contribute that turn into reputation.

**Chart: reputation.png** — the credible pre/post-ChatGPT artifact your prior-draft self-note asked whether existed. It does.

Keep the Pareto mathematics light. The striking fact is enough: even people with enormous accumulated investment in the platform leave. 

---

## 11. The paradox: there are enough answerers—and answers still get worse

This is probably your strongest analytical scene.

At first, the commons mechanism appears not to work:

Questions fall *faster* than answerer headcount.

There are actually more nominally active answerers per 100 questions.

So why doesn't service improve?

Then reveal:

* answered at all: **80% → 64%**;
* answers/question: **1.13 → 0.84**;
* median first answer: **~70 minutes → ~4 hours**;
* output per active answerer: **~2.2 → ~0.9/month**.

The system hasn't merely lost bodies.

It has lost **intensity and matching**.

That distinction is important enough to linger on.

---

## 12. Why questions sustain answerers

Now introduce the retention-by-opportunity result.

Answerers in busy tags are dramatically more likely to return than answerers in thin ones—and this relationship existed before ChatGPT.

This gives you the structural mechanism:

> Questions aren't merely demand for answers. They are opportunities to participate.

That sentence can carry a lot of the next section.

---

# EXPLANATION — Why Stack Overflow was vulnerable

## 13. Why did anyone answer strangers for free?

Now Eghbal/Pink/reputation stop being background reading and become explanation.

SO paid in:

* mastery;
* status;
* usefulness;
* autonomy;
* reciprocity;
* public reputation.

And its machinery transformed those motives into durable production:

**question → answer → votes/reputation → visibility → return → more answers.**

The key discovery:

> ChatGPT didn't need to make people less generous. It needed to make fewer people ask them for help.

Then the empirical loop:

**fewer public questions
→ fewer contribution opportunities + harder residual questions
→ lower engagement and retention
→ poorer coverage and slower answers
→ worse public-Q&A experience
→ fewer public questions.**

Now the simultaneous collapse has an explanation.

---

## 14. Why this platform in particular?

Bring in DeLine + Brooks.

SO specialized in programming knowledge that was unusually:

* general;
* portable;
* context-light;
* reusable;
* publicly expressible.

“How do I use this API?” is almost the canonical Stack Overflow question.

And libraries are the category that collapses hardest. 

That's not proof of the theory by itself, but it fits beautifully.

The qualities that made SO knowledge valuable to millions of programmers also made it ideal material for a model that could answer the same kinds of questions privately.

What remains hardest is increasingly local:

* Why was *this* system designed this way?
* What is it supposed to do?
* What caused this state?
* What trade-off are we willing to make?

Those were never Stack Overflow's strongest product anyway.

---

# POSTERIOR — It was dying. And ChatGPT still killed it.

## 15. Return to the original belief

This needs to be explicit.

You were **not wrong** that Stack Overflow was unhealthy before ChatGPT.

The hostility was real.

The newcomer pipeline was weakening.

Question volume had been falling for years.

The mistake was treating those facts as sufficient to explain what happened next.

Your posterior could be:

> **Stack Overflow was declining before ChatGPT. But decline is not death. Generative AI turned a slow deterioration into the collapse of the system that produced new public knowledge.**

Or, more personally:

> **I had confused evidence that Stack Overflow could die with evidence that it already had.**

That feels particularly Bayesian.

---

## 16. Return to your embarrassing questions

Now revisit younger-you.

At the beginning, his Stack Overflow questions were evidence of incompetence.

By the end, they look slightly different.

He encountered a problem, failed to solve it privately, exposed his ignorance, and created an occasion for another programmer to help.

The exchange was inefficient for him.

But because it happened publicly, **the residue of that inefficiency became useful to everyone else**.

This is where your initial command-line/competence story pays off without requiring you to renounce it.

You can still believe programmers should use better tools.

You can still believe ChatGPT is the better tool.

---

## 17. Final posterior

The larger update is therefore not “AI bad.”

It is a tension between individual and collective efficiency:

> **ChatGPT is often a much better way for a programmer to get an answer. Stack Overflow was a much better way for that act of getting an answer to leave something behind.**

And perhaps the final formulation:

> **Generative AI did not kill Stack Overflow by being worse. It killed Stack Overflow by being better—for the person asking the question.**

That, I think, is where the post should land.

The tragedy—if it is one—is that **the individually rational choice no longer produces the public good as a side effect.**
