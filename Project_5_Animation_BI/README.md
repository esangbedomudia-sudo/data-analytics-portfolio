# Project 5 — Animation BI

**Status:** Portfolio-ready  
**Domain:** Animation and entertainment analytics  
**Primary data source:** The Movie Database (TMDB) API  
**Technology stack:** Python, pandas, MySQL, SQL, Power BI

## Project Overview

Animation BI is an end-to-end business intelligence project analyzing animated feature films released between 2000 and 2025. The project transforms TMDB movie metadata into a relational MySQL data model, reusable SQL analytical views, and an interactive Power BI dashboard.

The analysis explores audience ratings, TMDB popularity, release-year trends, genres, production companies, production countries, and financial performance where budget and revenue data are available.

The project demonstrates a practical analytics workflow involving API-based data collection, data preparation, relational database design, SQL analysis, dashboard development, and data-quality validation.

## Objectives

- Collect and prepare animated-film metadata through the TMDB API.
- Apply consistent, documented movie-selection criteria.
- Clean and validate movie-level and related dimension data.
- Model movies and their many-to-many relationships in MySQL.
- Develop reusable SQL views for detailed and aggregated analysis.
- Build an interactive Power BI dashboard.
- Document data quality, assumptions, and analytical limitations.
- Package the project for a data analytics or business intelligence portfolio.

## Data Source and Selection Criteria

The project uses the [TMDB API](https://developer.themoviedb.org/docs), which provides movie metadata such as release dates, runtime, audience ratings, vote counts, popularity, genres, production companies, production countries, budgets, and revenues.

The discovery-stage dataset was selected using the following criteria:

| Criterion | Selection |
|---|---|
| Genre | Animation (TMDB genre ID 16) |
| Release dates | January 1, 2000–December 31, 2025 |
| Runtime | At least 60 minutes |
| Vote count | At least 100 |
| Adult entries | Excluded |
| Video entries | Excluded |

Candidate discovery prioritized popularity. Consequently, the dataset represents a defined selection of animated feature films rather than a comprehensive census of the animation industry. Short films and titles below the vote-count threshold are excluded.

### Candidate Dataset

- **File:** `data/animation_movie_candidates.csv`
- **Records:** 1,236 unique movie candidates

This file represents the discovery-stage candidate dataset. Additional prepared movie, genre, company, and country data support the database and dashboard workflow.

## Technology Stack

| Technology | Role |
|---|---|
| Python | API interaction, data collection, cleaning, validation, and preparation |
| TMDB API | Movie metadata source |
| pandas | Data manipulation and preparation |
| MySQL | Relational storage and SQL analytics |
| MySQL Workbench | Database management and query execution |
| Power BI Desktop | Dashboard development and visualization |
| Git | Version control |

## Project Workflow

The project follows an end-to-end analytics workflow:

1. Explore TMDB discovery and movie-detail endpoints.
2. Discover candidate movies using the established selection criteria.
3. Inspect and validate the candidate dataset.
4. Collect detailed movie records.
5. Clean and validate movie, genre, company, and country data.
6. Load the prepared data into relational MySQL tables.
7. Develop reusable SQL analytical views.
8. Build a Power BI dashboard.
9. Validate database outputs and document data quality, limitations, and setup considerations.

The project includes prepared datasets, database scripts, five analytical views, a Power BI dashboard, and a separate database restore test.

## Data Model

The MySQL database is named `animation_bi`. Its relational design separates movie records from reference data and relationship tables, allowing each movie to be associated with multiple genres, production companies, and production countries.

### Core Tables

| Table | Purpose |
|---|---|
| `movies` | Movie-level metadata and analytical fields |
| `genres` | Genre reference data |
| `movie_genres` | Movie-to-genre relationships |
| `production_companies` | Production-company reference data |
| `movie_companies` | Movie-to-company relationships |
| `production_countries` | Production-country reference data |
| `movie_countries` | Movie-to-country relationships |

Staging tables used during data preparation include `movies_staging`, `genres_staging`, `companies_staging`, and `countries_staging`. These support imports and are distinct from the core analytical tables.

### Country Data Import

`import_countries_to_mysql.py` reads `data/animation_movie_countries_cleaned.csv` and inserts country relationship records into the existing `countries_staging` table in `animation_bi`.

The script reads `MYSQL_USER` and `MYSQL_PASSWORD` from a local `.env` file. It does not create or clear the staging table.

The chronological working SQL workflow separately creates `countries_staging` and includes subsequent inserts into `production_countries` and `movie_countries`.

**Important:** The country import script uses ordinary inserts. Rerunning it may introduce duplicate rows or cause constraint errors, depending on the existing database state. Review the current table contents before rerunning the import.

## SQL Analytics

The primary analytical SQL file is `Project_5_Animation_BI.sql`. It defines five reusable views using `CREATE OR REPLACE VIEW`.

| View | Purpose |
|---|---|
| `vw_movie_analysis` | Movie-level analytical fields, financial availability flags, profit, and revenue multiple |
| `vw_year_analysis` | Year-level movie counts, average ratings, popularity, vote counts, and financial metrics |
| `vw_genre_analysis` | Movie counts and average audience/popularity metrics by genre |
| `vw_company_analysis` | Movie counts and average metrics by production company |
| `vw_country_analysis` | Movie counts and average metrics by production country |

### Recorded View Row Counts

The following counts were checked during development in the original database and a separate restore-test database.

| View | Recorded rows |
|---|---:|
| `vw_movie_analysis` | 1,236 |
| `vw_year_analysis` | 26 |
| `vw_genre_analysis` | 19 |
| `vw_company_analysis` | 81 |
| `vw_country_analysis` | 50 |

The company view includes companies associated with at least 10 distinct movies.

### Analytical Measures

The project includes:

- Movie counts
- Average audience rating
- Average TMDB popularity
- Average vote count
- Financial-data availability counts
- Average budget and revenue
- Average profit
- Revenue multiple

**Profit**

`Revenue - Budget`

**Revenue multiple**

`Revenue / Budget`

The revenue multiple is not a formal return-on-investment (ROI) measure. It does not account for marketing, distribution, financing, or other costs. Profit and revenue multiple are calculated only where both budget and revenue are available; revenue multiple additionally requires a positive budget.

## Data Quality and Limitations

Missing financial data is distinguished from a genuine value of zero. During preparation, zero values in budget and revenue were treated as missing, and three zero-runtime records were converted to missing runtime values.

### Recorded Financial Data Availability

| Measure | Movies |
|---|---:|
| Total movies | 1,236 |
| Budget available | 476 |
| Revenue available | 722 |
| Both budget and revenue available | 424 |
| Budget values treated as missing because they were zero | 760 |
| Revenue values treated as missing because they were zero | 514 |

Missing budget or revenue must not be interpreted as a confirmed zero-dollar amount. Financial analyses therefore use a smaller subset of the full movie population.

### Other Limitations

- TMDB metadata, popularity, and vote counts can change over time.
- The 2025 release-year data may be incomplete relative to all films released that year.
- Movies can have multiple genres, production companies, and production countries. Aggregated counts across these categories can overlap and should not be summed as though the categories were mutually exclusive.
- TMDB popularity and vote counts are not direct measures of box-office success.
- Budget and revenue coverage varies, limiting the number of movies suitable for financial calculations.
- The selection excludes short films and movies with fewer than 100 votes.
- Popularity-prioritized candidate discovery may affect which titles are represented.

These limitations should be considered when interpreting comparisons and drawing conclusions about the broader animation industry.

## Power BI Dashboard

**File:** `Project_5_Animation_BI_Dashboard.pbix`

The dashboard was developed in Power BI Desktop and successfully refreshed during development. It contains six analytical sections on a single page.

### 1. Industry Overview

High-level KPIs summarize the selected movie population.

| KPI | Recorded value |
|---|---:|
| Total movies | 1,236 |
| Average rating | 6.99 |
| Average popularity | 8.38 |
| Average vote count | Approximately 1,524 |

### 2. Year Trends

Explores changes in movie volume, audience ratings, popularity, vote counts, and available financial measures by release year.

### 3. Genre Analysis

Compares genres by movie count and audience/popularity measures.

### 4. Production Companies

Examines production-company representation and compares company-level movie and audience metrics. The SQL analysis applies a minimum threshold of 10 distinct movies per company.

### 5. Country Analysis

Explores production countries associated with the selected films and compares movie counts and audience/popularity measures.

### 6. Financial Performance

Examines available budgets, revenues, profit, and revenue multiples while accounting for incomplete financial coverage.

### Power BI Model Note

The current model includes a relationship between `vw_movie_analysis[release_year]` and `vw_year_analysis[release_year]`. The other analytical views are disconnected in the current model.

This is an important implementation detail when interpreting cross-visual filtering behavior. The dashboard's existence does not imply that every view participates in a shared relationship model.

## Project Files

The principal deliverables include:

| File or directory | Purpose |
|---|---|
| `Project_5_Animation_BI.sql` | Primary SQL script defining the five analytical views |
| `Project_5_Animation_BI_database_export.sql` | MySQL database export containing structures, data, and final view definitions |
| `data/Project_5_Animation_BI_working_sql_workflow.sql` | Chronological working SQL log of imports, validation, exploratory checks, and view definitions |
| `Project_5_Animation_BI_Dashboard.pbix` | Power BI dashboard |
| `data/animation_movie_candidates.csv` | Discovery-stage dataset of 1,236 unique candidates |
| `import_countries_to_mysql.py` | Country relationship import script |
| `README.md` | Project documentation |
| `.gitignore` | Excludes local environment and generated development files from version control |

The `data/` directory also contains prepared movie, genre, company, and country files. Python scripts support TMDB access, candidate discovery, detailed data collection, cleaning, quality checks, data-model validation, and database imports.

The presence of a script in the repository does not by itself establish that every collection or preparation step has been rerun from scratch.

### Important SQL Workflow Note

`data/Project_5_Animation_BI_working_sql_workflow.sql` is a chronological working log, not a standalone database backup or a script intended to run from beginning to end on a fresh database without preparation.

Statements depend on tables and staging data created or populated in earlier steps, and some import commands use machine-specific absolute file paths. Review the required database state, execution order, and file paths before rerunning individual sections.

For the final analytical view definitions, use `Project_5_Animation_BI.sql`. For database restoration, use the database export with an appropriate target schema and compatible MySQL environment.

## Security and Reproducibility

TMDB credentials are stored locally in `.env`. Never commit or publish this file or disclose the API token.

The `.gitignore` is intended to exclude `.env`, `.venv/`, `__pycache__/`, and `.vs/`.

Reproducing the full workflow requires:

- Appropriate TMDB API credentials for API-dependent collection steps
- A compatible Python environment and required dependencies
- MySQL and suitable database permissions
- The prepared project data for applicable import steps
- Power BI Desktop to open and interact with the dashboard

The project includes database and analytical deliverables, but the complete workflow is not packaged as a fully automated fresh-machine setup. Environment configuration, database prerequisites, import order, and machine-specific paths may require adjustment.

### Database Restore Test

The database export was restored into a separate schema named `animation_bi_restore_test`; the live `animation_bi` schema was not used as the restore target.

The test recreated the expected 11 tables and five analytical views. Recorded counts included:

| Object | Recorded rows |
|---|---:|
| `movies` | 1,236 |
| `vw_movie_analysis` | 1,236 |
| `vw_year_analysis` | 26 |
| `vw_genre_analysis` | 19 |
| `vw_company_analysis` | 81 |
| `vw_country_analysis` | 50 |

This was a structural and row-count validation, not an exhaustive row-by-row comparison or a guarantee of portability across MySQL environments.

The export contains view definers using `root@localhost`. This is a portability consideration because other MySQL environments may not have the same account or permissions. Review the definers and appropriate privileges before restoring the export elsewhere.

## Portfolio Context

Project 5 extends the animation analytics portfolio with movie-level entertainment data and a business intelligence workflow.

| Project | Focus |
|---|---|
| Project 1 — Data Collection | YouTube animation data collection through an API |
| Project 2 — Performance Analytics | Performance analysis and visualization |
| Project 3 — Title Strategy Analysis | Patterns in animation video titles |
| Project 4 — SQL Analytics | SQL-based analysis of YouTube animation data |
| Project 5 — Animation BI | TMDB movie data, a relational MySQL model, reusable analytical views, and a Power BI dashboard |

Together, these projects demonstrate experience across API-based data collection, Python data preparation, exploratory analysis, SQL querying, relational data modeling, and business intelligence visualization.

## Attribution

This product uses the TMDB API but is not endorsed or certified by TMDB.

TMDB documentation: https://developer.themoviedb.org/docs

## Project Status

The core Project 5 deliverables are complete for portfolio presentation:

- Candidate dataset containing 1,236 unique movies
- Core relational database tables and five analytical views
- Power BI dashboard with six analytical sections
- Recorded analytical view row counts and KPI values
- Separate database restore test with expected table, view, and row counts
- Documented country import workflow
- Published project files and documentation in the GitHub repository

The project is presented with documented limitations rather than a claim of fully automated, fresh-machine reproducibility. Database portability, machine-specific import paths, and the current Power BI relationship model should be considered when reproducing or extending the work.

