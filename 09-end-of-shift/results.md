# What Salaried India Does After 5 pm and on Weekends: Results

Data: NSO Time Use Survey 2024 (person-day activity logs, 4 am to 4 am). Sections 5 and 6
use the Periodic Labour Force Survey (PLFS) person file for calendar year 2025, with the
2023-24 round for comparison.
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
  cooperative respondents aged 18 and over. n = 49,954 person-days: 43,886 on a normal day
  ("work day") and 6,068 on an "other day" (weekly off, leave, festival, per the
  field instructions; "off day").
- **Each person reports one day**, so weekday and weekend are different people,
  not the same person twice. Calendar weekends are a poor proxy for a day off:
  only 47% of salaried people are off on a Sunday, and 9% on a Saturday.
- **Groups.** There is no occupation field in the TUS, so the salaried are split
  into five groups by industry (NIC-2008 divisions). Every salaried person is in
  exactly one group:

  | Group | Industries | Share of salaried | Graduates | Women |
  |---|---|---|---|---|
  | Manufacturing and construction | NIC 10-33, 41-43 | 26% | 21% | 12% |
  | Trade, transport and hospitality | 45-56 | 21% | 22% | 10% |
  | Knowledge services | IT, media and telecom 58-63, finance and insurance 64-66, professional and scientific 69-75 | 15% | 84% | 23% |
  | Education, health and administration | 84-88 (public administration, education, health and social work), public and private | 23% | 62% | 44% |
  | Other industries | everything else (agriculture, utilities, real estate, support services, other services) | 15% | 25% | 31% |

  Industry is not occupation: a clerk in a factory is in manufacturing, and a
  cashier in a bank is in knowledge services. **Public employment** is a different
  cut, the employer recorded as government, local body or autonomous body, which
  is recorded only for people who did paid work (section 3).

## 1. After 5 pm on a work day

![](assets/what-matters.png)

What separates people who are still working at 5 pm from those who are not, tested
factor by factor (the share of the variation each explains on its own, from a weighted
linear model; the chart shows the three that matter and three that do not):

- **One industry stands out: education.** Schools and colleges (NIC 85) are 11% of
  salaried workers and only 20% [19-22] of them are still working at 5 pm, against 75%
  [74-76] of everyone else. That split alone explains 16% of the variation. Across all
  industries the figure is 20%, with health (59%) and public administration (62%)
  next lowest, and retail (90%) and IT (89%) highest.
- **Employer explains 10%.** 46% [45-47] of public employees are still working at 5 pm,
  against 79% [78-80] in private companies and firms (77% in companies, 81% in
  proprietary or partnership firms).
- **Gender explains 5%.** 49% [48-50] of women against 74% [74-75] of men. Much of
  that is where women work: outside education, women and men in private companies
  are about equally likely to be still working (77% and 80%), though not in
  proprietary firms (70% and 84%) or public employment (40% and 66%).
- **State (4%), rural or urban (2%) and age (2%) matter less.** The state with the
  earliest finish has 14% still working at 5 pm and the latest 89% (30 states with
  300+ people each). Rural workers 61%, urban 74%; those aged 50 and over 59%,
  under 25 77%.
- **Education level, household spending and the day of the week make no real
  difference.** Graduates are 66% and non-graduates 70%; the five household spending
  groups are 68-70%; weekdays, Saturday and Sunday 68-70%. Social group and marital
  status each explain under 1% (ST workers 54%, General 72%).
- **All the factors together explain only 25% of the variation.** The rest comes from
  things the survey does not record, such as the occupation, shift or hours of the
  individual job.

### The spread of finishing times

![](assets/finish-spread.png)

Five o'clock is not a point where people stop; it sits in the middle of a spread of
finishing times (the end of the last paid-work half hour, for people who did paid
work on a normal day):

- **27% have finished by 5 pm and 73% finish later.** Half of all people finish between
  5:00 pm and 7:30 pm, so a quarter finish before 5 and a quarter after 7:30. 15% have
  finished by 4 pm. 40% finish in the hour and a half either side, between 4:30 and
  6:00 pm, and the busiest half hour is 5:30 to 6:00 pm (18% finish then).
- **The spread differs by job.** In education 55% have finished by 4 pm and 78% [76-79]
  by 5 pm. Among public employers outside education, 18% are done by 4 pm, 37% [35-39]
  by 5 pm and 84% by 7 pm. Among private employers outside education, 7% are done by 4
  pm, only 16% [15-17] by 5 pm, 67% by 7 pm, and it is 9 pm before 90% have finished.
- So the 5 pm line splits each group differently: it is nearly the end of the day in
  education, the middle of the exit for public employers, and the start of it in the
  private sector.

### What drives the finish time, outside education

Leaving out education (NIC 85), whose early finish is built into the school day, on the
same 37,892 work-day person-days with paid work (full table: `assets/finish-drivers.csv`).
![](assets/finish-drivers.png)

Share of the variation in finishing time each factor explains (R-squared, weighted):

| Factor | Explains alone | Adds to all the others |
|---|---|---|
| Industry (2-digit NIC) | 8.4% | 3.8% |
| Gender | 4.2% | 2.1% |
| Employer (public, company, proprietary/partnership, other) | 3.7% | 0.7% |
| State | 2.6% | 1.2% |
| Urban or rural | 1.3% | 1.0% |
| Age, caste, marital status, household spending, graduate, day of week | under 1% each | under 0.3% |

- **Industry matters most, but even all factors together explain only 15%.** Most of
  the variation comes from things the survey does not record.
- **Retail, IT and hospitality finish late; health, public administration and agriculture
  early.** Median finish: retail 7:30 pm (92% after 5 pm), restaurants and hotels 7:30
  pm, IT 6:30 pm (92% after 5 pm), against 6:00 pm for health (63% after 5 pm) and public
  administration (66%).
- **Women finish earlier, and the gap is larger once industry is held equal.** Raw: women
  6:00 pm vs men 6:30 pm (64% vs 83% finish after 5 pm; the means differ by 79 minutes).
  With industry, employer, state and the rest held equal, women finish 64 minutes
  earlier, because women are concentrated in the early-finishing jobs.
- **Employer type:** public 5:30 pm, private company 6:00 pm, proprietary or partnership
  7:00 pm. With the rest held equal, public is 30 minutes earlier than other employers.
  Urban workers finish 35 minutes later than rural ones.
- **Older workers finish a little earlier** (50 and over: 26 minutes earlier than under 25,
  held equal).
- **The day starts at the same time, so the finish is the length of the day.** Start and
  finish are almost uncorrelated (0.05); hours of paid work and finish time are
  correlated at 0.64 (hours alone explain 38%).

Someone counts as **still working** at a given time if it falls between their first
and last paid-work half hour of the day, so a lunch or tea break (up to 4 hours) does
not count as having stopped. Counting only half hours with paid work as the main
activity gives 61% at 5 pm; allowing breaks gives 69% (67% to 69% for any limit from 1
to 6 hours).

By time of day, for the five industry groups:

| Share still working at | 5 pm | 6 pm | 7 pm | 9 pm |
|---|---|---|---|---|
| All salaried | 69% [68-69] | 42% [41-43] | 25% [24-26] | 7% |
| Trade, transport and hospitality | 84% [83-85] | 65% | 46% | 11% |
| Knowledge services | 83% [81-84] | 43% | 18% [17-20] | 5% |
| Manufacturing and construction | 78% [76-79] | 45% | 24% | 7% |
| Other industries | 61% [59-63] | 34% | 21% | 7% |
| Education, health and administration | 39% [38-41] | 19% | 12% | 3% |

- The remaining 31% at 5 pm break down as: 27% have finished for the day, 1% did no
  paid work that day and 0.3% start after 5 pm. (Of the 69%, about 7 points are on a
  break at that moment, mostly eating or in self-care.)
- Who the 27% who have finished are: education, health and administration (57% of
  that group are done by 5 pm, and 46% of all finishers), women (46% against 21% of men),
  public employees (52%, against 16-19% in private companies and small firms), rural
  workers (35% against 22% urban) and workers aged 50 and over (36% against 19% under
  25). Their paid day is shorter, not earlier: they start at 9:00 am (middle half 8:00
  to 9:30), while the others start at 9:30 (8:30 to 10:00), and do a median 6 hours of
  paid work against 8. Half of them stopped between 4 and 5 pm. At 5 pm 32% of them
  are commuting and 21% eating or in self-care.
- The median salaried person starts at 9:30 am (middle half 8:30 to 10:00) and their
  last paid-work half hour ends at 6 pm, a span of about 8.5 hours.

| Median start / median finish | Start | Finish | Done by 5 pm |
|---|---|---|---|
| All salaried | 9:30 am | 6:00 pm | 27% |
| Knowledge services | 10:00 am | 6:00 pm | 14% |
| Education, health and administration | 9:00 am | 5:00 pm | 57% |
| Manufacturing and construction | 9:00 am | 6:00 pm | 18% |
| Trade, transport and hospitality | 9:30 am | 7:00 pm | 13% |
| Other industries | 9:00 am | 6:00 pm | 33% |

- So "nobody leaves at 5" is wrong in both directions: most people are still working
  at 5, but by 7 pm more than four fifths of knowledge-services workers are done.
- What pulls the all-salaried average down is education, health and administration.
  Graduates in education (NIC 85, mostly teachers) do 16 minutes of paid work after
  5 pm. Within knowledge services, IT/media is 87% still working at 5 pm (53% at
  6 pm), finance 79% (34%) and professional services 78% (36%). Trade is the late
  group: retail is still 57% at 7 pm and 27% at 8 pm.

### When paid work ends

![](assets/clock-faces.png)

Median end of paid work on a work day (the last half hour of paid work, commuting
excluded), for three groups with schools and colleges left out, because their early
closing would otherwise dominate everything else:

| | Women | Men |
|---|---|---|
| Health and public administration (NIC 84, 86-88) | 5:30 pm | 6:00 pm |
| Knowledge services | 6:00 pm | 6:00 pm |
| Trade, transport and hospitality | 6:30 pm | 7:00 pm |

- Medians sit on a half-hour grid and can fall on a boundary, so read each as "about".
- Women's evening is housework (the rim turns red after 6 to 7 pm) in
  health and public administration and in knowledge services; men's is leisure.
  Commuting is the most common activity in only one half-hour slot for knowledge-services
  men (around 6:30 pm), because people leave work at different times.
- Early in the evening (5 to 8 pm) the most common activity covers only 35-45% of
  people, so the colour there means "the largest group", not "what most people do".

### The second shift

![](assets/evening.png)

| Minutes between 5 pm and midnight | Paid work | Domestic | Care | Leisure/media |
|---|---|---|---|---|
| All salaried women | 48 | 78 [76-80] | 13 | 63 |
| All salaried men | 92 | 10 [10-11] | 11 | 77 |
| Knowledge-services women | 71 | 48 [43-53] | 12 | 76 |
| Knowledge-services men | 85 | 8 [7-9] | 12 | 88 |
| Education, health and administration women | 28 | 91 [88-93] | 16 | 66 |
| Education, health and administration men | 51 | 13 [13-15] | 16 | 97 |

![](assets/total-work.png)

- Counting paid work, housework and care (commuting excluded), a salaried woman works
  9.6 hours on a normal work day and a salaried man 8.6: 65 minutes more [61-70] for
  women. They do 88 minutes less paid work [84-91] and 153 minutes more unpaid work
  [149-157]. After 5 pm the gap is 26 minutes [23-28].
- The same holds in every group: women work 63 minutes a day more in knowledge services
  [47-79], 94 more in manufacturing and construction [84-103], 66 more in trade,
  transport and hospitality [58-75] and 108 more in education, health and
  administration [102-115].
- By half hour, housework peaks at 40% of salaried women in the half hour from 7:30 pm,
  against 4% of men.
- Salaried women do almost eight times the evening domestic work that salaried
  men do (78 against 10 minutes). It is six times in knowledge services and seven in
  education, health and administration.
- Men's evening domestic time rises with household income (7 to 14 minutes, poorest
  to richest group). Women's barely moves (81 to 76). Money buys men into the
  kitchen a little; it does not buy women out of it.
- In all 19 groups we cut (chart below), women do 4 to 12 times the evening
  housework men do. Women's runs from 43 minutes (under 25) to 97 (aged 35 to 49),
  and men's stays at 7 to 14 minutes in every group.

![](assets/evening-splits.png)

- **Social group:** ST salaried workers are less likely to be still working at 5 pm: women
  35% [31-39] against 53% [50-56] for General, men 61% [57-64] against 77% [76-78].
  We have not separated how much of this is industry and sector mix.

## 2. Weekends and days off

![](assets/off-day.png)

- **Who gets the weekend.** 79% of knowledge-services workers are off on Sunday,
  against 47% of all salaried, 66% in education, health and administration, 42% in
  manufacturing and construction and 28% in trade, transport and hospitality.
  Saturday is off for 18% of knowledge-services workers and 6-12% elsewhere. For
  knowledge workers the weekend is real; for trade and transport it mostly is not.
- **What they do with it.** Women's domestic time on an off day is 292 [281-302]
  minutes for all salaried against 71 [67-75] for men. In knowledge services it is
  241 [218-263] against 74 [64-86], and knowledge-services men spend  minutes on
  leisure and media against  for women.
- 13% of knowledge-services workers still do some paid work on an off day, against
  23% in trade, transport and hospitality and 18% of all salaried.
- The gender gap holds in every cut we tried: sector, age, marital status, social
  group, religion and income. It is far larger than any difference between those
  groups.
- The off-day estimates for women in trade, transport and hospitality (n = 110) carry wide intervals.

### Day by day

![](assets/calendar-activity.png)

- Paid work is the activity that takes the most time on every weekday, in all six
  groups. It is longest for men in trade, transport and hospitality (7.6-8.6 hours)
  and shortest for women in health and public administration (5.0-6.6 hours).
- Saturday is a work day in every group. It is nearly a full one in trade, transport
  and hospitality (7.3-7.8 hours for women, 7.4-8.2 for men) and a shorter one in
  knowledge services (5.4-5.8 hours for women, 6.1-6.6 for men).
- Sunday is where the groups split. Women's largest activity is housework in
  health and public administration (3.8-4.3 hours in Q2 and Q3; meals and self-care
  in Q1, paid work in Q4) and housework or meals and self-care in knowledge services
  (4.0-4.6 hours). Men's is leisure and media in knowledge services (4.6-4.7 hours in
  Q2 to Q4), still paid work in health and public administration (4.4-5.3 hours) and
  in trade, transport and hospitality (6.2-7.1 hours).
- Each person reports one day and the survey does not release dates, so a square is
  a different set of people and Q1-Q4 are survey quarters.

## 3. Public versus private

The survey records the employer type on every paid-work activity. We group it as
**public** (Government/local body plus Autonomous), **private corporate**
(limited companies) and **private small** (proprietary plus partnership). 99% of
work-day respondents have a label.

| Work day | 5 pm | 7 pm | Evening paid work (min) | Evening domestic (min) |
|---|---|---|---|---|
| Public women | 26% | 5% | 22 | 94 |
| Private corporate women | 72% | 13% | 66 | 61 |
| Private small women | 67% | 22% | 72 | 69 |
| Public men | 55% | 13% | 53 | 13 |
| Private corporate men | 79% | 25% | 95 | 11 |
| Private small men | 83% | 40% | 113 | 8 |

Public-sector workers are concentrated in education, health and administration,
so we compared public and private workers within the same industry and education
level (NIC 2-digit x graduate cells, weighted to the public worker mix):

| Public minus private | Raw gap | Industry-adjusted gap |
|---|---|---|
| Women, evening paid work (min) | -47 [-50, -43] | -22 [-27, -17] |
| Women, evening domestic (min) | +29 [25, 33] | +14 [9, 20] |
| Women, % still working at 5 pm | -43 pts | -22 pts [-26, -18] |
| Men, evening paid work (min) | -51 [-54, -48] | -26 [-33, -19] |
| Men, evening leisure (min) | +23 [20, 25] | +12 [6, 17] |
| Men, % still working at 7 pm | -20 pts | -9 pts [-13, -6] |

Half the raw gap is industry and education mix, and half is a real public-sector
effect. An early finish buys women a longer domestic shift (+14 minutes) and men
more leisure (+12). Within single industries the gap is clearest in health
(public women 37% still working at 5 pm against 67% in private) and education (public
teachers 9 minutes of evening paid work against 22 for private teachers).

## 4. The household behind the salaried man

![](assets/ideal-worker-day.png)

The TUS covers every member of a household, so salaried men can be linked to their
wives (the head with the spouse of the head, or a married child with the spouse of a
married child, in households with exactly one such pair). That gives 23,997 men, of
whom 21,225 were on a normal work day. Husband and wife always answer for the same
weekday.

| Husband on a work day | Husband | Wife |
|---|---|---|
| Housework, whole day (min) | 15 [14-15] | 349 [346-352] |
| Care, whole day (min) | 24 [23-25] | 80 [78-82] |
| Housework, 5 pm to midnight (min) | 7 [6-7] | 118 [117-120] |
| Paid work, 5 pm to midnight (min) | 85 [84-87] | 10 [9-11] |
| Leisure and media, 5 pm to midnight (min) | 76 [75-77] | 58 [57-59] |

- 76% [76-77] of the wives are on domestic duties only and 14% [13-15] are in regular
  salaried jobs. Among knowledge-services husbands it is 73% [70-75] and 22% [20-24].
- A wife's unpaid work (housework plus care) is about 7 hours a day [7.1-7.2], a
  husband's about 40 minutes [37-39].
- Where the wife is not in paid work (nine in ten couples are this or the next
  case), the two work about the same hours: 8.5 for him [8.4-8.5, nearly all paid] and
  8.0 for her [7.9-8.0, almost all unpaid]. Where she is in a regular salaried job
  she works 10.1 hours [10.0-10.2] against his 8.3 [8.2-8.4].
- The wife does 92% [92-92] of the couple's housework and care. By the husband's
  industry it is 90% [89-90] in education, health and administration, 91% [90-92]
  in knowledge services, 92-93% elsewhere; it is 92% where she is on domestic duties
  only and 86% [85-87] where she is in a regular salaried job.
  Counting housework alone she does 96%. (The intervals are very narrow because they
  use the approximate survey design.)

- Where the wife is also in a regular salaried job (n = 2,817), she still does 209
  [203-215] minutes of housework to his 20 [18-22], and 95 [92-97] minutes of it
  after 5 pm to his 11 [9-13]. Her paid day is 362 minutes, his 462.
- Over the whole day wives report more leisure than husbands (138 against 113
  minutes), because the husband's paid day is longer. After 5 pm it reverses.

## 5. Women's participation (PLFS)

Participation counts people working or looking for work, by principal or subsidiary
status (the official "usual status" measure). The 2023-24 figures reproduce the
published 41.7% for women and 78.8% for men.

| Age 15 and over | 2023-24 | 2025 |
|---|---|---|
| Women in the labour force | 41.7% | 40.0% |
| Men in the labour force | 78.8% | 79.1% |
| Urban women | 28.0% | 27.7% |
| Rural women | 47.6% | 45.9% |
| Women in regular wage work (share of all women) | 6.2% | 6.9% |
| Men in regular wage work (share of all men) | 18.8% | 20.1% |

- The two rounds differ in period and design (July to June against the calendar year,
  first visits only), so a 1.7-point change in women's participation is within what
  the design difference could produce. It is not evidence of a fall.
- Salaried work is where participation is weakest. Of employed women, 21% are in
  regular wage jobs, 18% in casual labour, 36% self-employed and 25% unpaid family
  helpers; for men the unpaid share is 8%.
- Age 25-59: women's participation is 61% if not literate, 52.5% with less than
  secondary schooling, 42% with secondary, 39% with higher secondary and 45% for
  graduates. Men are at 95-98% at every level. It is 60% for rural women and 35% for
  urban women, 50% for married women and 62% for never-married women.
- By age, women's participation is 41% at 25-29 (men 96%) and peaks at 58% at
  35-44.
- Among women aged 15-59 whose main activity is domestic duties, 86% give child
  care and home-making as the reason; 5% give social reasons, 1% no work at a
  convenient location and 1% a lack of training. These are the respondents' own
  stated reasons.

## 6. The ideal worker, in the PLFS

Goyal described a workforce that is "young, talented, skilled, aspirational". We
read that as age 18 to 34 with a graduate or postgraduate degree (84,098 people in
the 2025 file).

| Usual status, % of the group | Men | Women |
|---|---|---|
| Regular wage or salaried | 40.2 | 18.9 |
| Self-employed or unpaid family | 31.4 | 9.6 |
| Casual labour | 2.7 | 0.6 |
| Unemployed | 14.4 | 11.5 |
| Student | 10.1 | 13.2 |
| Domestic duties | 0.2 | 45.1 |
| In the labour force | 88.8 | 40.6 |

- Among those in the labour force, about 16% of men and 28% of women are unemployed.
- Women are 32% of this cohort's regular wage workers (26% of all regular wage workers).

Those in regular wage jobs (23,271 people), against all regular wage workers aged 18 and over:

| | Young graduates | All regular wage workers |
|---|---|---|
| Employer: private company / public / proprietary or partnership | 45% / 22.5% / 26% | 29% / 22.6% / 39% |
| Professionals (share of group) | 42% (women 55%, men 37%) | 19% |
| Median monthly earnings | Rs 22,600 (women 20,000, men 24,500) | Rs 15,000 (women 10,500, men 17,000) |
| Earnings, 25th to 75th percentile | Rs 15,000 to 36,000 | Rs 10,000 to 26,600 |
| No written contract | 40% | 58% |
| No paid leave | 27% | 47% |
| No social security benefit | 30% | 51% |
| Contract, paid leave and social security all present | 51% | 33% |
| Median hours worked in the last 7 days | 48 | 48 |
| Worked 60 or more hours | 7.6% (men 9.6%, women 3.5%) | 14.8% (men 18.1%, women 5.5%) |
| Worked all 7 days | 13% (men 15%, women 8%) | 26% (men 26%, women 24%) |

- The young graduates who fit the description are in the more secure and better-paid
  part of the salaried workforce, and they work shorter weeks than regular wage
  workers as a whole.
- PLFS gives hours for each of the last seven days but not the weekday, so "worked all
  7 days" is the closest available measure of weekend work.

## What it means for the quote

- At 5 pm most salaried Indians are still working, and the median finishing time
  is 6 pm, so a good part of the quote's point stands for private-sector work in
  knowledge services: 88% of men and 87% of women in private corporate jobs there
  are still working at 5 pm. Trade, transport and hospitality stays latest of all
  (46% still working at 7 pm).
- It is not true that nobody leaves at 5. A quarter of salaried people are done
  by then, and education, health and administration are done much earlier (39%
  still working at 5 pm). By employer, only 55% of public men and 26% of public women
  are still working at 5 pm.
- On the weekend, knowledge-services workers do get the day off (79% on Sundays).
  The quote is wrong about that, though not for trade, transport and hospitality
  (28% off on Sundays). The day off is not equally shared: on it, women do about
  four times the domestic work that men do (292 against 71 minutes).
- The evening is not the same for everyone. A salaried man's wife does about 7 hours
  of unpaid work a day (he does about 40 minutes), and even when she also has a
  regular salaried job she does about ten times his housework.
- Women who could take such a job are few: 40% of women are in the labour force and
  7% are in regular wage work, and 45% of young women graduates are out of the labour
  force on domestic duties.
- The young graduates who fit Goyal's description are men about two to one among
  regular wage workers, earn a median Rs 22,600 a month and work a median 48 hours.

## Caveats

- **No occupation field in the TUS.** The groups are industries, so a clerk in a
  factory is in manufacturing and a cashier in a bank is in knowledge services. The
  within-industry check does not control for occupation, seniority, age or
  urban/rural.
- **"Public" is a lower bound.** Public-sector companies recorded as limited
  companies fall into "private corporate".
- **No employer split on off days.** Only 17% of off-day respondents have an
  employer label, and those who do worked 240-390 minutes on their day off. They
  are the people who were not actually off.
- **Sample.** Regular salaried and wage employees aged 18 and over. It includes
  informal salaried workers: the TUS has no contract, social security or firm-size
  field, so no formal-sector cut is reported.
- **Industry groups** partition the NIC-2008 divisions as in the table above; the
  clock and calendar charts show three groups with schools and colleges (NIC 85) left
  out: health and public administration (NIC 84, 86-88), knowledge services, and
  trade, transport and hospitality. Public employment is
  the recorded employer type, not an industry.
- **One day per person.** The weekday and the day-of-week charts compare different
  people, not one person's week.
- **Household pairs** cover households with a single head-spouse or married-child
  pair, and the diaries are one day each.
- **PLFS 2025** has no data layout in the download; the 2023-24 coding was assumed
  (the value distributions match). The weights (multiplier divided by 100) are used
  for shares and medians only, and the two rounds differ in design.
- **Intervals** use a state x sector approximation of the survey's strata. The
  small cells (women's off days in trade, transport and hospitality, ST, care-needing households) are indicative only.

Supporting tables: `assets/splits-ci.csv`, `assets/employer-ci.csv`,
`assets/within-industry.csv`, `assets/spouse-housework.csv` (includes the wife's share),
`assets/plfs-women-participation.csv`, `assets/plfs-ideal-cohort.csv`.
Scripts and how to run them: `scripts/README.md`.
