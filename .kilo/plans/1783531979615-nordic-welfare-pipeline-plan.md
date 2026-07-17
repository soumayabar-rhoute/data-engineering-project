# Nordic Welfare Resilience Pipeline — Plan

End-to-end data engineering project: build an automated pipeline that pulls socioeconomic
indicators (1990–2024) for the 5 Nordics (Sweden, Norway, Denmark, Finland, Iceland) from the
World Bank and OECD APIs, validates/cleans/transforms them, loads into PostgreSQL (medallion
layers), and answers the research question via SQL, Python, and Power BI.

## Confirmed decisions
- **Learn-as-you-build**: short learning track before each build phase; nothing studied in advance.
- **Medallion layers** in Postgres: `raw → staging → intermediate → marts`.
- **Plain Python + CLI** orchestration (no Airflow/scheduler) — simplest for a first project.
- **Postgres in Docker only**; Python runs in a local venv.
- **pytest** unit tests on transform/validate + inline quality checks (no live API tests in CI).

## What to learn first (before touching project code)
Learn each just before you need it:
1. **Python basics** (variables, functions, modules, `pip`, virtualenvs) — before Phase 2.
2. **`requests` + JSON** (calling REST APIs, parsing responses) — before Phase 2.
3. **Pandas** (DataFrames, groupby, pivot, merge, read/write CSV/JSON) — before Phase 4/5.
4. **SQL basics** (SELECT, WHERE, JOIN, GROUP BY, window functions) — before Phase 3/6.
5. **PostgreSQL + Docker** (run Postgres in a container, connect with a client) — before Phase 3.
6. **SQLAlchemy** (engine, connection, `to_sql`) — before Phase 3.
7. **pytest** (write a test, run it, use fixtures) — before Phase 8.
8. **Power BI** (Get Data → Postgres, build a visual, slicers) — before Phase 10.

Free resources: Python → python.org docs / Real Python; SQL → Mode SQL tutorial; Postgres +
Docker → official docs; Pandas → pandas.pydata.org user guide; pytest → docs.pytest.org.

## Build phases (ordered)
**Phase 0 — Environment & repo**
- Install Python 3.11+, Docker Desktop, Git, VS Code, Power BI Desktop.
- Create `requirements.txt` (pandas, requests, sqlalchemy, psycopg2-binary, pytest, python-dotenv),
  `.env.example`, `.gitignore` (ignore `.env`, `__pycache__/`, `.pytest_cache/`, `data/`).
- Create `docker-compose.yml` with one `postgres:16` service (port 5432, named volume). Start it:
  `docker compose up -d`. Verify with `docker compose ps`.
- Init Git repo (already done), make first commit, push to a new GitHub repo. Commit per phase.

**Phase 1 — Define the fixed indicator set** (`config/indicators.yaml`)
Pick ~12–15 indicators measuring "welfare resilience" (ability to protect citizens through
shocks like 2008/COVID). Suggested:
- World Bank: GDP per capita const. `NY.GDP.PCAP.KD`; unemployment `SL.UEM.TOTL.ZS`; youth
  unemployment `SL.UEM.YOUTH.ZS`; Gini `SI.POV.GINI`; life expectancy `SP.DYN.LE00.IN`; health
  exp %GDP `SH.XPD.CHEX.GD.ZS`; education exp %GDP `SE.XPD.TOTL.GD.ZS`; gov debt %GDP
  `GC.DOD.TOTL.GD.ZS`; population `SP.POP.TOTL`.
- OECD (SDMX): social spending %GDP `SOCX`; tax revenue %GDP `REV`; long-term unemployment;
  low-income/poverty rate `INE`.
Each YAML entry: `name, source (wb/oecd), code, unit, description`. This file drives the pipeline.

**Phase 2 — Extract** (`src/extract_worldbank.py`, `src/extract_oecd.py`)
- WB REST/JSON, no key: `https://api.worldbank.org/v2/country/{iso3}/indicator/{code}?format=json&date=1990:2024&per_page=1000`
  (response is `[metadata, observations]`; use index 1).
- OECD SDMX-JSON, no key: `https://stats.oecd.org/sdmx-json/data/{dataset}/...` (parse
  `dataSets` + `structure.dimensions`; do ONE dataset first, then generalize).
- Return list-of-dicts (one row per country-year-indicator) AND save raw JSON/CSV to `data/raw/`.
- Wrap in try/except, small `time.sleep` between calls.

**Phase 3 — Load raw** (`src/db.py`, `src/load.py`, `sql/01_init_schema.sql`)
- `raw` schema stores data exactly as received (text/JSON columns), one table per source.
- SQLAlchemy engine from `.env`; add `ingested_at` timestamp. This is the audit trail.

**Phase 4 — Validate + staging** (`src/validate.py`)
Inline checks before promoting data: required columns/types present; `year BETWEEN 1990 AND 2024`;
no unexpected NULLs; value sanity (unemployment/Gini 0–100); country is one of the 5 Nordics.
On failure raise a clear error or write to `staging.quality_issues`. Passed rows → `staging`
(typed long table: `country, year, indicator_code, value, unit`).

**Phase 5 — Transform + intermediate** (`src/transform.py`)
- Unify WB + OECD into one long format; standardize units; add `indicator_name`.
- Handle missing years (document: forward-fill or flag gaps). Output `intermediate.indicators_long`.

**Phase 6 — Marts** (`sql/02_marts.sql`)
Analytics-ready views for the research question:
- `marts.resilience_scorecard` (one row per country-year, all indicators side by side).
- `marts.crisis_impact` (2008→2009→2010 deltas: unemployment, debt, social spend).
- `marts.trend_1990_2024` (long trends for dashboards).

**Phase 7 — Orchestrate** (`pipeline/run.py`)
CLI running extract → validate → load(raw) → staging → transform → intermediate → marts.
Flags: `--source wb`, `--rebuild`. Run: `python -m pipeline.run`.

**Phase 8 — Tests** (`tests/`)
- `test_transform.py`, `test_validate.py` using `tests/fixtures/` samples (no network).
- Assert good rows pass and bad rows (null year, out-of-range value) are caught. Run: `pytest`.

**Phase 9 — Analysis** (`sql/03_analysis.sql`, `analysis/research_analysis.py`)
- SQL answering "How resilient was the Nordic welfare model 1990–2024?" (pre/post-crisis
  trajectories, inequality, social-spending buffers).
- Python: load marts via SQLAlchemy, summary stats, export matplotlib PNGs for the report.

**Phase 10 — Power BI**
Connect to Postgres (`localhost:5432`, `marts` schema). Build 3–4 visuals: Nordic trends
1990–2024, crisis-impact bars, inequality/spending scatter, country slicer.

**Phase 11 — Document & finalize**
Write `README.md`: goal, architecture (mermaid/text), run + test instructions, research-answer
summary, Power BI screenshots. Final commit + push, tag `v1.0`.

## Risks / tips
- OECD SDMX is the hard part — finish WB fully, then one OECD dataset, then generalize.
- Missing data is normal; validation must handle (not crash on) gaps.
- Never commit `.env`.
- Commit per phase so you always have a working state.
- If an API shape changes, only `extract` + `validate` change — the payoff of layering.

## Open questions
- Exact final indicator list (refine in Phase 1).
- Missing-year handling policy (forward-fill vs. flag) — decide in Phase 5.
