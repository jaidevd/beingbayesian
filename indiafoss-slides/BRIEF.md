# Brief: "Being Bayesian" — IndiaFOSS 2026 talk deck

Handoff notes for whoever picks up work on this deck next. Read this before
touching `index.html` — it'll save you from re-deriving decisions that were
already made deliberately, and from re-inventing facts that were already
verified against source.

## What this is

A 30-minute reveal.js slide deck (`index.html` + `style.css` + `assets/`) for
a talk proposed to IndiaFOSS 2026, based on the proposal at
`../notes/indiafoss-proposal.md`. The talk argues that FOSS/open-data people
are uniquely positioned to stress-test loud public claims using India's own
open microdata (NSS/HCES/PLFS/TUS), and walks through four such claims as
worked examples, each run through a five-step process: **Prior → Trigger →
Skepticism → Investigation → Posterior**.

Session type: Talk, 30 min. Level: Beginner–Intermediate. Speaker: Jaidev
Deshpande, author of the newsletter this is all drawn from
(beingbayesian.in).

Current state: tag `draft-0` on branch `jd-indiafoss-slides` is the first
complete draft (40 slides); the branch head as of this brief is a
restructured second pass (43 slides) after the first editorial review
(`../review.md`). Treat everything here as live and likely to keep changing.

## Run it

```
cd indiafoss-slides && npx live-server --port=8791 --no-browser .
```

Reveal.js reads slides in document order; navigate with arrow keys, `S` for
speaker view (every slide has real speaker notes in `<aside class="notes">`
— several slides are intentionally sparse on-screen because the explanation
lives there instead).

## The four case studies (the spine of the talk)

1. **Kirana stores** (`01-kirana-stores/`) — "quick commerce is killing
   kirana stores" → only ~7% of households shop online at all; e-commerce's
   real rival is infrastructure and caste/income inequality, not an app.
2. **Gig economy** (`02-gig-economy/`) — "gig work liberates the poor and
   uneducated" → PLFS has no "gig worker" category; the claim can't even be
   checked against a defined population.
3. **90-hour week** (`03-90-hr-workweek/`) — captains-of-industry claims →
   women already do 4x the unpaid domestic work, so the same "ask" costs men
   and women completely different things.
4. **Public welfare / moral hazard** (`06-public-welfare/`) — "free
   healthcare breeds vice spending" → the real gap is ~₹2/month (a rounding
   error); the genuine welfare effect was hiding in an unrelated LPG subsidy
   quietly funding private tuition.

Deliberately **excluded**: `04-stray-dogs` (raw data, zero analysis) and
`05-ai-hype` (argument-driven, no primary dataset) — confirmed via explicit
audit, not an oversight. `07-stackoverflow` is referenced once (a
self-caught methodological near-miss, parallel to the welfare essay's "git
history" story) but is not a case study — it's not India microdata, which is
this talk's whole thesis.

## Deck structure (current order)

Title → 3-question audience quiz (Prior round, one question per slide) →
Brandolini's law → FOSS/Sisyphus framing → the 5-step process (annotated
with a worked kirana example, not abstract labels) → Case 1 → Case 2 →
quiz Update round → Case 3 → Case 4 → the welfare essay's real git history
("Giving up" commit, etc.) → a Stack Overflow near-miss callback →
synthesis table → quiz reveal (placeholder) → **data sources block**
(real HCES file/section structure, real NSS sampling design, unit-of-
analysis traps, the survey-weight gotcha, a practical checklist) → bonus
data-literacy detour (bad-data/knowledge/interpretation taxonomy, a
collider-bias demo) → "the knack" (temperament, Hanlon's razor, a Rosling
quote) → an honest on-stage confession about a gap in a published essay →
"numbers alone don't move anyone" (the last-mile device) → closing.

## Design system

- Reveal.js 5, warm papayawhip/maroon/teal/darkgoldenrod palette, Lora
  (display) + IBM Plex Sans/Mono (system/data) — the same house style as
  every chart in the newsletter's essays (see the `beingbayesian-chart-style`
  memory: matplotlib with `Agg` backend, papayawhip bg, maroon/teal/
  darkorange/seagreen/darkgoldenrod palette, hidden top/right spines, dashed
  gridlines, `Lora` lacks the `→` glyph — use "to" not "→" in chart text).
- Reusable slide components already built into `index.html`'s inline
  `<style>`: `.claim-card` (a quoted loud claim), `.gut-check` (the
  Skepticism beat), `.posterior-line`/`.posterior-note` (the payoff),
  `.code-block` (real code/terminal output, dark-on-warm), `.timeline` (the
  git-log reveal), `.qr-placeholder`/`.quiz-*` (the live-poll slides).
- Every chart image in `assets/` is either reused directly from the essays'
  own output or **regenerated from the essays' raw source data** in-house
  style when no saved image existed (`02-education-income-gender.png`,
  `collider-bias.png`) — never a generic stock chart.

## Editorial rules that got established the hard way

- **Verify before writing.** Every number, code snippet, and structural
  claim in this deck was checked against actual source — notebooks, git
  history, HCES's own methodology PDF — not asserted from general knowledge.
  When the "household file / person file / item file" model turned out to
  be an invented simplification (no such files exist), it got replaced with
  the real structure, sourced from `~/src/hces-2023-24` and its methodology
  PDF. Don't reintroduce plausible-sounding-but-unverified structure.
- **The audience is smart.** Don't over-explain acronyms or condescend
  ("alphabet soup" framing was explicitly removed for this reason).
- **Slides are not notes.** Explanatory prose, connective reasoning, and
  "why this matters" belong in `<aside class="notes">`, not on-screen. A
  slide should carry a title, a number/quote/chart, and little else.
- **This deck is not shy about self-criticism.** It includes a live
  confession about a gap in a published essay and the unfiltered git
  history of a essay's failed first attempt, on purpose — that honesty is
  load-bearing for the talk's argument, not incidental color. Don't sand it
  down without a good reason.
- **"Being Bayesian" is a metaphor, not a technical claim.** Asked directly,
  the honest answer is that nothing here computes an actual posterior
  distribution or applies Bayes' theorem — the name describes a discipline
  (state your prior, get real evidence, actually let it move you, publish
  the update) borrowed from a real colloquial tradition (Julia Galef, Tetlock
  superforecasters), not a statistical method. If asked to justify the name
  technically, don't overclaim.

## Open items

1. **Quiz claim 3 is unresolved.** Two of three live-poll questions are
   final (online groceries; health insurance & vice). The third — a
   tax/middle-class/welfare-burden claim — is explicitly marked `CLAIM TBD`
   in a dashed placeholder on two slides. It needs a real, checkable claim
   with real HCES/PLFS numbers behind it before this deck is presentation-
   ready. Do not invent one; if you're asked to fill this in, research it
   the same way every other claim in this deck was researched.
2. **QR codes are placeholders.** The live audience exercise needs two real
   Google Forms (Prior round, Update round — same 3 questions, binned
   multiple-choice, no login, anonymous, one form per round rather than an
   edit-link) built and their QR codes/links dropped into the
   `[QR pending]` slots.
3. **The results-reveal slide is an empty dashed box.** Once both forms
   have responses, pull them into a sheet, compute the same weighted-
   comparison the rest of the talk argues for, and render a real chart in
   house style (matplotlib, papayawhip/maroon/teal) into that slide.
4. **This is a working draft, not a final cut.** Expect more review passes.

## Key source material (where facts came from)

- `../notes/indiafoss-proposal.md` — the original CFP text this deck is
  built to deliver on; re-check new content against it before assuming
  something is out of scope.
- Essay directories `01-kirana-stores/`, `02-gig-economy/`, `03-90-hr-
  workweek/`, `06-public-welfare/` — published essays plus their notebooks,
  markdown notes, and (for 06) full git history. A lot of the deck's
  sharpest material is stuff that got cut from the published essays but is
  still sitting in the notebooks/git log.
- `~/src/hces-2023-24/` — the actual raw HCES 2023-24 microdata repo
  (section-wise parquet files, `schema.yaml`/`schema.json`, `README.md`).
- `~/src/hces_2023/01_docs/` — official HCES handbook PDFs, including
  `Survey methodology and Estimation Procedure.pdf` (the real sampling
  design: FSU/SSU, stratification, wealth-tier oversampling, panels).
- `~/src/beingbayesian/plfs/*.map.yaml` — PLFS's own column-mapping schema,
  which independently confirms the same FSU/stratum/sub-stratum sampling
  language HCES uses.
- `../../blog/content/posts/bayesian-storytelling.md` — the original essay
  (dated the day after the newsletter launched) that first defined the
  Prior/Trigger/Skepticism/Investigation/Posterior framework. Richer than
  what's in the deck; worth rereading if extending "the knack" section.
- An earlier Gramener talk, "Spotting Bad Analytics" (same author) — mined
  for the three-question skepticism checklist, the Hans Rosling quote, and
  the collider-bias demo (regenerated in house style, not reused as-is).

## Contact points if something seems off

If a slide references a number you can't find in the essay it cites, or a
"real" detail (a file name, a sampling term, a git commit hash) that doesn't
check out against the sources above — flag it rather than smoothing it over.
Every such detail in this deck was put there because it was verified once;
if it's since drifted, that's a bug worth catching, not a style choice to
preserve.
