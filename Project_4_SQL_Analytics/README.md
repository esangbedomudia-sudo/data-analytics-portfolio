
# Project 4 — YouTube Animation SQL Analytics

## Overview

This project uses MySQL and SQL to analyze YouTube animation video data stored in a relational database.

Building on the dataset collected in Project 1, this project demonstrates how SQL can be used to explore data, aggregate performance metrics, compare animation categories, evaluate channel performance, and rank videos using analytical queries.

Python supports the database import workflow, while MySQL provides the environment for querying and analyzing the data.

The project demonstrates practical SQL techniques relevant to data analytics and business intelligence workflows.

## Objectives

The objectives of this project are to:

- Import the YouTube animation dataset into a MySQL database.
- Explore and query records stored in a relational table.
- Analyze video performance and audience engagement.
- Compare performance across animation categories and channels.
- Apply aggregation, filtering, conditional logic, subqueries, and window functions.
- Identify high-performing videos using overall and category-level benchmarks.
- Validate record counts and video ID uniqueness.

## Tools & Technologies

- **SQL** — Querying, aggregating, filtering, and analyzing data.
- **MySQL** — Relational database management system.
- **MySQL Workbench** — Database interaction and SQL query development.
- **Python** — Supporting the database import workflow.
- **Python CSV module** — Reading the dataset from a CSV file for import into MySQL.
- **Git and GitHub** — Version control and project hosting.

## Dataset

The project uses the expanded YouTube animation dataset created in Project 1.

- **Source file:** `youtube_animation_data_expanded.csv`
- **Database:** `youtube_animation_analytics`
- **Table:** `youtube_videos`
- **Records:** 141 video records
- **Unique video IDs:** 141

The dataset contains video information such as titles, channels, publication dates, views, likes, comments, and calculated performance metrics.

The analysis reflects the records collected for this project and should not be interpreted as a complete representation of all YouTube animation content.

## Analysis Performed

### 1. Dataset Exploration

- Count total video records.
- Identify the number of distinct animation categories and channels.
- Examine the distribution of videos across categories.
- Validate record counts and video ID uniqueness.

### 2. Category Performance Analysis

- Compare average views across animation categories.
- Calculate average like rates by category.
- Measure the percentage of videos meeting a defined engagement threshold.
- Count videos that exceed their category's average view count.

### 3. Video Performance Analysis

- Identify the ten videos with the highest view counts.
- Find videos exceeding the dataset's average views.
- Compare individual videos against their category averages.
- Rank the top three videos within each category using `ROW_NUMBER()`.

### 4. Channel Performance Analysis

- Count videos associated with each channel.
- Compare average views for channels represented by multiple videos.
- Identify channels with the highest counts of videos exceeding the overall average.

### 5. Advanced SQL Analysis

- Use subqueries and derived tables to organize analytical calculations.
- Apply window functions to calculate category and overall benchmarks.
- Compare `ROW_NUMBER()` and `RANK()` to understand different ranking behaviors.
- Handle zero-view records safely in engagement calculations using `NULLIF()`.

### Analytical Considerations

The like rate is calculated as:

`Like Rate = Likes / Views`

A 5% like rate is used as a defined threshold for the high-engagement analysis. This threshold is an analytical choice rather than a universal industry benchmark.

Category and channel comparisons describe patterns within the collected dataset. They do not establish causation or guarantee future performance.

## SQL Concepts Demonstrated

### Core Querying

- `SELECT`
- `WHERE`
- `ORDER BY`
- `LIMIT`

### Aggregation and Grouping

- `GROUP BY`
- `HAVING`
- `COUNT()`
- `AVG()`
- `SUM()`

### Conditional Logic and Calculated Metrics

- `CASE` statements
- Calculated engagement rates
- `NULLIF()` for safe division
- Conditional aggregation

### Subqueries and Derived Tables

- Scalar subqueries
- Derived tables in the `FROM` clause
- Comparisons against overall and category-level averages

### Window Functions and Ranking

- `AVG() OVER()`
- `PARTITION BY`
- `ROW_NUMBER()`
- `RANK()`

These techniques demonstrate how SQL can retrieve, summarize, compare, and rank data for analytical reporting.

## Project Structure

```text
Project_4_SQL_Analytics/
├── README.md
├── sql/
│   └── youtube_animation_analytics.sql
└── src/
    └── sql_import.py
```

### `sql/`

Contains `youtube_animation_analytics.sql`, the main SQL script for dataset exploration, category analysis, video performance, channel analysis, ranking, and validation.

### `src/`

Contains `sql_import.py`, the Python script that reads the shared CSV dataset and imports its records into the MySQL `youtube_videos` table.

The import script uses an upsert operation so that existing video IDs are updated instead of inserted as duplicate records.

## Skills Demonstrated

- SQL query development
- MySQL database querying
- Relational database fundamentals
- Data exploration and filtering
- Aggregation and grouped reporting
- Conditional logic and calculated metrics
- Subqueries and derived tables
- Window functions and ranking
- Performance benchmarking
- Engagement analysis
- Python-assisted data import
- Data validation
- Git version control

## Connection to Other Projects

This project builds on **Project 1 — YouTube Animation Data Collection**, which provides the dataset used throughout the portfolio.

It complements:

- **Project 2 — YouTube Animation Performance Analytics:** Uses Python to explore video performance, engagement, and category-level patterns.
- **Project 3 — YouTube Animation Title Strategy Analysis:** Investigates title keywords and their relationship to video views.

Project 4 approaches the dataset from a database perspective, demonstrating how SQL can perform structured analysis and comparisons within MySQL.

Together, these projects demonstrate a workflow spanning data collection, Python-based performance analysis, title analysis, and relational database analytics.

## Future Improvements

Potential extensions include:

- Add SQL joins when related tables become available.
- Create database views for reusable analytical queries.
- Develop additional metrics and more robust data quality checks.
- Connect the database to a BI dashboard for interactive reporting.

## Conclusion

Project 4 demonstrates how SQL and MySQL can be used to investigate video performance, compare animation categories, evaluate channels, and rank individual videos.

It provides a foundation for more advanced analytical work, including reusable database views, BI dashboards, and predictive modeling.
