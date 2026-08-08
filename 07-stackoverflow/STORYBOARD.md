The governing arc is:

I thought AI would punish people who failed to learn how to find answers. Then I discovered that the people asking those embarrassing questions were also feeding a machine that turned private ignorance into public knowledge—and AI has broken that machine.

I. PRIOR — What competent programmers do

1. “In the beginning was the command line.”
Open with Stephenson. Brief history from punch cards → CLI → GUI. Establish your prejudice: fluency with tools matters; competent programmers learn high-ROI skills instead of fumbling around.

2. The intern.
The debugging story. Distinguish reasoning from dexterity. Your irritation isn't that he couldn't solve the problem; it's that he resisted learning the obvious tools for solving it efficiently.

Purpose: make the reader inhabit your worldview. There are competent knowledge workers and people who are vulnerable because they refuse to become competent.

3. Then indict yourself.
Fourteen years earlier, you were hardly different. Bring up the five Stack Overflow questions: deleted ones, embarrassing ones, inability to search properly.

The line:

I was precisely someone who deserved to have their job taken away by AI.

Keep it. It plants a bomb that the rest of the essay detonates.

4. Stack Overflow as part of becoming competent.
Shift from your profile to everybody's experience. Friend encounters previous interns' failed questions and answers from his own boss. SO wasn't merely a website programmers visited; it had become part of the environment in which programmers learned.

Then the contradictions: career-making reputation, extraordinary expertise, gatekeeping, humiliation, toxicity.

End this act with something simple:

For most of my career, getting stuck, searching Stack Overflow, and discovering that somebody else had already been stuck in precisely the same way was simply part of programming.

No power laws yet.

II. TRIGGER — Something disappeared

5. Show the question-volume chart.

Very little prose before it.

Stack Overflow peaks, slowly declines—and then falls off a cliff after 2022.

The obvious explanation arrives immediately:

ChatGPT killed Stack Overflow.

But you don't believe explanations that convenient.

Chart: monthly questions, 2008–2025.

III. SKEPTICISM — Perhaps Stack Overflow killed itself

6. It was already declining.
The peak was around 2014. Maybe the repository was filling up. Maybe people simply had fewer unanswered programming questions.

This immediately kills the strawman version of the story: healthy community suddenly murdered by ChatGPT.

7. And Stack Overflow really was unpleasant.
Now use the newcomer analysis.

Rejection of first questions: ~5% (2010) → ~18% (2017 peak), then easing to ~15% by 2022.
Retention (newcomers who ever return): 58% (2010) → 42% (2022) — all before ChatGPT.
SO recognizes the problem in 2018 and improves somewhat.

(Note: the 18% is the 2017 peak, not the 2022 level — that's exactly what makes the "hostility was already easing when the collapse hit" contradiction land. Keep it tagged as the peak.)

This gives the alternative explanation its strongest possible case.

Perhaps ChatGPT arrived at the scene of a murder already in progress.

But notice the contradiction: hostility had actually begun easing when the catastrophic collapse happened.

Chart: newcomer rejection + retention. Don't drown this section in the yearly regressions.

IV. INVESTIGATION — Start eliminating explanations

8. Old age isn't enough.
Bring in the genuine-question series. Useful, upvoted, non-duplicate questions decline only gently with age — no cliff — until 2022, then break. (Not "flat then cliff": they drift down with the general aging, but the sharp break is unmistakably post-2022.)

Use the age-fair definition — upvoted + never-duplicate. Do NOT use the "referenced-by-others-later" cut: it's an age artifact (recent questions haven't had time to be referenced) that fabricates a false slow decline from 2011.

Then the trend break — and lean the causal claim on the PNAS difference-in-differences result (SO vs Russian/Chinese/Math counterfactuals), not on our within-SO series alone. Our series show a coincident break; PNAS supplies the identification.

The important conclusion is modest:

Stack Overflow was aging. What happened after 2022 was something else.

Chart: genuine questions (age-fair) or actual-vs-pretrend, not both unless necessary.

9. Maybe AI merely removed the rubbish.
Rapid-fire eliminations:

duplicates don't explain it;
genuine questions collapse;
beginners and experienced askers both collapse;
high- and low-reputation contributors both retreat.

Don't give each one a chart. This is an investigative montage.

10. Maybe programming itself moved on.
Now the durable-tag result.

Flutter was booming. Rust was booming. jQuery was dying. They all suffered almost the same fate on Stack Overflow.

Pre-ChatGPT tag growth has essentially no relationship with post-ChatGPT survival.

This is the moment the investigation changes character:

Whatever disappeared was not Java, Rust, PHP or jQuery. It was the habit of asking questions on Stack Overflow.

Chart: durable-tag decoupling. This deserves space.

V. THE BODY — What actually collapsed?

11. The people.
Move from questions to the community producing answers.

Answerers −92%. Editors −99%. Even the 100k+ reputation elite goes from 83% active to 39%.

If you want the power-law material, this is where it belongs. Briefly establish just how enormous and unequal the contributor system was, then show that even its extraordinarily invested core couldn't escape.

Don't linger on Pareto mathematics unless it earns its keep.

12. Then reveal the paradox.
You expected answerers simply to disappear faster than questions.

They don't.

There are actually more active answerers per remaining question.

And yet:

answered questions: 80% → 64%;
answers/question: 1.13 → 0.84;
median first answer: ~70 min → ~4 hours;
per-answerer output: ~2.2 → ~0.9/month.

This is probably the analytical climax.

The community hasn't merely become smaller. It has become shallower.

Chart: feedback.png. Give it room.

VI. MECHANISM — Why shrinking demand destroys supply

13. Why did anyone answer strangers for free?

Now explain the commons.

SO paid contributors in other currencies: mastery, status, autonomy, usefulness, reciprocity, belonging, durable public reputation.

But those motives needed machinery:

questions → opportunities to help → votes/reputation/visibility → reasons to return → answers → reasons to ask.

SO's genius was converting private motivation into persistent public production.

14. Test the mechanism.
Bring in the opportunity-retention result.

Answerers working in busy tags were 2–3× more likely to return than those in thin tags, both before and after GPT.

That relationship predates AI.

Therefore the dependency was already built into the system:

Contributors return when the commons gives them things to contribute to.

GPT doesn't have to destroy people's generosity. It only has to remove the occasions on which that generosity becomes public.

Now give the completed loop:

fewer public questions → fewer opportunities + harder residual questions → lower engagement and retention → poorer matching and slower answers → Stack Overflow becomes less attractive → fewer public questions.

VII. WHY STACK OVERFLOW? — The thing it was best at was the thing AI could eat

15. DeLine and Brooks.

Now zoom out from economics to programming itself.

Brooks: essential versus accidental difficulty.
DeLine: self-contained versus contextual information needs.

Don't claim they're identical. Show how strongly they align.

Stack Overflow was extraordinarily good at questions like:

How do I use this function?
Why does this API throw this error?
What's the idiomatic way to do X?

General, portable, decontextualized knowledge.

Then hit the empirical result:

libraries fall 98%—the steepest category.

The properties that made SO answers valuable—public, reusable, searchable, context-light—also made them excellent training material and excellent candidates for substitution.

The harder questions remain elsewhere:

Why was our system designed this way?
What should it do?
What trade-off did somebody make three years ago?
What does the customer actually want?

Those were never primarily Stack Overflow's product.

VIII. POSTERIOR — The embarrassing question was doing work

16. Return to your old Stack Overflow profile.

This should be the emotional turn.

At the beginning, you looked at those questions and saw evidence of incompetence.

Now look again.

Past-you had a stupid problem. He exposed his ignorance publicly. Somebody helped him. The answer remained behind. Somebody else could find it. Maybe you eventually became competent enough to answer other people's stupid questions.

The embarrassment was part of a knowledge-production process.

ChatGPT can eliminate the embarrassment.

It can also eliminate the public artifact.

17. Bring in the present-day AI anecdote.
Your Copilot example belongs here: fifteen lines produced in seconds. Celebrate it. Don't manufacture nostalgia for tedious work.

The unsettling thing is precisely that it works so well.

Had that problem once sent you to Stack Overflow, your struggle might have produced something reusable. Now the exchange happens privately and disappears.

IX. THE POSTERIOR

The prior was approximately:

Making knowledge easier to access makes us collectively better at producing and using knowledge.

The posterior is:

Making knowledge cheaper to consume can make public knowledge more expensive to produce.

Or, perhaps stronger for the actual essay:

Stack Overflow turned private ignorance into public knowledge. Generative AI turns public knowledge back into private answers.

That's the larger story.

Not “ChatGPT killed a website.” Not even “AI is eating its training data.”

It is about a change in the economics of knowledge production: the individual can become dramatically better off while the commons that made the improvement possible becomes poorer.

Final image

I'd end where you began: with competence.

The intern fumbling through menus seemed obviously vulnerable because he refused to learn a better tool. Using AI is now itself the better tool. Refusing it would be equally foolish.

The disturbing posterior is therefore not that we should go back.

It's that doing the individually rational thing—asking the machine—may slowly destroy something that was collectively valuable.

That's your Johnny Lawrence story. And it is already your own.

---

## Notes

- **Act I is drafted** in `prior.md` (Stephenson opening, the intern, the five-questions self-indictment, SO-as-institution). Beats 1–4 map to it directly.
- **Evidence backing every beat** is catalogued in `FINDINGS.md` (chart → script → data inventory).

## Data-fidelity guardrails (keep these true in the prose)

1. **Causation rests on PNAS, not our series.** Our within-SO analyses show a break *coincident* with ChatGPT; the causal claim leans on del Río-Chanona et al. (PNAS Nexus 2024) and their difference-in-differences against counterfactual platforms. Cite them as corroboration, not a rival.
2. **Genuine questions = age-fair metric only** (upvoted + never-duplicate). The "referenced-later" cut is an age artifact — never use it to argue quality declined.
3. **The feedback-loop paradox (beat 12) is engagement, not headcount.** Answerers did *not* leave faster than questions; headcount fell together (answerers-per-question even rose). What deteriorated is per-answerer output, answer coverage, and speed — "shallower, not just smaller." Don't let an edit flip this into "answerers left faster."
4. **Recent months are censored** on the answering metrics (frac-answered, time-to-first-answer to ~mid-2025) and on retention (12-mo return valid to Dec-2024). Cite settled values, not the final month.
5. **Reputation numbers are dump-date snapshots** — the 83%→39% elite-survival and the Pareto *shape* are robust; avoid cross-time *level* comparisons of median/percentile reputation.
6. **"~1 in 5 newcomers rejected" is the 2017 peak**, and rejection was easing by 2022 — the contradiction the skepticism act needs.
