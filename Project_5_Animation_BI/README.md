# Project 5 — Animation Business Intelligence

## Overview

Animation BI is an end-to-end business intelligence project analyzing animated feature films released between 2000 and 2025.

Using movie metadata from The Movie Database (TMDB) API, the project develops a data workflow spanning API-based collection, Python data preparation, relational database modeling, SQL analytics, and interactive Power BI visualization.

The analysis explores audience ratings, TMDB popularity, release-year trends, genres, production companies, production countries, and financial performance where budget and revenue data are available.

The project demonstrates how data from an external API can be transformed into structured, reusable analytical datasets and presented through a business intelligence dashboard.

## Objectives

- Collect and prepare animated-film metadata using the TMDB API.
- Apply documented movie-selection criteria.
- Clean and validate movie records and related reference data.
- Design a relational MySQL database for movie metadata and many-to-many relationships.
- Develop reusable SQL analytical views.
- Build an interactive Power BI dashboard.
- Validate data quality and database restoration.
- Document assumptions, limitations, and reproduction requirements.

## Tools & Technologies

| Technology | Purpose |
|---|---|
| Python | API interaction, data collection, cleaning, and validation |
| TMDB API | Source of movie metadata |
| Pandas | Data manipulation and preparation |
| MySQL | Relational data storage and SQL analytics |
| MySQL Workbench | Database management and query execution |
| Power BI Desktop | Dashboard development and visualization |
| Git | Version control |

## Data Source and Selection Criteria

The project uses the [TMDB API](https://developer.themoviedb.org/docs) to retrieve movie metadata, including release dates, runtime, audience ratings, vote counts, popularity, genres, production companies, production countries, budgets, and revenues.

The discovery-stage candidate dataset uses the following selection criteria:

| Criterion | Selection |
|---|---|
| Genre | Animation (TMDB genre ID 16) |
| Release dates | January 1, 2000–December 31, 2025 |
| Runtime | At least 60 minutes |
| Vote count | At least 100 |
| Adult entries | Excluded |
| Video entries | Excluded |

Candidate discovery prioritized popularity. The resulting dataset is therefore a defined selection of animated feature films, not a comprehensive census of the animation industry. Short films and movies below the vote-count threshold are excluded.

### Candidate Dataset

- **File:** `data/animation_movie_candidates.csv`
- **Records:** 1,236 unique movie candidates

This file represents the discovery-stage dataset. Additional prepared datasets contain movie, genre, production-company, and production-country information for database loading and analysis.

## Project Workflow

The project follows an end-to-end analytics workflow:

1. Explore TMDB discovery and movie-detail endpoints.
2. Discover candidate movies using the defined selection criteria.
3. Inspect and validate the candidate dataset.
4. Collect detailed movie records.
5. Clean and validate movie and related reference data.
6. Load prepared datasets into relational MySQL tables.
7. Develop reusable SQL analytical views.
8. Build a Power BI dashboard using analytical outputs.
9. Validate database results and document data quality, limitations, and setup requirements.

The repository includes prepared datasets, database scripts, five analytical views, a Power BI dashboard, and a separate database restore test.

## Database Design

The MySQL database is named `animation_bi`. Its relational design separates movie records from reference tables and relationship tables, allowing movies to be associated with multiple genres, production companies, and production countries.

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

Staging tables support data preparation and imports:

- `movies_staging`
- `genres_staging`
- `companies_staging`
- `countries_staging`

These tables are separate from the core analytical tables.

### Country Data Import

The `import_countries_to_mysql.py` script reads `data/animation_movie_countries_cleaned.csv` and inserts country relationship records into the existing `countries_staging` table in `animation_bi`.

The script reads `MYSQL_USER` and `MYSQL_PASSWORD` from a local `.env` file. It does not create or clear the staging table.

The chronological working SQL workflow separately creates `countries_staging` and includes subsequent inserts into `production_countries` and `movie_countries`.

**Import consideration:** The country import script uses ordinary inserts. Rerunning it may introduce duplicate rows or cause constraint errors, depending on the existing database state. Review the table contents before rerunning the import.

## SQL Analytics

The primary analytical SQL script is `Project_5_Animation_BI.sql`. It defines five reusable views using `CREATE OR REPLACE VIEW`.

### Analytical Views

| View | Purpose |
|---|---|
| `vw_movie_analysis` | Movie-level analytical fields, financial availability flags, profit, and revenue multiple |
| `vw_year_analysis` | Year-level movie counts, average ratings, popularity, vote counts, and financial metrics |
| `vw_genre_analysis` | Movie counts and average audience/popularity metrics by genre |
| `vw_company_analysis` | Movie counts and average metrics by production company |
| `vw_country_analysis` | Movie counts and average metrics by production country |

### Recorded View Row Counts

The following counts were recorded during development in the original database and a separate restore-test database.

| View | Recorded rows |
|---|---:|
| `vw_movie_analysis` | 1,236 |
| `vw_year_analysis` | 26 |
| `vw_genre_analysis` | 19 |
| `vw_company_analysis` | 81 |
| `vw_country_analysis` | 50 |

The company view includes companies associated with at least 10 distinct movies.

### Analytical Measures

The SQL views support analysis of:

- Movie counts
- Average audience ratings
- Average TMDB popularity
- Average vote counts
- Financial-data availability
- Average budget and revenue
- Average profit
- Revenue multiple

**Profit**

`Revenue - Budget`

**Revenue multiple**

`Revenue / Budget`

Revenue multiple is not a formal return-on-investment (ROI) measure. It does not account for marketing, distribution, financing, or other costs.

Profit and revenue multiple are calculated only when both budget and revenue are available. Revenue multiple additionally requires a positive budget.

## Data Quality and Limitations

Data preparation distinguishes missing financial information from genuine zero values. Zero values in budget and revenue were treated as missing, and three zero-runtime records were converted to missing runtime values.

### Recorded Financial Data Availability

| Measure | Movies |
|---|---:|
| Total movies | 1,236 |
| Budget available | 476 |
| Revenue available | 722 |
| Both budget and revenue available | 424 |
| Budget values treated as missing because they were zero | 760 |
| Revenue values treated as missing because they were zero | 514 |

Missing budget or revenue must not be interpreted as a confirmed zero-dollar amount. Financial analyses consequently use a smaller subset of the full movie population.

### Additional Limitations

- TMDB metadata, popularity, and vote counts can change over time.
- Data for movies released in 2025 may be incomplete relative to all releases during that year.
- Movies can have multiple genres, production companies, and production countries. Aggregated counts across these categories can overlap and should not be summed as though the categories were mutually exclusive.
- TMDB popularity and vote counts are not direct measures of box-office success.
- Budget and revenue coverage varies, limiting the number of movies suitable for financial calculations.
- The selection excludes short films and movies with fewer than 100 votes.
- Popularity-prioritized candidate discovery may influence which titles are represented.

These limitations should be considered when interpreting comparisons and drawing conclusions about the broader animation industry.

## Power BI Dashboard

**Dashboard file:** `Project_5_Animation_BI_Dashboard.pbix`

The dashboard was developed in Power BI Desktop and successfully refreshed during development. It presents six analytical sections on a single page.

### 1. Industry Overview

High-level KPIs summarize the selected movie population.

| KPI | Recorded value |
|---|---:|
| Total movies | 1,236 |
| Average rating | 6.99 |
| Average popularity | 8.38 |
| Average vote count | Approximately 1,524 |

These values are recorded development results, not guaranteed to remain identical if the source data or dashboard calculations change.

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

### Power BI Model Consideration

The current model includes a relationship between `vw_movie_analysis[release_year]` and `vw_year_analysis[release_year]`. The other analytical views are disconnected in the current model.

This is an important implementation detail when interpreting cross-visual filtering behavior. The dashboard should not be assumed to have a fully connected relationship model across every analytical view.

## Project Files

| File or directory | Purpose |
|---|---|
| `Project_5_Animation_BI.sql` | Primary SQL script defining the five analytical views |
| `Project_5_Animation_BI_database_export.sql` | MySQL database export containing structures, data, and final view definitions |
| `data/Project_5_Animation_BI_working_sql_workflow.sql` | Chronological working SQL log covering imports, validation, exploratory checks, and view definitions |
| `Project_5_Animation_BI_Dashboard.pbix` | Power BI dashboard |
| `data/animation_movie_candidates.csv` | Discovery-stage dataset containing 1,236 unique candidates |
| `import_countries_to_mysql.py` | Country relationship import script |
| `README.md` | Project documentation |
| `.gitignore` | Excludes specified local environment and development files from version control |

The `data/` directory also contains prepared movie, genre, company, and country datasets.

Additional Python scripts support TMDB access, candidate discovery, detailed data collection, cleaning, data-quality checks, data-model validation, and database imports.

The presence of a script in the repository does not by itself establish that every collection or preparation step has been rerun from scratch.

### Important SQL Workflow Note

`data/Project_5_Animation_BI_working_sql_workflow.sql` is a chronological working log, not a standalone database backup or a script intended to run from beginning to end on a fresh database without preparation.

Statements depend on tables and staging data created or populated in earlier steps, and some import commands use machine-specific absolute file paths. Review the required database state, execution order, and file paths before rerunning individual sections.

For the final analytical view definitions, use `Project_5_Animation_BI.sql`.

For database restoration, use the database export with an appropriate target schema and compatible MySQL environment.

## Security and Reproducibility

TMDB credentials are stored locally in `.env`. Never commit or publish this file or disclose the API token.

The `.gitignore` is intended to exclude:

- `.env`
- `.venv/`
- `__pycache__/`
- `.vs/`

Reproducing the workflow requires:

- Appropriate TMDB API credentials for API-dependent collection steps
- A compatible Python environment and required dependencies
- MySQL and suitable database permissions
- Prepared project data for the applicable import steps
- Power BI Desktop to open and interact with the dashboard

The project includes database and analytical deliverables, but the complete workflow is not packaged as a fully automated, fresh-machine setup. Environment configuration, database prerequisites, import order, and machine-specific paths may require adjustment.

### Database Restore Test

The database export was restored into a separate schema named `animation_bi_restore_test`. The live `animation_bi` schema was not used as the restore target.

The test recreated the expected 11 tables and five analytical views. Recorded row counts included:

| Object | Recorded rows |
|---|---:|
| `movies` | 1,236 |
| `vw_movie_analysis` | 1,236 |
| `vw_year_analysis` | 26 |
| `vw_genre_analysis` | 19 |
| `vw_company_analysis` | 81 |
| `vw_country_analysis` | 50 |

This was a structural and row-count validation, not an exhaustive row-by-row comparison or a guarantee of portability across MySQL environments.

The export contains view definers using `root@localhost`. This may affect portability because other MySQL environments may not have the same account or permissions. Review the definers and applicable privileges before restoring the export elsewhere.

## Portfolio Context

Project 5 extends the animation analytics portfolio with movie-level entertainment data and a business intelligence workflow.

| Project | Focus |
|---|---|
| Project 1 — Data Collection | YouTube animation data collection through an API |
| Project 2 — Performance Analytics | Performance analysis and visualization |
| Project 3 — Title Strategy Analysis | Patterns in animation video titles |
| Project 4 — SQL Analytics | SQL-based analysis of YouTube animation data |
| Project 5 — Animation BI | TMDB movie data, relational MySQL modeling, reusable analytical views, and a Power BI dashboard |

Together, these projects demonstrate experience across API-based data collection, Python data preparation, exploratory analysis, text analysis, SQL querying, relational data modeling, and business intelligence visualization.

## Attribution

This product uses the TMDB API but is not endorsed or certified by TMDB.

[TMDB API Documentation](https://developer.themoviedb.org/docs)

## Project Status

The core Project 5 deliverables are complete for portfolio presentation:

- Candidate dataset containing 1,236 unique movies
- Core relational database tables and five analytical views
- Power BI dashboard with six analytical sections
- Recorded analytical view row counts and KPI values
- Separate database restore test with expected table, view, and row counts
- Documented country import workflow
- Published project files and documentation in the GitHub repository

The project documents known limitations rather than claiming fully automated, fresh-machine reproducibility. Database portability, machine-specific import paths, and the current Power BI relationship model should be considered when reproducing or extending the work.