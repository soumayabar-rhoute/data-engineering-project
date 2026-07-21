# data-engineering-project
## why this project? : 
hey I'm Soumaya Bar-rhoute, moroccan  data and ai engineering student at ENSAM Rabat. this is my first dara-engineering-project. 
it's my first project ever. hahaha
m going to build everything from scratch understand everyhting step by step inchallah . 
fpr help m using google, and kilo's extension on vscode. let's go.
---
# project's folder structure: 
## requirements.txt: 
lists every Python package your project needs,
with locked versions, i created it so that everyonr can recreact te exact Pythpn environment with one command: pip install -r requirements.txt.
without it we'll be dependent on whatever version of pandas happens to be installed in our maching, which causes "it works on my laptop" bugs.
## dockerfile : 
this file gives instrustions for docker to build a container for our project, it packages our code, dependecies, and runtime into a single unit that runs identically everywhere. 
## but what's the diffrence between requirements.txt and dockerfile:
requirements.txt tells Python what packages your application needs.

Dockerfile tells Docker how to build an entire computer environment that can run your application.
## makefile: 
okay so now the makefile i still don't understand it that much.
a makefile defines shortucts for common commands. instead of typing long commands we simply type make run. 
in python projects it's mainly optional , use donly if we have +3 commands we type repeatedly. 
but the idea it's not clear yet. i'll learn it while doing the project.
## .gitignore: 
tells git which files to completly ignore and never commit.
.gitigonore only affects untracked files. if we already committed a file and then add it to .gitignor ,git will still tarck it we have to run : 
git rm --cached -r file
critical entries for this project: 
.venv : the virtual environment. 
_pycache_ : python bytcode
.env : contains secrets like database passwords.
.data/raw: large downloads data files.
data/raw*:  tells git : "ignore every file inside data/raw"
!data/raw/.gitkeep: but do not ignore files named .gitkeep
committing raw data wastes space and creates merge conflicts. 
.logs/: 
log files change every time we run the piplenie. no need to commit them 
## src/ : 
contains all our python code and nothing else. The subdirectories are organized by domain, not by technical layer : the idea is still not clear,
## src/ingestion/ : data acquisition : 
contains code that talks to external apis and downloads raw data. 
isolating ingestion means we can change the api url aor add a new one without touching validation or loading code.
## src/validation : data quality check:
raw data from APIs is messy, validation catched problems before they pollute our database, cleaning fixes them. sperating validation from ingestion means we can improve data quality without redownloading data.
## src/loading : database operations : 
contains loader.py, which takes cleaned data and writes it to PostgreSQL.
## data/ : all data files : 
the only place data lives. Code never writes data outside this folder. 
## data/raw : untouched downloaded data :
contains csv files exactly as they came from the API.
if a cleaner bug corrupts data, we can always re-ingest from raw contains .gitkeep file so git tracks the empty folder. the actual CSVs are gitignored as mentiones before. 
## data/staging/ : cleaned, analysis-ready data:
contains csv files after validation and cleaning before loading to the database . it's a sefety checkpoint. we can inspect cleaned data before it hits the database. 
also contains a .gitkeep file for the same reason. 
## tests\ : Automated tests: 
it exists to prove that my code works and prevent regressions, 
## scripts: 
not every piece of the code deserves a module in src/, some things are just tools we run once to verify something. scripts/ in the junk drawer for those. 
## sql :
will contains schema "table definitions" and analysis. 
## docs/ : Documentation:
### architecure.md
diagrams and explanations of how the pipeline works.
### data_dictionary : 
what each colmn means, units and sources.
### workflows.md : 
how to run the pipeline, common commands.

## commands:
.venv\Scripts\activate.ps1 : with every new terminal. 
## what's a virtual environment : 
a virtual environment in Python is an isolated environment on our computer where we can run and test our python projects. 
it allows us to manage project-specific dependencies without interfering with other projects or the original Python installation. it is a separate container for each Python project.
# deactivate pur venv: 
deactivate
# delete the .venv folder entirely :
Remove-Item -Recurse -Force .venv
# recreate it : 
python -m venv .venv 
# reinstall every package from the locked requirements.txt: 
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
# verify it worked: 
python -c "import pandas, requests, sqlalchemy, psycopg2, yaml, dotenv, pytest; print('ALL OK')"
# what is pip : 
pip is the package installer for python. you can use pip to install packages from the python Package index.
# pip install: 
adds new libraries to our python environment.
# pip freeze: 
it looks at our currently active python ven and prints every install package with its exact version, 
## What is PostgreSQL? : 
PostgreSQL is a powerful open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workolads.
## what SQLAlchemy:
SQLAlchemy: is a python library used to interact with relational databases using Python code. It provides tools for executing sql queries and managing databes connections