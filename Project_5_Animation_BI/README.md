# Project 5 — Animation BI

## Project Overview

Project 5 is an in-progress business intelligence and analytics project that uses The Movie Database (TMDB) API to explore animated feature films released between 2000 and 2025.

The project demonstrates an end-to-end analytics workflow: API-based data collection, data cleaning and validation, relational data modeling, SQL analytics, and Power BI dashboard development.

The goal is to turn movie metadata into an organized analytical dataset and an interactive dashboard that helps users explore animation industry trends, audience ratings, popularity, production companies, countries, and available financial performance data.

**Project status: In progress.** The core dataset, MySQL analytical views, and Power BI dashboard have been developed. Final documentation, validation of SQL deliverables, and repository preparation remain in progress.

## Objectives

- Collect animation movie metadata through the TMDB API.
- Establish and apply consistent movie-selection criteria.
- Clean and validate movie and related dimension data.
- Organize movie, genre, production company, and country data in a relational MySQL database.
- Create reusable SQL analytical views.
- Build a Power BI dashboard that communicates trends and comparisons.
- Document data limitations and analytical assumptions.
- Demonstrate a reproducible analytics workflow suitable for a data analytics or BI portfolio.

## Data Source

This project uses the [TMDB API](https://developer.themoviedb.org/docs).

TMDB was selected because it provides movie metadata, audience ratings, popularity measures, release dates, genres, production companies, production countries, budgets, and revenues. These fields support several complementary analytical questions within one project.

### Movie Selection Criteria

The candidate dataset was created using the following criteria:

- **Genre:** Animation (TMDB genre ID `16`)
- **Release dates:** January 1, 2000 through December 31, 2025
- **Runtime:** At least 60 minutes
- **Vote count:** At least 100 votes
- **Adult entries:** Excluded
- **Video entries:** Excluded

The initial candidate discovery process prioritized popularity. These criteria define the project's selected movie population; findings should not be interpreted as representing every animated film ever produced.

### Candidate Dataset

File: `data/animation_movie_candidates.csv`

The candidate dataset contains **1,236 unique movie candidates**.

This is the discovery-stage dataset. The project also contains collected, cleaned, and analytical data files used to prepare the relational database and dashboard.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | API interaction, data collection, cleaning, validation, and dataset preparation |
| TMDB API | Movie metadata source |
| pandas | Data manipulation and preparation |
| MySQL | Relational storage and SQL analytics |
| MySQL Workbench | Database management and query execution |
| Power BI Desktop | Dashboard development and visualization |
| Git and GitHub | Version control and portfolio presentation |

## Workflow

The project follows this general workflow:

1. **Explore the API** — inspect available TMDB animation movie discovery and detail endpoints.
2. **Discover candidates** — collect movies using the established selection criteria.
3. **Inspect candidate data** — review the resulting CSV and validate the selected movie population.
4. **Collect movie details** — retrieve detailed information needed for analysis.
5. **Clean and validate data** — prepare movie records and related genre, company, and country data.
6. **Build the relational database** — organize the data in MySQL tables and relationship tables.
7. **Create analytical views** — define reusable SQL views for movie-level and aggregated analysis.
8. **Build the dashboard** — use the analytical data in Power BI to present industry trends and comparisons.
9. **Validate and document** — verify results, document assumptions, and prepare the project for portfolio review.

The project has progressed through the database and dashboard stages. Final validation and repository-readiness work remain in progress.

## Data Model

The MySQL database is named `animation_bi`.

The relational model separates movie records from their related dimensions and relationships.

### Core Tables

| Table | Purpose |
|---|---|
| `movies` | Movie-level metadata and analytical fields |
| `genres` | Genre reference data |
| `movie_genres` | Movie-to-genre relationships |
| `production_companies` | Production company reference data |
| `movie_companies` | Movie-to-company relationships |
| `production_countries` | Production country reference data |
| `movie_countries` | Movie-to-country relationships |

Staging tables are used during data preparation and import:

- `movies_staging`
- `genres_staging`
- `companies_staging`
- `countries_staging`

The staging tables support the import workflow; they are distinct from the core analytical tables.

## SQL Analytics

The main SQL script is `Project_5_Animation_BI.sql`.

It defines five analytical views using `CREATE OR REPLACE VIEW`.

| View | Purpose |
|---|---|
| `vw_movie_analysis` | Movie-level analytical fields, financial availability flags, profit, and revenue multiple |
| `vw_year_analysis` | Year-level movie counts, average ratings, popularity, vote counts, and financial metrics |
| `vw_genre_analysis` | Movie counts and average audience/popularity metrics by genre |
| `vw_company_analysis` | Movie counts and average metrics by production company |
| `vw_country_analysis` | Movie counts and average metrics by production country |

### Verified View Counts

The views were queried during project development in both the original database and the separate restore-test database. The following row counts were recorded:

| View | Rows |
|---|---:|
| `vw_movie_analysis` | 1,236 |
| `vw_year_analysis` | 26 |
| `vw_genre_analysis` | 19 |
| `vw_company_analysis` | 81 |
| `vw_country_analysis` | 50 |

The company analysis includes companies associated with at least 10 distinct movies.

### Analytical Measures

The project includes the following types of measures:

- Movie counts
- Average audience rating
- Average popularity
- Average vote count
- Financially eligible movie counts
- Average revenue
- Average budget
- Average profit
- Portfolio revenue multiple

Profit is calculated as:

`Profit = Revenue - Budget`

The revenue multiple is calculated as:

`Revenue Multiple = Revenue / Budget`

The revenue multiple is **not a formal return-on-investment measure**. It does not account for marketing, distribution, production financing, or other costs.

## Data Quality and Limitations

The project explicitly distinguishes missing financial information from a genuine value of zero.

### Financial Data

During preparation, zero values were treated as missing for these fields:

| Field | Zero values treated as missing |
|---|---:|
| Budget | 760 |
| Revenue | 514 |

Three records with a runtime of zero were also converted to missing runtime values.

Recorded financial availability counts:

| Measure | Movies |
|---|---:|
| Total movies | 1,236 |
| Budget available | 476 |
| Revenue available | 722 |
| Both budget and revenue available | 424 |

Profit and revenue multiple are calculated only for records with both budget and revenue available. Revenue multiple additionally requires a positive budget.

Missing financial values must not be interpreted as zero-dollar budgets or revenues.

### Other Limitations

- TMDB metadata and audience metrics can change over time.
- The 2025 release-year data may be incomplete because the collection period and available records may not cover every release.
- Movies can belong to multiple genres and have multiple production companies or countries. Aggregated category counts may therefore overlap.
- Popularity and vote counts reflect TMDB's data and are not direct measures of box-office success.
- Budget and revenue availability varies by movie, so financial analyses use smaller subsets than the full dataset.
- The selected criteria exclude short films and movies with fewer than 100 votes, limiting generalization beyond the selected population.

## Power BI Dashboard

File: `Project_5_Animation_BI_Dashboard.pbix`

The Power BI dashboard has been developed and opened successfully in Power BI Desktop. A refresh was performed successfully during development, and the visuals remained displayed.

The dashboard is organized into six analytical sections.

### 1. Industry Overview

High-level KPIs summarize the selected movie population.

Recorded KPI values:

| KPI | Value |
|---|---:|
| Total Movies | 1,236 |
| Average Rating | 6.99 |
| Average Popularity | 8.38 |
| Average Vote Count | Approximately 1,524 |

### 2. Year Trends

Explores how movie volume, audience ratings, popularity, vote counts, and available financial metrics vary by release year.

### 3. Genre Analysis

Compares animation genres by movie count and audience/popularity measures.

### 4. Production Companies

Examines production company representation and compares company-level movie and audience metrics. The company analysis uses the established minimum of 10 distinct movies.

### 5. Country Analysis

Explores the countries associated with the selected movies and compares movie counts and audience/popularity metrics.

### 6. Financial Performance

Examines available budget, revenue, profit, and revenue-multiple measures. Financial interpretations must account for the reduced number of movies with complete financial information.

The dashboard uses the SQL analytical views as its analytical foundation. The Power BI model includes a relationship between `vw_movie_analysis[release_year]` and `vw_year_analysis[release_year]`; the other analytical views remain disconnected in the current model.

**Dashboard status:** Built and refreshed during development. Final validation and documentation remain part of the unfinished project.

## Project Files

The following are the principal project files and folders. This list is not intended to inventory every file.

### Python Scripts

The project includes scripts for:

- Testing TMDB authentication and data retrieval
- Exploring animation movie discovery options
- Discovering movie candidates
- Collecting detailed movie information
- Inspecting candidate and movie-detail datasets
- Cleaning movie and dimension data
- Creating the analytical dataset and dimension files
- Checking data quality and anomalies
- Validating cleaned data and the data model
- Importing company and country data into MySQL
- Splitting company data into manageable files

These scripts support the collection, preparation, import, and validation stages. The presence of a script does not by itself establish that every execution or validation step is complete.

### SQL and Dashboard Files

- **`Project_5_Animation_BI.sql`** — primary SQL script defining the five analytical views.
- **`Project_5_Animation_BI_database_export.sql`** — MySQL Workbench database export containing database structures, data, and final view definitions. A separate restore test in `animation_bi_restore_test` successfully recreated the expected 11 tables and 5 analytical views, with the expected movie and view row counts. Restoration portability across different MySQL environments and the `root@localhost` view definer still require consideration.
- **`data/Project_5_Animation_BI_working_sql_workflow.sql`** — working SQL workflow containing import steps, validation queries, exploratory checks, and view definitions. It is not a standalone database backup.
- **`Project_5_Animation_BI_Dashboard.pbix`** — Power BI dashboard.
- **`README.md`** — project documentation.
- **`.gitignore`** — excludes local environment and generated development files from version control.

### Data Files

The `data/` directory contains the candidate dataset and other movie, genre, company, and country data files used during collection and preparation.

The principal discovery-stage dataset is:

`data/animation_movie_candidates.csv`

It contains 1,236 unique movie candidates.

## Security and Reproducibility

TMDB credentials are stored locally in `.env`. The environment file must not be committed to Git or published in the repository.

The `.gitignore` file excludes `.env`, `.venv/`, `__pycache__/`, and `.vs/`.

To reproduce the project, a user will need their own TMDB credentials, the appropriate Python environment and dependencies, a compatible MySQL installation, the prepared project data, and Power BI Desktop to open the dashboard.

Database export restoration was tested in a separate database named `animation_bi_restore_test`. The test confirmed the expected 11 tables, 5 views, 1,236 movie records, and recorded analytical view row counts. This is a structural and row-count validation, not an exhaustive comparison of every restored record or a guarantee of portability across different MySQL environments.

## Portfolio Context

Project 5 builds on the previous projects in the animation analytics portfolio:

- **Project 1 — Data Collection:** demonstrates collecting YouTube animation data through an API.
- **Project 2 — Performance Analytics:** explores performance measures and visualizations.
- **Project 3 — Title Strategy Analysis:** investigates patterns in animation video titles.
- **Project 4 — SQL Analytics:** demonstrates SQL-based analysis of YouTube animation data.
- **Project 5 — Animation BI:** extends the portfolio with TMDB movie data, a relational MySQL data model, reusable analytical views, and a Power BI dashboard.

Project 5 adds a more complete BI workflow and a different data source, expanding the portfolio beyond YouTube video performance analysis.

## Attribution

This product uses the TMDB API but is not endorsed or certified by TMDB.

## Current Status and Remaining Work

Project 5 is **unfinished and in progress**.

Completed development work includes the candidate dataset, core MySQL tables and analytical views, and the Power BI dashboard. The database views, key KPI counts, and a separate database restore test have been checked during development. The project files have also been committed to the local Git repository in commit `f86e02f` (`Add Project 5 Animation BI dashboard`), with a subsequent README status update in commit `23d187c`.

Remaining work includes:

- Reviewing the chronological working SQL workflow for clarity and reproducibility.
- Addressing any remaining portability concerns with the database export, including the view definer.
- Confirming that the README accurately reflects the final file structure and project state.
- Reviewing Git tracking and credential exclusions to ensure `.env` and unnecessary local files are not committed.
- Completing any necessary final corrections and committing those updates.

The project should not be considered complete until the remaining validation and documentation checks have been addressed.