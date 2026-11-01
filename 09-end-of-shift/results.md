# What Salaried India Does After 5 pm and on Weekends: Results

Data: NSO Time Use Survey 2024 (person-day activity logs, 4 am to 4 am).
All estimates are weighted (`mult`, ratio of weighted sums, as in 03-90-hr-workweek).
Intervals are 95% cluster bootstraps over FSUs, resampled within state x sector
strata (300 draws). The strata are an approximation of the real design.

## The claim

> "Nobody in India will tell you it's 5 o'clock. And certainly, no Indian will
> ever remind you it's the weekend."

Two things are wrong with this before looking at any data. It says "Indians" but
describes a minority: only a small share of Indian workers are salaried, and for
everyone else there is no 5 o'clock to announce. And it assumes the day ends when
paid work does, which for most women it does not. The survey can also simply
test it.

## Who is in the sample

- **Salaried:** usual principal status "regular salaried / wage employee",
  cooperative respondents only. n = 50,235 person-days: 44,147 on a normal day
  ("work day") and 6,088 on an "other day" (weekly off, leave, festival, per the
  field instructions; "off day").
- **Each person reports one day**, so weekday and weekend are different people,
  not the same person twice. Calendar weekends are a poor proxy for a day off:
  only 47% of salaried people are off on a Sunday, and 9% on a Saturday.
- **Knowledge workers.** There is no occupation field, only NIC-2008 industry,
  education and usual status, so the cohorts are built from industry x education:
  - **KW core:** IT/media/telecom (NIC 58-63), finance (64-66) and professional
    services (69-75), graduates and above.
  - **KW broad:** KW core plus public administration, education and health
    (84-86), graduates only.
  - **Contrast groups:** blue-collar (manufacturing, construction, trade,
    transport) and non-graduates. Where useful, the white-collar NIC list from
    03-90-hr-workweek (age 15-60) is shown as a fourth cohort.

## 1. After 5 pm on a work day

![](assets/still-working.png)

| Share still in paid work at | 5 pm | 6 pm | 7 pm | 9 pm |
|---|---|---|---|---|
| All salaried | 61% [61-62] | 38% | 24% | 6% |
| KW core | 77% [75-79] | 42% | 17% [15-19] | 3% |
| KW broad | 53% [52-55] | 28% | 13% [12-14] | 3% |
| Blue-collar | 72% | 49% | 32% | 7% |

- The median salaried person's last paid-work slot ends at 6 pm (6:30 pm for
  blue-collar). Only 13% of KW core are done by 5 pm, against 27% of all salaried.
- So "nobody leaves at 5" is wrong in the other direction too: most people are
  still working at 5, but by 7 pm three quarters of KW core are done.
- KW broad looks early only because of education. Graduates in education
  (NIC 85, mostly teachers) do 16 minutes of paid work after 5 pm. IT/media, finance and professional services
  are still at 74-78% at 6 pm. Retail is still at 51% at 8 pm.

### The second shift

![](assets/evening.png)

| Minutes between 5 pm and midnight | Paid work | Domestic | Care | Leisure/media |
|---|---|---|---|---|
| All salaried women | 48 | 78 [76-80] | 12 | 63 |
| All salaried men | 93 | 10 [10-11] | 11 | 77 |
| KW core women | 75 | 45 [39-50] | 12 | 76 |
| KW core men | 86 | 8 [7-9] | 13 | 88 |

- Salaried women do almost eight times the evening domestic work that salaried
  men do. Even among KW core the ratio is more than five.
- Married KW core women do 67 minutes of domestic work and 24 of care in the
  evening, against 6 and 19 for married KW core men.
- Men's evening domestic time rises with household income (7 to 14 minutes, poorest
  to richest group). Women's barely moves (81 to 76). Money buys men into the
  kitchen a little; it does not buy women out of it.
- **Social group:** in KW broad, ST salaried workers are far less likely to be at
  work at 5 pm: women 26% [19-34] against 46% [42-50] for General, men 41% [34-47]
  against 61% [59-63]. Part of this is industry mix.

## 2. Weekends and days off

![](assets/off-day.png)

- **Who gets the weekend.** 83% of KW core respondents are off on Sunday, against
  47% of all salaried and 37% of blue-collar. Among KW core off days, 62% fall on
  a Sunday and 18% on a Saturday. For these workers the weekend is real.
- **What they do with it.** Women's domestic time on an off day is 291 [282-301]
  minutes for all salaried against 71 [67-76] for men. In KW core, 229 [202-254]
  against 75 [63-87]. KW core men spend 295 minutes [279-310] on leisure and media
  (TV alone is about two and a half hours), against 211 [190-232] for women.
- 13-15% of KW core and KW broad people still do some paid work on an off day,
  against 20% of blue-collar.
- The gender gap holds in every cut we tried: sector, age, marital status, social
  group, religion and income. It is far larger than any difference between those
  groups.
- The off-day estimates for KW core women (n = 230) carry wide intervals.

## 3. Public versus private

The survey records the employer type on every paid-work activity. We group it as
**public** (Government/local body plus Autonomous), **private corporate**
(limited companies) and **private small** (proprietary plus partnership). 99% of
work-day respondents have a label.

| Work day | 5 pm | 7 pm | Evening paid work (min) | Evening domestic (min) |
|---|---|---|---|---|
| Public women | 24% | 4% | 22 | 94 |
| Private corporate women | 66% | 13% | 66 | 61 |
| Private small women | 61% | 20% | 72 | 69 |
| Public men | 51% | 12% | 53 | 13 |
| Private corporate men | 71% | 24% | 95 | 11 |
| Private small men | 73% | 38% | 113 | 8 |

Public-sector workers are concentrated in education, health and administration,
so we compared public and private workers within the same industry and education
level (NIC 2-digit x graduate cells, weighted to the public worker mix):

| Public minus private | Raw gap | Industry-adjusted gap |
|---|---|---|
| Women, evening paid work (min) | -47 [-50, -43] | -21 [-26, -17] |
| Women, evening domestic (min) | +29 [25, 33] | +14 [8, 19] |
| Women, % at work at 5 pm | -40 pts | -20 pts [-24, -16] |
| Men, evening paid work (min) | -52 [-54, -48] | -26 [-32, -19] |
| Men, evening leisure (min) | +23 [20, 25] | +12 [7, 16] |
| Men, % at work at 7 pm | -20 pts | -9 pts [-12, -5] |

Half the raw gap is industry and education mix, and half is a real public-sector
effect. An early finish buys women a longer domestic shift (+14 minutes) and men
more leisure (+12). Within single industries the gap is clearest in health
(public women 36% at work at 5 pm against 62% in private) and education (public
teachers 9 minutes of evening paid work against 22 for private teachers).

## What it means for the quote

- At 5 pm most salaried Indians are still working, and the median finishing time
  is 6 pm, so a good part of the quote's point stands for private-sector white
  collar work: in KW core, 79% of men and 80% of women in private corporate jobs
  are still at work at 5 pm.
- It is not true that nobody leaves at 5. A quarter of salaried people are done
  by then, and public-sector workers are done much earlier: only 51% of public
  men and 24% of public women are still working at 5 pm.
- On the weekend, white-collar workers do get the day off (83% on Sundays). The
  quote is wrong about that. The day off is not equally shared, though: on it,
  women do about four times the domestic work that men do.

## Caveats

- **No occupation field.** Knowledge worker is inferred from industry and
  education, so a graduate cashier in a bank counts. The within-industry check
  does not control for occupation, seniority, age or urban/rural.
- **"Public" is a lower bound.** Public-sector companies recorded as limited
  companies fall into "private corporate".
- **No employer split on off days.** Only 17% of off-day respondents have an
  employer label, and those who do worked 240-390 minutes on their day off. They
  are the people who were not actually off.
- **Intervals** use a state x sector approximation of the survey's strata. The
  small cells (KW core women, ST, care-needing households) are indicative only.

Supporting tables: `assets/splits-ci.csv`, `assets/employer-ci.csv`,
`assets/within-industry.csv`.
