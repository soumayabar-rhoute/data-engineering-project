# Nordic Welfare Model Resilience - Data Engineering Project Plan

**Timeline:** 10–14 weeks (realistic for a beginner)  
**Pace:** 4–6 hours per week  
**Goal:** Build an automated data pipeline, then analyze and visualize the results.  
**Stack:** Python, Pandas, Requests, SQLAlchemy, pytest, PostgreSQL, Docker, Git/GitHub

---

## Critical Rule: No Step Is Complete Until You Can Explain It

Before moving to the next step, you must be able to answer these three questions out loud or in writing:

1. **What** did I just build?
2. **Why** does it work this way?
3. **How** would I explain it to someone who has never seen this before?

If you cannot answer all three, do not proceed. Go back, re-read the code, break it on purpose, fix it, and try again. This is not optional. This is how you build real understanding.

---

## Pre-Project: Foundations (Week 0)

**These are non-negotiable prerequisites. Do not skip them.**

### Python Fundamentals (1–2 weeks)

**Learn:**
- Variables, data types, loops, functions, lists, dictionaries
- `if/else` logic and basic error handling (`try/except`)
- Installing packages with `pip`
- Virtual environments (`python -m venv .venv`)

**Prove you understand (mandatory):**
1. Write a function `calculate_average(numbers)` that returns the average of a list of numbers.
2. Without looking at any reference, write a `for` loop that iterates through a list of dictionaries and prints each dictionary's `"name"` key.
3. Write a `try/except` block that catches a `ZeroDivisionError` when dividing by zero.

**Resources:**
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [Automate the Boring Stuff with Python, Chapters 1–6](https://automatetheboringstuff.com/)

**Checkpoint:** You have written and run three scripts without looking at tutorials. If you had to Google basic syntax, you are not ready. Go back and practice more.

---

### Command Line Basics (2–3 days)

**Learn:**
- `cd`, `ls`/`dir`, `mkdir`, `python --version`
- Running Python scripts: `python script.py`
- What the current directory is (`pwd` on Mac/Linux, `cd` on Windows)

**Prove you understand:**
1. Create a folder `test_project`, navigate into it, create a file `hello.py` that prints `"Hello"`, and run it from the command line.
2. Navigate up one level and back into `test_project` using two different methods.

**Checkpoint:** You can navigate and run scripts without thinking about each command.

---

### Git Basics (2–3 days)

**Learn:**
- `git init`, `git add`, `git commit`, `git status`
- Creating a repo on GitHub and pushing to it
- What `.gitignore` does and why it matters

**Prove you understand:**
1. Create a new repo locally, make 3 commits with different messages, push to GitHub.
2. Intentionally create a merge conflict, resolve it, and push the resolution.
3. Explain out loud: "What does `git add` do? What does `git commit` do? How are they different?"

**Resources:**
- [GitHub Skills: Git Handbook](https://skills.github.com/)

**Checkpoint:** You can describe the Git workflow from memory: working directory → staging area → local repository → remote repository.

---

## Phase 1 — Project Setup (Weeks 1–2)

*Difficulty: Medium. Lots of new tools, but mostly following instructions.*

### Step 1: Create the folder structure and initialize Git

**What to learn first:**
- What a "repository" is
- Why folder structure matters in larger projects
- The difference between a folder and a Git repo

**Tasks:**
1. Create the main project folder and subfolders.
2. Initialize Git and make the first commit.
3. Create a `.gitignore` file (Google "python gitignore template" if needed).
4. Create a GitHub repo and push to it.

**Understanding check (mandatory):**
1. Without looking at your commands, write down what `git init`, `git add .`, and `git commit -m "..."` each do.
2. Explain why `.gitignore` is important. Give an example of a file that should be ignored and why.
3. Draw a simple diagram showing the relationship between your local folder, Git, and GitHub.

**Expected outcome:** A clean GitHub repo with folders but no code yet. You can explain the Git workflow from memory.

---

### Step 2: Set up Python virtual environment and install packages

**What to learn first:**
- What a virtual environment is (isolated Python setup per project)
- What `pip` does
- The difference between `pip install` and `pip freeze`

**Tasks:**
1. Create and activate a virtual environment.
2. Create `requirements.txt` and install packages.
3. Run `pip freeze > requirements.txt` to lock versions.

**Understanding check (mandatory):**
1. Without looking at notes, explain: "What is a virtual environment and why do I need one?"
2. Delete your `.venv` folder. Recreate it from `requirements.txt` using only `pip install -r requirements.txt`. If this fails, you do not understand the workflow yet.
3. Explain the difference between `pip install pandas` and `pip freeze > requirements.txt`.

**Expected outcome:** You can destroy and recreate your Python environment from scratch using only `requirements.txt`.

---

### Step 3: Set up Docker and PostgreSQL

**What to learn first:**
- What Docker is (containers = lightweight, isolated, reproducible software packages)
- What PostgreSQL is (a relational database that stores data in tables)
- What a "connection string" is (the address your code uses to find the database)

**Beginner alternative:** If Docker feels overwhelming, use SQLite first (file-based, no server). You can switch to PostgreSQL later.

**Tasks:**
1. Install Docker Desktop.
2. Create `docker-compose.yml` and start PostgreSQL.
3. Verify the database is running.

**Understanding check (mandatory):**
1. Without looking at any reference, write down what each line in your `docker-compose.yml` does.
2. Explain the difference between `docker compose up` and `docker compose down`.
3. Explain what a "volume" does in Docker and why it matters for a database.
4. Connect to the database using `psql` and run `SELECT 1;`. Explain what happened.

**Expected outcome:** You can start and stop a database with one command and explain what is happening behind the scenes.

---

### Step 4: Create a simple connection test

**What to learn first:**
- What SQLAlchemy is (a Python library that connects code to databases)
- What an "engine" is (the interface between Python and the database)
- Environment variables and `.env` files (storing secrets outside your code)

**Tasks:**
1. Create `.env` with your database connection string.
2. Write `scripts/test_connection.py` that connects and prints the database version.

**Understanding check (mandatory):**
1. Without looking at your code, draw a diagram showing: `.env` → `load_dotenv()` → `os.getenv()` → `create_engine()` → `engine.connect()` → SQL query.
2. Explain why you should NOT hardcode your database password in Python files.
3. Change the database password in `docker-compose.yml`, restart the container, and update `.env` to match. Verify the connection script still works.

**Expected outcome:** You understand the full path from environment variable to database query.

---

## Phase 2 — Data Ingestion (Weeks 3–4)

*Difficulty: Medium-High. This is where many beginners get stuck. Take your time.*

### Step 5: Learn about APIs (1–2 days)

**What to learn first:**
- What an API is (a program that answers questions with data)
- REST APIs: GET requests, JSON format, query parameters
- How to read API documentation
- What an "indicator" or "dataset" means

**Hands-on practice (do this BEFORE writing any pipeline code):**
1. In your browser, go to: `https://api.worldbank.org/v2/country?format=json&per_page=3`
2. You should see a JSON response. This is exactly what your code will receive.
3. Change `per_page=3` to `per_page=5` and observe the difference.
4. Change `format=json` to `format=xml` and observe the difference.

**Understanding check (mandatory):**
1. Without looking at any notes, explain what JSON is and why APIs use it.
2. Explain the difference between a URL path parameter (`/country/NOR`) and a query parameter (`?format=json`).
3. Pick one World Bank indicator code. Without using the internet, explain what data you think it represents and why you would want it for this project.

**Expected outcome:** You can read API documentation and construct a URL by hand.

---

### Step 6: Fetch data from World Bank API manually

**What to learn first:**
- The `requests` library: `requests.get()`, `response.status_code`, `response.json()`
- JSON parsing in Python
- What a DataFrame is (a table-like structure in Pandas)

**Tasks:**
1. Write `scripts/test_world_bank.py` that fetches GDP per capita for Norway.
2. Explore the response structure with `print()` statements.
3. Extract the data into a DataFrame.

**Understanding check (mandatory):**
1. Intentionally break your code: change the indicator code to something invalid. Run it. Read the error. Explain what happened.
2. Without looking at your code, write out the full URL that `requests.get()` will call (include all query parameters).
3. Explain what `response.raise_for_status()` does and why it is useful.
4. Draw a diagram showing: URL → HTTP request → JSON response → DataFrame.

**Expected outcome:** You understand the full request/response cycle for an API call.

---

### Step 7: Build a reusable World Bank fetcher function

**What to learn first:**
- Writing functions: parameters, return values, docstrings
- Single-responsibility principle (one function does one thing)
- Default arguments in Python

**Tasks:**
1. Create `src/ingestion/world_bank.py` with `fetch_indicator()`.
2. Test it with multiple indicators.

**Understanding check (mandatory):**
1. Without looking at your code, write the function signature from memory: `def fetch_indicator(____):`
2. Explain what `";".join(COUNTRIES)` does and why we need it.
3. Add a `print()` statement inside the function to show the URL being called. Run it. Verify the URL is correct.
4. Refactor: add a `source` parameter to the function. Explain why this makes the function more reusable.

**Expected outcome:** You can write and explain a function that encapsulates an API workflow.

---

### Step 8: Save raw data and orchestrate ingestion

**What to learn first:**
- CSV writing: `df.to_csv()`
- `os.listdir()` or `glob` for looping over files
- Python scripts as entry points (`if __name__ == "__main__":`)

**Tasks:**
1. Identify 4–5 indicators and save them as CSVs to `data/raw/`.
2. Create a script that loops through indicators and saves them all.

**Understanding check (mandatory):**
1. Without looking at your script, write out the full ingestion workflow from memory.
2. Open one of your raw CSV files in a text editor. Explain what you see and why the data looks the way it does.
3. Intentionally break the script by renaming a raw CSV file. Run the orchestration script. Observe what happens. Explain the error.

**Expected outcome:** You have raw data files and understand the full ingestion flow.

---

### Step 9: Try the OECD API (optional)

**Beginner note:** If you are struggling, skip this. Come back after the World Bank pipeline works end-to-end.

**Understanding check (mandatory if you do this step):**
1. Without looking at any notes, explain one difference between the World Bank API and the OECD API.
2. Explain why different APIs might return data in different structures.

---

## Phase 3 — Data Validation & Cleaning (Weeks 5–6)

*Difficulty: Medium. Pandas manipulation can be tricky.*

### Step 10: Learn Pandas basics (1–2 days)

**What to learn first:**
- Loading CSVs: `pd.read_csv()`
- Inspecting data: `df.head()`, `df.info()`, `df.describe()`
- Checking for nulls: `df.isnull().sum()`
- Checking for duplicates: `df.duplicated().sum()`
- Filtering rows: `df[df["value"] > 0]`

**Hands-on practice:**
1. Load one raw CSV. Run every command listed above.
2. Write down what each command does in your own words.

**Understanding check (mandatory):**
1. Without looking at any reference, explain what a DataFrame is and how it differs from a Python list or dictionary.
2. Write code that loads a CSV, filters for rows where `value > 50000`, and prints the number of remaining rows.
3. Explain what `df.info()` tells you that `df.head()` does not.

**Resources:**
- [Pandas 10-minute tutorial](https://pandas.pydata.org/docs/user_guide/10min.html)

**Expected outcome:** You can load, inspect, and filter a DataFrame without looking at documentation.

---

### Step 11: Build a validator

**What to learn first:**
- What "data quality" means
- How to write checks that catch problems
- Boolean logic and conditional statements

**Tasks:**
1. Create `src/validation/validator.py` with checks for schema, nulls, duplicates, and value ranges.
2. Run it against your raw data.

**Understanding check (mandatory):**
1. Without looking at your code, write out the four validation checks from memory.
2. Intentionally introduce a problem into a raw CSV (add a duplicate row, add a null value, add a value outside the valid range). Run the validator. Explain which check caught which problem.
3. Explain why validation happens BEFORE cleaning, not after.

**Expected outcome:** You understand what data quality problems exist in real-world data and how to detect them.

---

### Step 12: Build a cleaner

**What to learn first:**
- `drop_duplicates()`, `fillna()`, `dropna()`, `astype()`
- String methods: `.str.strip()`
- Pandas method chaining

**Tasks:**
1. Create `src/validation/cleaner.py`.
2. Test it on raw data.

**Understanding check (mandatory):**
1. Without looking at your code, explain what `df.copy()` does and why it is important in the cleaner.
2. Explain the difference between `fillna()` and `dropna()`. When would you use each?
3. Intentionally break a DataFrame by setting a numeric column to strings. Run the cleaner. Explain what `pd.to_numeric(errors="coerce")` does to the broken values.
4. Refactor the cleaner to also handle negative unemployment values (set them to NaN). Explain your logic.

**Expected outcome:** You can transform messy data into clean data and explain every transformation.

---

### Step 13: Orchestrate validation and cleaning

**Tasks:**
1. Create `src/validation/run_validation.py` that processes all raw files.
2. Save cleaned data to `data/staging/`.

**Understanding check (mandatory):**
1. Without looking at your code, explain the full validation/cleaning pipeline from raw CSV to staging CSV.
2. Compare a raw CSV and its cleaned version side by side. List every difference and explain why each change was made.
3. Explain what would happen if you ran the cleaner twice on the same data. Would it produce the same result? Why or why not?

**Expected outcome:** You have a reproducible validation/cleaning pipeline and understand every transformation it performs.

---

## Phase 4 — Database Loading (Weeks 7–8)

*Difficulty: Medium-High. This is the most complex phase. Take it slow.*

### Step 14: Learn SQL basics (1 week)

**What to learn first:**
- What SQL is (a declarative language for querying relational databases)
- Basic queries: `SELECT`, `FROM`, `WHERE`, `ORDER BY`
- Creating tables: `CREATE TABLE`
- Inserting data: `INSERT INTO`
- Data types: `INTEGER`, `FLOAT`, `VARCHAR`, `TEXT`, `TIMESTAMP`

**Hands-on practice:**
1. Connect to PostgreSQL with `psql`.
2. Create a test table, insert rows, query them back.
3. Try `SELECT` with `WHERE`, `ORDER BY`, and `LIMIT`.

**Understanding check (mandatory):**
1. Without looking at any notes, write a SQL query that selects all countries with GDP per capita greater than 50000.
2. Explain what a "primary key" is and why it matters.
3. Explain the difference between `VARCHAR(50)` and `TEXT`. When would you use each?
4. Write a `CREATE TABLE` statement for a simple `users` table with `id`, `name`, `email`, and `created_at`.

**Resources:**
- [SQLBolt Lessons 1–6](https://sqlbolt.com/)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)

**Expected outcome:** You can write basic SQL queries and create tables without looking at documentation.

---

### Step 15: Design your database schema

**What to learn first:**
- What a "table" is in a database
- Primary keys, foreign keys, unique constraints
- Data types and when to use them

**Beginner approach:** Start with ONE simple table. Refactor to a star schema later if you want.

**Tasks:**
1. Design a single `indicators` table.
2. Write `sql/schema.sql`.
3. Run it and verify the table exists.

**Understanding check (mandatory):**
1. Without looking at your SQL, write the `CREATE TABLE` statement from memory.
2. Explain every column in your table: what it stores, what type it is, and why.
3. Explain the `UNIQUE(country, year, indicator_code)` constraint. What problem does it solve?
4. Draw a diagram of your table showing columns, types, and constraints.

**Expected outcome:** You can design a simple database schema and explain every design decision.

---

### Step 16: Load data into the database

**What to learn first:**
- `DataFrame.to_sql()` method
- SQLAlchemy engine and connection basics
- `if_exists` parameter: `"replace"`, `"append"`, `"fail"`

**Tasks:**
1. Create `src/loading/loader.py`.
2. Load all staged CSVs into PostgreSQL.
3. Verify with SQL queries.

**Understanding check (mandatory):**
1. Without looking at your code, explain what `df.to_sql()` does step by step.
2. Explain the difference between `if_exists="replace"` and `if_exists="append"`. Which one did you use and why?
3. Run `SELECT COUNT(*) FROM indicators;` in psql. Explain what the number means.
4. Intentionally run the loader twice. What happens? Is this good or bad? How would you fix it?

**Expected outcome:** You can load Pandas DataFrames into PostgreSQL and understand the implications of different loading strategies.

---

### Step 17: Build the full pipeline entry point

**Tasks:**
1. Create `src/main.py` that chains ingestion → validation → cleaning → loading.
2. Run it end-to-end.

**Understanding check (mandatory):**
1. Without looking at your code, draw a flowchart of the pipeline from start to finish.
2. Explain what happens at each step if something goes wrong (e.g., API is down, CSV is corrupted, database is offline).
3. Run the pipeline from a clean state. Verify data in PostgreSQL. Explain what you see.

**Expected outcome:** You have a working pipeline and can trace any piece of data from API to database.

---

## Phase 5 — Testing (Weeks 9–10)

*Difficulty: Medium. New concepts, but very valuable.*

### Step 18: Learn pytest basics (2–3 days)

**What to learn first:**
- What unit tests are (small, isolated tests for small pieces of code)
- Test functions: `def test_something():`
- Assertions: `assert result == expected`
- Running tests: `pytest`
- Test fixtures: setup code that runs before tests

**Hands-on practice:**
1. Write a test that checks `1 + 1 == 2`.
2. Write a test that checks a function you wrote in a previous phase.
3. Make the test fail. Observe the failure. Fix the code. Observe the pass.

**Understanding check (mandatory):**
1. Without looking at any notes, explain what a "unit test" is and why it is useful.
2. Explain the difference between `assert` and `print()` for verifying code behavior.
3. Write a test for a function that does NOT exist yet. Run it. Watch it fail. Explain why it failed.

**Resources:**
- [Python Testing with pytest, Chapters 1–3](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/)

**Expected outcome:** You understand the test-code-fail-fix-pass cycle.

---

### Step 19: Write tests for your cleaner

**What to learn first:**
- `@pytest.fixture` for reusable test data
- Parametrized tests: `@pytest.mark.parametrize`
- Asserting DataFrame shapes and values

**Tasks:**
1. Write `tests/test_cleaner.py` with tests for whitespace stripping, null removal, type conversion, and duplicate removal.
2. Run `pytest tests/test_cleaner.py -v`.

**Understanding check (mandatory):**
1. Without looking at your code, explain what a `fixture` is and why it is useful.
2. Write a test that verifies the cleaner handles a DataFrame with ALL null values in the `value` column. What should happen? Why?
3. Make one of your tests fail by changing the expected output. Run pytest. Explain the failure message.

**Expected outcome:** You can write tests that verify data transformations.

---

### Step 20: Write tests for your validator and loader

**Tasks:**
1. Write `tests/test_validator.py`.
2. Write `tests/test_loader.py` (test DataFrame preparation; database testing comes later).

**Understanding check (mandatory):**
1. Without looking at your code, list all the validator checks and explain what problem each one catches.
2. Write a test that passes a DataFrame with the wrong columns to the validator. Explain what should happen.
3. Explain why testing the actual database is harder than testing pure Python functions.

**Expected outcome:** You have a test suite for your core pipeline components.

---

## Phase 6 — Analysis & SQL Modeling (Weeks 10–11)

*Difficulty: Medium. This is where you connect data to insights.*

### Step 21: Learn SQL for analysis

**What to learn first:**
- `SELECT` with multiple conditions
- `GROUP BY` and `ORDER BY`
- Aggregations: `AVG()`, `MAX()`, `MIN()`, `COUNT()`
- Filtering: `WHERE`, `HAVING`
- Aliases: `AS`

**Hands-on practice:**
1. Run analytical queries against your `indicators` table.
2. Save queries as `.sql` files in `sql/analysis/`.

**Understanding check (mandatory):**
1. Without looking at any notes, explain what `GROUP BY` does and when you need it.
2. Explain the difference between `WHERE` and `HAVING`.
3. Write a query that finds the average unemployment rate for each Nordic country. Explain each clause.

**Resources:**
- [SQLBolt Lessons 7–12](https://sqlbolt.com/)

**Expected outcome:** You can write SQL queries that answer analytical questions.

---

### Step 22: Write analysis queries for your research questions

**Tasks:**
1. Write SQL files for:
   - Unemployment trends
   - Gini inequality trends
   - GDP vs. social spending correlation
   - Resilience during crises (1990s, 2008, COVID)

**Understanding check (mandatory):**
1. Without looking at your queries, write out your research questions in plain English.
2. For each query, explain: "What question does this answer? What does the result mean?"
3. Run each query. Write a 2–3 sentence interpretation of the results.

**Expected outcome:** You have SQL queries that answer your research questions and can explain what the results mean.

---

### Step 23: Python analysis with Pandas and Matplotlib

**What to learn first:**
- Jupyter notebooks basics
- Plotting with Matplotlib or Seaborn
- Connecting notebooks to PostgreSQL with SQLAlchemy

**Tasks:**
1. Create `notebooks/analysis.ipynb`.
2. Pull data from PostgreSQL and create visualizations.

**Understanding check (mandatory):**
1. Without looking at your notebook, explain how data flows from PostgreSQL to a chart.
2. Explain what a line chart shows and why it is appropriate for time-series data.
3. Create a new visualization (e.g., a bar chart) that you did not build in the tutorial. Explain what it shows.

**Expected outcome:** You can analyze data in Python and create meaningful visualizations.

---

## Phase 7 — Dashboard (Weeks 11–12)

*Difficulty: Medium. Depends on which tool you choose.*

### Step 24: Build a dashboard

**Option A: Streamlit (Recommended for beginners)**
- Install: `pip install streamlit`
- Create `app.py` with interactivity
- Run: `streamlit run app.py`

**Option B: Power BI**
- Connect to PostgreSQL
- Build pages with KPIs, slicers, and charts

**Minimum viable dashboard:**
- 1 page with a dropdown to select country
- Line chart showing 1–2 indicators over time

**Understanding check (mandatory):**
1. Without looking at your dashboard code, explain how a user interacts with it from start to finish.
2. Explain what a "data model" is in the context of your dashboard.
3. Add one new feature (e.g., a new indicator, a new chart type) without following a tutorial. Explain what you built and why.

**Expected outcome:** You can build an interactive dashboard and explain how it works.

---

## Phase 8 — Deepening Understanding (Weeks 12+)

This phase is where you transform from "I followed a tutorial" to "I deeply understand this."

### Step 25: The Feynman Technique (Teach to Learn)

**What to do:**
1. Write a 1-page document explaining your entire project to a 10-year-old. No jargon.
2. Record a 5-minute video (or audio) explaining the pipeline. Imagine you are teaching a friend.
3. Post it somewhere (GitHub README, LinkedIn, a blog). Public accountability forces clarity.

**Understanding check (mandatory):**
1. If you cannot explain it simply, you do not understand it well enough. Go back and study that part.

---

### Step 26: Break Everything on Purpose

**What to do:**
For each component, break it intentionally and fix it:

| Component | How to break it | What you learn |
|-----------|----------------|----------------|
| API fetcher | Use an invalid indicator code | Error handling, HTTP status codes |
| Validator | Add a column with all nulls | What happens when validation fails |
| Cleaner | Add a row with a negative unemployment value | How cleaning handles edge cases |
| Loader | Run it twice without deduplication | Idempotency and why it matters |
| Database | Drop the `indicators` table | What happens when schema is missing |
| Pipeline | Disconnect internet during ingestion | Retry logic and failure modes |

**Understanding check (mandatory):**
For each broken component, write a 2-sentence explanation of what happened and why.

---

### Step 27: Rebuild from Memory

**What to do:**
1. Delete all your code (keep your `data/` folder and database).
2. Rebuild the entire pipeline from scratch without looking at the old code.
3. Compare your new version to the old version. Note what you did differently and why.

**Understanding check (mandatory):**
1. If you cannot rebuild a component without reference, you have not internalized it yet. Review and try again.

---

### Step 28: Extend the Project

**What to do:**
Add something that was NOT in the plan. Examples:
- Add a new data source (e.g., Eurostat API)
- Add a new indicator you researched yourself
- Implement retry logic with exponential backoff for API calls
- Add a second database table and join it in queries
- Implement a simple star schema with dimension tables
- Add CI/CD with GitHub Actions
- Containerize the entire pipeline with Docker

**Understanding check (mandatory):**
1. Explain every line of the new code you wrote.
2. Explain how the new feature integrates with the existing pipeline.

---

## Final Verification: Can You Build This From Scratch?

At the end of the project, close your laptop. Open a blank text editor. Without looking at any of your old code or notes, answer these questions:

1. **Pipeline:** Write out the full data pipeline from API to dashboard. Name each step and the technology used.
2. **Code:** Write the `fetch_indicator()` function from memory. Write the `clean_dataframe()` function from memory. Write the `CREATE TABLE` statement from memory.
3. **Concepts:** Explain in your own words: API, JSON, DataFrame, SQL, primary key, virtual environment, Docker container, unit test, idempotency.
4. **Debugging:** Describe a bug you encountered and how you fixed it. What did you learn?

If you cannot do this, you are not done. Go back to the phase where the gap is and deepen your understanding.

---

## How This Plan Guarantees Understanding

| Mechanism | What it prevents | How it works |
|-----------|-----------------|--------------|
| **Understanding checks before every step** | Skipping ahead without comprehension | You cannot proceed until you can explain the concept |
| **"Explain it back" exercises** | Illusion of competence from copy-paste | Teaching forces you to organize knowledge mentally |
| **Break-on-purpose exercises** | Fragile understanding that breaks under pressure | You learn failure modes and recovery |
| **Rebuild from memory** | Dependency on tutorials and references | You prove you internalized the structure |
| **Feynman technique** | Surface-level knowledge | Simplifying for others reveals gaps in your own understanding |
| **Extension exercises** | "I followed instructions" mindset | Building something new requires deep comprehension |

**A plan cannot force you to learn.** But this plan removes every shortcut. You cannot passively check boxes and claim understanding. Every step requires active demonstration of knowledge.

The difference between this plan and a tutorial is: **a tutorial gives you answers. This plan forces you to generate answers.**

---

## Timeline (Understanding-Focused)

| Weeks | Phase | Focus | Understanding Check |
|-------|-------|-------|---------------------|
| 0 | Pre-Project | Python, Git, CLI | 3 programming tasks from memory |
| 1–2 | Setup | Folders, venv, Docker | Explain every command and config file |
| 3–4 | Ingestion | APIs, requests, CSVs | Trace data flow from URL to file |
| 5–6 | Validation | Pandas, cleaning | Write validator and cleaner from memory |
| 7–8 | Loading | SQL, schema, loader | Explain SQL + Python integration |
| 9–10 | Testing | pytest, test design | Write tests for all components |
| 10–11 | Analysis | SQL queries, notebooks | Answer research questions with data |
| 11–12 | Dashboard | Streamlit or Power BI | Build interactive dashboard from scratch |
| 12+ | Deepening | Teach, break, rebuild, extend | Rebuild entire project from memory |

**Total: 10–14 weeks at 4–6 hours/week.**

This is slower than a tutorial. But when you finish, you will not just have a project. You will have a mental model of how data engineering works that you cannot unlearn.
