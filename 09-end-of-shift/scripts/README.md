# Reproducing 09-end-of-shift

Sample: regular salaried / wage employees, cooperative respondents, aged 18 and over (`build.py`).

Inputs: the cleaned TUS 2024 parquet files in `../../time-use-survey-2024/clean/`
(paths are hard-coded at the top of `build.py`, `grid.py`, `emp.py`).

Every script takes a work directory `D` as its first argument and keeps
intermediates there. Two inputs must also sit in `D`:

- `D/nic-white-collar.yaml`: copy of `../03-90-hr-workweek/nic-white-collar.yaml`
- `D/../conv/ICATUS-2016-Sheet1.csv`: the ICATUS-2016 workbook converted to CSV
  (`soffice --headless --convert-to csv ICATUS-2016.xlsx`, then rename the output to
  `ICATUS-2016-Sheet1.csv`; openpyxl cannot read the workbook)

Run in this order (`python scripts/<name>.py D`):

| Step | Script | Writes (in `D`) |
|---|---|---|
| 1 | `build.py` | `sal_rows.parquet`: salaried, cooperative persons, minutes from 4 am |
| 2 | `grid.py` | `persons.parquet`, `grid.parquet`: 48-slot grid + household merge |
| 3 | `ana.py` | `P2.pkl`, `G2.pkl`: cohort flags |
| 4 | `hh.py` | `P3.pkl`: household splits, 03 white-collar flag |
| 5 | `emp.py` | `employer.parquet`: public / private labels |
| 6 | `boot.py` | `boot.pkl`: cluster-bootstrap CIs for the charts |
| 7 | `boot_splits.py` | `splits_ci.csv` |
| 8 | `boot_emp.py` | `employer_ci.csv` |
| 9 | `within.py` | `within_ind.csv` |
| 10 | `charts.py D OUT` | `still-working.png`, `evening.png`, `off-day.png` in `OUT` |

`tab.py` holds the shared activity grouping and profile function (imported by
exec from the other scripts). `q1.py`, `ind.py`, `wk.py`, `hh_off.py` print the
exploratory tables behind the text of `results.md`.

The CSVs in `assets/` are the outputs of steps 7-9, renamed with hyphens.

Extra figure (not in `results.md` yet): `clock.py D OUT` writes `clock-faces.png`. It needs steps 1-5 only
(it reads `P3.pkl` and `employer.parquet`).

`calheat.py D OUT` writes `calendar-activity.png` (most time-consuming activity by day of week and survey quarter,
same six cohorts as the clocks). It needs steps 1-5 and reads `sub_round` from the raw person file.

Note: run each script to completion. Piping a script into `head` kills it early (SIGPIPE) and can leave a stale
intermediate file, e.g. `P3.pkl`, which every later step reads.

## PLFS and household analyses (not in `results.md` yet)

These use other inputs and are independent of steps 1-10 above, except `spouse.py`, which needs `P3.pkl`.

- `plfs_profile.py <cperv12025.csv> <out.csv>`: profile of the "ideal worker" cohort (age 18-34, graduate or above) in the PLFS 2025
  person file: usual status, occupation, industry, employer, earnings, contract, leave, social security, hours and days worked.
  Writes `assets/plfs-ideal-cohort.csv`.
- `plfs_women.py <cperv12025.csv> <perv1.dta> <out.csv>`: women's labour force participation, 2023-24 against 2025, by sector, age,
  education and marital status, plus the stated reason for domestic duties. Writes `assets/plfs-women-participation.csv`.
- `spouse.py <TUS clean dir> <P3.pkl> <out.csv>`: salaried men linked to their wives in the same TUS household (housework, care,
  paid work and leisure, with cluster-bootstrap intervals). Writes `assets/spouse-housework.csv`. `spouse_chart.py <csv> <png>`
  draws `assets/ideal-worker-day.png`.

The PLFS 2025 file (`Data_in_CSV.zip`, with no data layout) is not in the repo. The scripts assume the 2023-24 coding for education,
enterprise type, contract, paid leave and social security; value distributions match. PLFS gives hours for each of the last
seven days but not the weekday, so "worked all 7 days" is the closest measure of weekend work.
