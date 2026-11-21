# Is It 5 O'Clock Yet? What the Time Use Survey Says About Piyush Goyal's Claim: Results

Data: NSO Time Use Survey (TUS) 2024, person-day activity logs from 4 am to 4 am. Sections 4
and 6 also use the Periodic Labour Force Survey (PLFS) person file for calendar year 2025, with
the 2023-24 round for comparison; section 5 uses the Household Consumption Expenditure Survey
(HCES) 2023-24 for washing machines. All estimates are weighted (`mult`, ratio of weighted sums).
Intervals are 95% cluster bootstraps over FSUs, resampled within state x sector strata
(300 draws); the strata are an approximation of the real design.

## The claim, and what it needs to be true

> "Nobody in India will tell you it's 5 o'clock. And certainly, no Indian will
> ever remind you it's the weekend."

The quote makes three testable statements and leaves one thing out:

1. **The day does not stop at 5.** Do salaried people keep working past 5 pm?
2. **The weekend does not exist.** Do they work on their days off?
3. **"Indians" are young, skilled and willing to work hard.** Who is that, and how many
   people can be that?
4. **What the quote leaves out:** what happens at home while someone is available at 5 pm.

## The answer in short

- **The fulcrum: the quote describes a worker who has someone else covering the rest, and
  that cannot hold if more women are to join the workforce.** A salaried man's wife does
  about seven hours of unpaid work a day and he does about forty minutes. When the wife also
  has a salaried job she still does the evening shift, working 10.1 hours a day to his 8.3.
  Salaried women work 65 minutes a day more than salaried men once housework is counted.
  The unpaid work has to go somewhere when more women take jobs; today it stays with them.
- **The person who fits the description is mostly a man.** Among young graduates, 40% of
  men and 19% of women are in regular wage work, and 45% of young women graduates are out of
  the labour force on domestic duties.
- **At 5 pm most salaried people are still working (69%), but 5 pm is where the exit
  begins.** The median day ends at 6 pm, and a quarter of people are done before 5.
- **When you stop depends on where you work, not on being Indian.** Outside schools and
  colleges, retail and hospitality finish at 7:30 pm and health and public administration at
  6:00 pm. Employer and gender matter too, and all the factors together explain only 15% of
  who finishes when.
- **The weekend is real for some and not for others.** 79% of knowledge-services workers
  are off on Sunday, against 28% in trade, transport and hospitality.

The sections below build to the fulcrum: the claim in the evening (2 and 3) and at the
weekend (4), the household behind it (5), who can be the ideal worker (6).

## 1. Who is "nobody": the sample

- **Salaried:** usual principal status "regular salaried or wage employee", cooperative
  respondents aged 18 and over. n = 49,954 person-days, 43,886 on a normal day ("work day")
  and 6,068 on an "other day" (weekly off, leave, festival, per the field instructions;
  "off day").
- **They are a minority.** In the PLFS, 20.1% of men and 6.9% of women aged 15 and over are
  in regular wage work. For everyone else there is no 5 o'clock to announce.
- **Each person reports one day**, so weekday and weekend are different people, not the same
  person twice.
- **There is no occupation field in the TUS.** Where we compare types of work we use the
  industry (NIC-2008 divisions): trade, transport and hospitality (NIC 45-56), knowledge
  services (IT, media and telecom 58-63, finance and insurance 64-66, professional and
  scientific 69-75), health and public administration (NIC 84, 86-88), education (NIC 85).
  Industry is not occupation: a clerk in a factory is in manufacturing. Public employment is
  the recorded employer type (government, local body or autonomous body), not an industry.

## 2. At 5 pm: most are still working, but this is where the exit starts

![](assets/finish-spread.png)

Someone is **still working** at a given time if it falls between their first and last
paid-work half hour of the day, so a lunch or tea break (up to 4 hours) does not count as
having stopped. Counting only half hours with paid work gives 61% at 5 pm; allowing breaks
gives 69% (67% to 69% for any break limit from 1 to 6 hours).

- **69% [68-69] are still working at 5 pm. 27% have finished** and 1% did no paid work that
  day. The share still working is 42% at 6 pm, 25% at 7 pm and 7% at 9 pm.
- **The median salaried person starts at 9:30 am and stops at 6:00 pm**, a span of about
  8.5 hours. Half of all people finish between 5:00 and 7:30 pm, and the busiest half hour
  is 5:30 to 6:00 pm (18% finish then).
- **So the quote is half right.** Most people are working at 5, but the day ends within an
  hour or two of it for most, and it is an ordinary length (about 8.5 hours).
- **The 5 pm line cuts each group differently.** In education 78% [76-79] have finished by
  5 pm. Among public employers outside education it is 37% [35-39], and among private
  employers outside education only 16% [15-17], with 67% done by 7 pm and 90% by 9 pm.
- **Education is the exception that drags the average.** Schools and colleges (11% of
  salaried workers) close early: 20% [19-22] of them are still working at 5 pm, against 75%
  [74-76] of everyone else. We leave them out of the next comparisons, because the school day
  would otherwise dominate everything else.

## 3. When you stop depends on where you work, and what the evening holds

![](assets/clock-faces.png)

Median end of paid work on a work day (the last half hour of paid work, commuting excluded),
with schools and colleges left out. Each clock shows the most common activity in every half
hour from noon to midnight, and the hand points to when paid work ends:

| | Women | Men |
|---|---|---|
| Health and public administration (NIC 84, 86-88) | 5:30 pm | 6:00 pm |
| Knowledge services | 6:00 pm | 6:00 pm |
| Trade, transport and hospitality | 6:30 pm | 7:00 pm |

- **The hand moves later from health and public administration to trade, for both genders.**
- **What fills the evening differs by gender.** For women the rim turns to housework (red)
  after about 6 to 7 pm in health and public administration and in knowledge services; for
  men it is leisure. Early in the evening (5 to 8 pm) the most common activity covers only
  35-45% of people, so the colour there means "the largest group", not "what most people
  do".
- Medians sit on a half-hour grid and can fall on a boundary, so read each as "about".

Which factors predict the finishing time? Outside education (37,892 work-day person-days
with paid work), the share of the variation that each factor explains (R-squared of weighted
models; it is not causation; full table in `assets/finish-drivers.csv`):

| Factor | Explains alone | Adds to all the others |
|---|---|---|
| Industry (2-digit NIC) | 8.4% | 3.8% |
| Gender | 4.2% | 2.1% |
| Employer (public, company, proprietary or partnership, other) | 3.7% | 0.7% |
| State | 2.6% | 1.2% |
| Urban or rural | 1.3% | 1.0% |
| Age, caste, marital status, household spending, graduate, day of week | under 1% each | under 0.3% |

- **All factors together explain only 15%.** Most of the variation comes from things the
  survey does not record, such as the job, the shift or the boss.
- **Industry:** retail finishes at 7:30 pm (92% after 5 pm), restaurants and hotels at 7:30
  pm, IT at 6:30 pm (92% after 5 pm), against 6:00 pm for health (63% after 5 pm) and public
  administration (66%).
- **Employer:** public 5:30 pm, private company 6:00 pm, proprietary or partnership 7:00 pm.
  Public employers finish 30 minutes earlier with the rest held equal.
- **Gender:** women finish at 6:00 pm and men at 6:30 pm (64% against 83% after 5 pm). With
  industry, employer, state and the rest held equal, women finish 64 minutes earlier, because
  women are concentrated in the early-finishing jobs.
- **The day starts at about the same time for everyone**, so the finish is the length of the
  day: start and finish are almost uncorrelated (0.05) and hours of paid work explain 38% of
  finishing time.
- **An early finish does not mean free time for women.** Only 26% of public-sector women are
  still working at 5 pm (public men: 55%), and they do 94 minutes of housework in the evening.
  Comparing within the same industry and education level, public-sector women do 14 minutes
  more evening housework than private-sector women [9-20], and men do 12 more minutes of
  leisure [6-17].

## 4. The weekend: real for some, not for those in trade

![](assets/off-day.png)

- **Who gets the weekend.** Only 47% of salaried people are off on a Sunday and 9% on a
  Saturday. 79% of knowledge-services workers are off on Sunday, against 66% in education,
  health and administration, 42% in manufacturing and construction and 28% in trade,
  transport and hospitality. For knowledge workers the weekend is real; for trade and
  transport it mostly is not.
- **Some work on their days off.** 18% of salaried people do some paid work on a day off, 13%
  in knowledge services and 23% in trade, transport and hospitality.
- **The day off is not equally restful.** Women's domestic time on a day off is 292 [281-302]
  minutes against 71 [67-75] for men. In knowledge services it is 241 [218-263] against 74
  [64-86]. The gap holds in every cut we tried: sector, age, marital status, social group,
  religion and income.
- **Saturday is a work day in every group** we checked, nearly a full one in trade, transport
  and hospitality (7.3-7.8 hours for women, 7.4-8.2 for men).
- The off-day estimates for women in trade, transport and hospitality (n = 110) have wide
  intervals.
- **Most salaried people work on weekends.** 91% [90-92] do some paid work on a Saturday and
  57% [56-59] on a Sunday (92% and 61% outside education), against 94-96% on Monday to
  Friday. The PLFS 2025, which does not give the weekday, agrees: outside education 84.7%
  [84.1-85.3] of salaried workers worked six or more of the last seven days and 28.5%
  [27.8-29.1] worked all seven (women 30.3%, men 27.9%). Weekly hours average 52.3 for men
  and 45.2 for women, and 43.9% work more than 48 hours (`assets/plfs-days-worked.csv`).
- **On any day off, not just the weekend.** Outside education 18.2% [16.4-19.9] do some paid
  work on a day off (17.9% with education), for 6.0 hours on average among those who do
  (women 12.8%, men 19.8%). By the day it falls on: Saturday 18.7% [14.6-23.7], Sunday
  14.5% [12.0-17.2], Monday to Friday 23.0% [20.5-25.6]. 43% are off on a Sunday and 8.8% on a
  Saturday outside education (47% and 9.5% with education). "Day off" is the respondent's
  "other day", so it includes leave and festivals: 51% of off days are Sundays and 11.5% are
  Saturdays.
- **The weekend chart** (`assets/weekend.png`, `assets/weekend-work.csv`, education excluded).
  On a day off women work 360 minutes in total (paid work, housework and care) and men 175;
  unpaid work 320 against 102; housework 276 against 70 (4.6 against 1.2 hours). 93.1% of
  women do some housework on a day off, against 50.8% of men. On a work day the totals are 584
  and 520 minutes. The gap holds on Sundays only and after reweighting to the same industry
  mix. The ratio of women's to men's housework falls from 7.5 to 3.9 because men do more on a
  day off, but the gap in hours widens, so quote hours, not the ratio.

## 5. The fulcrum: the day does not end when paid work does

The quote assumes a worker who is available at 5 pm and on the weekend. This section shows
what makes that possible, and where the unpaid work goes when the wife also has a job.

![](assets/ideal-worker-day.png)

The TUS covers every member of a household, so salaried men can be linked to their wives (the
head with the spouse of the head, or a married child with the spouse of a married child, in
households with exactly one such pair): 23,997 men, 21,225 on a normal work day. Husband and
wife answer for the same weekday.

| Husband on a work day | Husband | Wife |
|---|---|---|
| Housework, whole day (min) | 15 [14-15] | 349 [346-352] |
| Care, whole day (min) | 24 [23-25] | 80 [78-82] |
| Housework, 5 pm to midnight (min) | 7 [6-7] | 118 [117-120] |
| Paid work, 5 pm to midnight (min) | 85 [84-87] | 10 [9-11] |

- **The wife does 92% of the couple's housework and care** (96% of housework alone). Her
  unpaid work is about 7 hours a day, his about 40 minutes. 76% of the wives are on domestic
  duties only and 14% are in regular salaried jobs.
- **Where she is not in paid work, the two work the same hours:** 8.5 for him (nearly all
  paid) and 8.0 for her (almost all unpaid). Where she is in a regular salaried job she works
  10.1 hours against his 8.3.
- **Even then she does the evening shift.** With a salaried wife (n = 2,817), she still does
  209 [203-215] minutes of housework to his 20 [18-22], 95 [92-97] minutes of it after 5 pm to
  his 11 [9-13].
- **It holds for every salaried woman, not only wives of salaried men.** Counting paid work,
  housework and care, a salaried woman works 9.6 hours on a work day and a salaried man 8.6:
  65 minutes more [61-70]. She does 88 minutes less paid work and 153 minutes more unpaid
  work. In the four industry groups we measured the gap is 63 to 108 minutes.
- **Between 5 pm and midnight** women do 78 minutes of domestic work against 10 for men
  (about eight times); this is all salaried people on work days, education included. Housework
  peaks at 40% of salaried women in the half hour from 7:30 pm, against 4% of men.
- **In the six groups on the clock faces** (education excluded, work days, 5 pm to midnight)
  women do 62 minutes of housework against 8 for men: health and public administration 77
  against 10, knowledge services 48 against 8, trade, transport and hospitality 55 against 7.
  Women's evening leisure is 60, 76 and 53 minutes and men's 84, 88 and 63, so housework
  outweighs leisure for women only in the first group (and by 2 minutes in the third). Use the
  word "dominated" with care. The "Parkinson" pattern is real but small, about 9 minutes of
  extra housework for each hour that work finishes earlier.
- **Washing machines (HCES 2023-24 and TUS 2024).** 36% of households that live mainly on a
  wage or salary have a washing machine (46% in cities, 21% in villages), against 20.9% of all
  households (40.4% urban, 11.0% rural); the HCES records presence only, so a missing answer
  counts as "no". In the TUS, women in salaried households that wash by machine spend about 4
  minutes a day less on laundry than comparable women who wash by hand (95% interval about 3
  to 5, controlling for urban or rural, age, household size, per-capita spending and her work
  status); men under 2 minutes either way. Households that outsource laundry have about 26
  minutes less, but only about 3% of salaried households do. The TUS variable is machine
  washing by household members, not ownership, and the comparison is across households, so it
  is an association, not an effect of buying a machine.
- **Money does not change it.** Men's evening housework rises from 7 to 14 minutes between
  the poorest and richest households; women's stays at 76-81. In all 19 groups we cut, women
  do 4 to 12 times the evening housework men do.

## 6. The ideal worker: who can be one

Goyal described a workforce that is "young, talented, skilled, aspirational". We read that as
age 18 to 34 with a graduate or postgraduate degree (84,098 people in the 2025 PLFS file).

| Usual status, % of the group | Men | Women |
|---|---|---|
| Regular wage or salaried | 40.2 | 18.9 |
| Self-employed or unpaid family | 31.4 | 9.6 |
| Casual labour | 2.7 | 0.6 |
| Unemployed | 14.4 | 11.5 |
| Student | 10.1 | 13.2 |
| Domestic duties | 0.2 | 45.1 |
| In the labour force | 88.8 | 40.6 |

- **Women are 32% of this cohort's regular wage workers**, 26% of all regular wage workers.
  Women's overall labour force participation is 40.0% in 2025 (41.7% in 2023-24, a change
  within what the difference in survey design could produce) against 79.1% for men. Among
  women aged 15-59 whose main activity is domestic duties, 86% give child care and
  home-making as the reason.
- **Most working women are not salaried.** Among women aged 18-59 in the PLFS 2025, 8.5%
  [8.3-8.7] are in regular salaried work against 25.1% [24.7-25.5] of men; 51.7% [51.2-52.2]
  are in domestic duties against 0.4% of men; 13.6% are self-employed against 34.6%; 8.8% are
  unpaid family helpers against 7.3% (`assets/plfs-days-worked.csv`). So the "more women in
  the workforce" story is mostly not a salaried story, and the salaried cohort is not who
  the minister's comment about women describes. Of the women in domestic duties, 75% give
  child care and home-making as the main reason (86% of those who gave a reason; 13% have
  none recorded), 0.9% no work at a convenient location and 0.5% a lack of training.
- **The PLFS does not measure willingness to work.** It records the reason for being in
  domestic duties (a constraint, not a preference), whether someone was seeking or available
  for work (0.1% of these women), and the hours available for additional work on each of the
  last seven days (`ahr1`-`ahr7`). It has no questions on evenings or weekends.
- **The people who do fit are in the better part of salaried work.** Young graduates in
  regular wage jobs earn a median Rs 22,600 a month (women 20,000, men 24,500) against
  Rs 15,000 for all regular wage workers. 40% have no written contract (all: 58%) and they
  work a median 48 hours, the same as other regular wage workers, with fewer working 60 hours
  or more (7.6% against 14.8%).
- **So the claim describes men, mostly.** What a longer work week would require of the
  household is in section 5: even without a job, the wife's day is as long as his.

## Verdict: how right is Goyal?

- **The fulcrum:** the quote holds only for a worker whose home is run by someone else, and
  in these households that is almost entirely the wife. If more women are to be in the
  workforce, as he reportedly also said (quote to be sourced), the unpaid work cannot stay where it is, and "nobody will tell
  you it's 5 o'clock" cannot be the norm. The survey shows where the work goes today, not
  what happens as participation rises (that is an inference).
- **"Indians":** it generalises from a minority, mostly men: 20.1% of men and 6.9% of women
  are in regular wage work.
- **5 o'clock:** mostly right in the private sector, wrong overall. 69% are still working at
  5 pm, but a quarter have stopped, and the median finish of 6 pm is an ordinary working day.
  Retail, hospitality and private small firms run late; schools, health and the public sector
  do not.
- **The weekend:** wrong for knowledge workers (79% are off on Sunday) and for most others,
  right for trade, transport and hospitality, where only 28% get Sunday.

## Caveats

- **No occupation field in the TUS.** Groups are industries, so a clerk in a factory is in
  manufacturing and a cashier in a bank is in knowledge services. The within-industry
  comparisons do not control for occupation, seniority, age or urban/rural.
- **"Public" is a lower bound.** State-owned companies recorded as limited companies fall
  into "private". The survey records the employer only on paid-work activities, so there is no
  employer split on off days (only 17% of off-day respondents have a label, and they are the
  ones who worked).
- **Sample.** Regular salaried and wage employees aged 18 and over, including informal salaried
  workers. The TUS has no contract, social security or firm-size field, so there is no
  formal-sector cut.
- **One day per person.** The weekday and the day-of-week comparisons are between different
  people, not one person's week.
- **Household pairs** cover households with a single head-spouse or married-child pair.
- **PLFS 2025** has no data layout in the download; the 2023-24 coding was assumed (the value
  distributions match). PLFS gives hours for each of the last seven days but not the weekday.
- **Weekday weights.** The TUS weights do not equalise the days of the week (Sunday is 12.5%
  of person-days against about 14.3% if equal), a minor effect on the weekend figures.
- **Off days** are the respondent's "other day": weekly off, leave or festival, not literally a
  weekend.
- **Medians** sit on a half-hour grid. "Explains X%" is R-squared, not causation. Small cells
  (women's off days in trade, transport and hospitality, ST workers) are indicative only.

## Not yet covered

- **Goyal's audience** (a gathering of Dutch businessmen) and who he was addressing: needs web
  research.
- **Goyal's exact words on women joining the workforce** in the same speech (recalled, not yet
  sourced; the quote must be checked before it is used).
- **A cross-country test of the fulcrum:** in countries where more women are in paid work,
  do husbands take on unpaid work, or do wives carry a double day? Needs the OECD Time Use
  Database (stats.oecd.org, dataset TIME_USE), which could not be fetched from here (the OECD
  host refuses automated requests); a manual download is needed.
- **What Murthy, Aggarwal and Subrahmanyan's longer-week suggestions imply** for women's labour
  force participation: section 5 gives the household arithmetic, but the extension is yours to
  draw.

## Other charts and tables

The earlier analysis is still in `assets/`: `finish-drivers.png` (median finish and middle half by
industry, employer and gender), `calendar-activity.png` (most time-consuming activity by day of
week), `what-matters.png` (what predicts still working at 5 pm), and `evening.png`,
`evening-splits.png` and `total-work.png` (the second shift in detail). Tables:
`assets/splits-ci.csv`, `assets/employer-ci.csv`, `assets/within-industry.csv`,
`assets/spouse-housework.csv`, `assets/finish-spread.csv`, `assets/finish-drivers.csv`,
`assets/plfs-women-participation.csv`, `assets/plfs-ideal-cohort.csv`,
`assets/plfs-days-worked.csv` and `assets/weekend-work.csv`; the weekend chart is
`assets/weekend.png`. Scripts and how to run them: `scripts/README.md`.
