# Reproducing 09-end-of-shift

Inputs: the cleaned TUS 2024 parquet files in `../../time-use-survey-2024/clean/`
(paths are hard-coded at the top of `build.py`, `grid.py`, `emp.py`).

Every script takes a work directory `D` as its first argument and keeps
intermediates there. Two inputs must also sit in `D`:

- `D/nic-white-collar.yaml`: copy of `../03-90-hr-workweek/nic-white-collar.yaml`
- `D/../conv/ICATUS-2016-Sheet1.csv`: the ICATUS-2016 workbook converted to CSV
  (`soffice --headless --convert-to csv ICATUS-2016.xlsx`; openpyxl cannot read it)

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
