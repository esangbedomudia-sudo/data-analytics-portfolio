Project 5 — Animation BI
Status: In progress
Domain: Animation and entertainment analytics
Primary data source: The Movie Database (TMDB) API
Core stack: Python, pandas, MySQL, SQL, Power BI
Project Overview
Project 5 is a business intelligence and analytics project exploring animated feature films released from 2000 through 2025. It transforms TMDB movie metadata into a relational MySQL data model, reusable analytical views, and an interactive Power BI dashboard.

The project examines audience ratings, TMDB popularity, release-year trends, genres, production companies, production countries, and financial performance where budget and revenue data are available. It is designed to demonstrate a practical end-to-end analytics workflow using a dataset connected to the animation and entertainment industry.

The project is still in progress. The core dataset, database model, five analytical views, dashboard, and a separate database restore test have been developed. Final workflow documentation, portability review, repository checks, and remaining validation are not yet complete.
Objectives
- Collect and prepare animated-film metadata through the TMDB API.
- Apply consistent, documented movie-selection criteria.
- Clean and validate movie-level and related dimension data.
- Model movies and their many-to-many relationships in MySQL.
- Create reusable SQL views for movie-level and aggregated analysis.
- Build a Power BI dashboard for industry trends and comparisons.
- Document data quality, assumptions, and analytical limitations.
- Package the work clearly for a data analytics or business intelligence portfolio.
Data Source and Selection Criteria
This project uses the TMDB API. TMDB provides movie metadata including release dates, runtime, audience ratings, vote counts, popularity, genres, production companies, production countries, budgets, and revenues. Coverage varies by field and title.

The candidate discovery dataset was selected using these criteria:
Criterion	Selection
Genre	Animation (TMDB genre ID 16)
Release dates	January 1, 2000–December 31, 2025
Runtime	At least 60 minutes
Vote count	At least 100
Adult entries	Excluded
Video entries	Excluded


The initial candidate discovery prioritized popularity. The resulting dataset represents this defined selection—not every animated film ever produced. It also excludes short films and titles below the vote-count threshold, so results should not be generalized to the entire animation industry without qualification.
Candidate Dataset
- File: data/animation_movie_candidates.csv
- Records: 1,236 unique movie candidates
This is the discovery-stage candidate file. Additional collected, cleaned, and analytical data files are used in the database and dashboard workflow.
Technology Stack
Technology	Role
Python	API interaction, data collection, cleaning, validation, and preparation
TMDB API	Movie metadata source
pandas	Data manipulation and preparation
MySQL	Relational storage and SQL analytics
MySQL Workbench	Database management and query execution
Power BI Desktop	Dashboard development and visualization
Git	Version control


Workflow
The project workflow covers:
1. Explore TMDB discovery and movie-detail endpoints.
2. Discover candidate movies using the established criteria.
3. Inspect and validate the candidate dataset.
4. Collect detailed movie records.
5. Clean and validate movie, genre, company, and country data.
6. Load data into relational MySQL tables.
7. Create reusable analytical views.
8. Build the Power BI dashboard.
9. Validate outputs, document limitations, and prepare the repository.
The database and dashboard stages have been developed. Remaining work focuses on reproducibility, portability, documentation accuracy, and final repository checks.
Data Model
The MySQL database is named animation_bi. The relational design separates movie records from reference data and relationship tables, allowing a movie to be associated with multiple genres, production companies, and production countries.
Core Tables
Table	Purpose
movies	Movie-level metadata and analytical fields
genres	Genre reference data
movie_genres	Movie-to-genre relationships
production_companies	Production-company reference data
movie_companies	Movie-to-company relationships
production_countries	Production-country reference data
movie_countries	Movie-to-country relationships


Staging tables used in data preparation include movies_staging, genres_staging, companies_staging, and countries_staging. They support imports and are distinct from the core analytical tables.
Country Data Import
import_countries_to_mysql.py reads data/animation_movie_countries_cleaned.csv and inserts country relationship records into the existing countries_staging table in animation_bi. It reads MYSQL_USER and MYSQL_PASSWORD from the local .env file. The script does not create or clear the staging table.

The chronological working SQL workflow separately creates countries_staging and includes the subsequent inserts into production_countries and movie_countries. Do not rerun the country import script just to verify the workflow: it uses ordinary inserts and may add duplicate rows or encounter constraint errors.
SQL Analytics
The primary analytical SQL file is Project_5_Animation_BI.sql. It defines five views with CREATE OR REPLACE VIEW.
View	Purpose
vw_movie_analysis	Movie-level analytical fields, financial availability flags, profit, and revenue multiple
vw_year_analysis	Year-level movie counts, average ratings, popularity, vote counts, and financial metrics
vw_genre_analysis	Movie counts and average audience/popularity metrics by genre
vw_company_analysis	Movie counts and average metrics by production company
vw_country_analysis	Movie counts and average metrics by production country


Recorded View Row Counts
These counts were checked during development in the original database and in a separate restore-test database.
View	Recorded rows
vw_movie_analysis	1,236
vw_year_analysis	26
vw_genre_analysis	19
vw_company_analysis	81
vw_country_analysis	50


The company view includes companies associated with at least 10 distinct movies.
Analytical Measures
The project includes movie counts, average audience rating, average popularity, average vote count, financial-eligibility counts, average budget, average revenue, average profit, and portfolio revenue multiple.
- Profit: Revenue - Budget
- Revenue multiple: Revenue / Budget
The revenue multiple is not a formal return-on-investment (ROI) measure. It does not account for marketing, distribution, financing, or other costs. Profit and revenue multiple are calculated only where both budget and revenue are available; revenue multiple also requires a positive budget.
Data Quality and Limitations
Missing financial data is distinguished from a genuine value of zero. During preparation, zero values in budget and revenue were treated as missing, and three zero-runtime records were converted to missing runtime values.
Recorded Financial Availability
Measure	Movies
Total movies	1,236
Budget available	476
Revenue available	722
Both budget and revenue available	424
Budget values treated as missing because they were zero	760
Revenue values treated as missing because they were zero	514


Missing budget or revenue must not be interpreted as a confirmed zero-dollar amount. Financial analyses use a smaller subset than the full movie population.
Other Limitations
- TMDB metadata, popularity, and vote counts can change over time.
- The 2025 release-year data may be incomplete relative to all films released that year.
- A movie may have multiple genres, production companies, and production countries. Aggregated counts across these categories can overlap and should not be summed as though categories were mutually exclusive.
- TMDB popularity and vote counts are not direct measures of box-office success.
- Budget and revenue coverage varies, limiting the number of movies suitable for financial calculations.
- The selection excludes short films and movies with fewer than 100 votes, limiting generalization beyond the selected population.
- The candidate discovery process prioritized popularity, which may affect which titles are represented.
Power BI Dashboard
File: Project_5_Animation_BI_Dashboard.pbix

The dashboard has been developed in Power BI Desktop and was successfully refreshed during development. It contains six analytical sections on a single page.
1. Industry Overview
High-level KPIs summarize the selected movie population.
KPI	Recorded value
Total Movies	1,236
Average Rating	6.99
Average Popularity	8.38
Average Vote Count	Approximately 1,524


2. Year Trends
Explores how movie volume, audience ratings, popularity, vote counts, and available financial measures vary by release year.
3. Genre Analysis
Compares genres by movie count and audience/popularity measures.
4. Production Companies
Examines production-company representation and compares company-level movie and audience metrics. The SQL analysis uses a minimum threshold of 10 distinct movies per company.
5. Country Analysis
Explores production countries associated with the selected films and compares movie counts and audience/popularity measures.
6. Financial Performance
Examines available budgets, revenues, profit, and revenue multiples while accounting for incomplete financial coverage.

The current Power BI model includes a relationship between vw_movie_analysis[release_year] and vw_year_analysis[release_year]. The other analytical views are disconnected in the current model. The dashboard is built, but final validation and documentation are still part of the project’s remaining work.
Project Files
The main deliverables include:
File or directory	Purpose
Project_5_Animation_BI.sql	Primary SQL script defining the five analytical views
Project_5_Animation_BI_database_export.sql	MySQL database export containing structures, data, and final view definitions
data/Project_5_Animation_BI_working_sql_workflow.sql	Chronological working SQL log of imports, validation, exploratory checks, and view definitions
Project_5_Animation_BI_Dashboard.pbix	Power BI dashboard
data/animation_movie_candidates.csv	Discovery-stage dataset of 1,236 unique candidates
import_countries_to_mysql.py	Country relationship import script
README.md	Project documentation
.gitignore	Excludes local environment and generated development files from version control


The data/ directory also contains prepared movie, genre, company, and country files. Python scripts support TMDB access, candidate discovery, detailed data collection, cleaning, quality checks, data-model validation, and database imports. Script presence alone does not establish that every step has been rerun or independently validated.
Important SQL Workflow Note
data/Project_5_Animation_BI_working_sql_workflow.sql is a chronological working log, not a standalone database backup or a script intended to run from top to bottom on a fresh database. Statements depend on tables and staging data created or populated in earlier steps, and some import commands use machine-specific absolute file paths. Review the required database state, execution order, and file paths before rerunning individual sections.
Security and Reproducibility
TMDB credentials are stored locally in .env. Never commit or publish this file or disclose the token. The .gitignore is intended to exclude .env, .venv/, __pycache__/, and .vs/.

Reproducing the workflow requires appropriate TMDB credentials, a compatible Python environment and dependencies, MySQL, the prepared project data, and Power BI Desktop to open the dashboard. The current workflow and database export still require portability and reproducibility review before they can be described as a fully automated, fresh-machine setup.
Database Restore Test
The database export was restored into a separate schema named animation_bi_restore_test; the live animation_bi schema was not used as the restore target. The test recreated the expected 11 tables and five analytical views. Recorded counts included 1,236 rows in movies and vw_movie_analysis, 26 in vw_year_analysis, 19 in vw_genre_analysis, 81 in vw_company_analysis, and 50 in vw_country_analysis.

This was a structural and row-count validation, not an exhaustive row-by-row comparison or a guarantee of portability across MySQL environments. The export’s root@localhost view definer remains a portability consideration.
Portfolio Context
Project 5 extends the animation analytics portfolio with movie-level entertainment data and a business intelligence workflow.
- Project 1 — Data Collection: YouTube animation data collection through an API.
- Project 2 — Performance Analytics: Performance analysis and visualization.
- Project 3 — Title Strategy Analysis: Patterns in animation video titles.
- Project 4 — SQL Analytics: SQL-based analysis of YouTube animation data.
- Project 5 — Animation BI: TMDB movie data, a relational MySQL model, reusable analytical views, and a Power BI dashboard.
Attribution
This product uses the TMDB API but is not endorsed or certified by TMDB.
Current Status and Remaining Work
Project 5 is in progress and should not yet be considered complete.
Completed or checked during development
- Candidate dataset of 1,236 unique movies.
- Core relational tables and five analytical views.
- Power BI dashboard with six sections and recorded KPI values.
- Recorded row-count checks for the analytical views.
- Separate database restore test with expected table, view, and row counts.
- Country import workflow documented.
- Git commits created for the dashboard, README updates, restore-test documentation, and country-import documentation.
Remaining work
1. Review the chronological SQL workflow for clarity and reproducibility without blindly executing it from top to bottom.
2. Assess database-export portability, including the root@localhost view definer.
3. Confirm that README file listings and descriptions match the final project structure.
4. Verify Git tracking and ensure .env, credentials, and unnecessary local files are not committed.
5. Complete any necessary corrections, rerun appropriate non-destructive checks, and commit the final updates.
The project should be marked complete only after these remaining checks and documentation updates have been addressed.