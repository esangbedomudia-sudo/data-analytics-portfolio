# Project 4 — YouTube Animation SQL Analytics

## Overview

This project uses MySQL and SQL to analyze YouTube animation video data stored in a relational database.

Building on the dataset collected in Project 1, the project demonstrates how SQL can be used to explore records, aggregate performance metrics, compare content categories, evaluate channel performance, and rank videos using increasingly advanced queries.

Python is used to support the data import workflow, while MySQL provides the environment for database querying and analysis.

This project demonstrates practical database analytics techniques relevant to data analyst and business intelligence workflows.

## Objectives

The objectives of this project are to:

- Import the YouTube animation dataset into a MySQL database.
- Explore and query data stored in relational tables.
- Analyze video performance and audience engagement.
- Compare performance across animation content categories and channels.
- Apply aggregation, filtering, subqueries, joins, and window functions.
- Generate analytical summaries directly from the database.

## Tools & Technologies

- **SQL** — Querying, transforming, aggregating, and analyzing data.
- **MySQL** — Relational database management system.
- **MySQL Workbench** — Database interaction and SQL query development.
- **Python** — Supporting the data import workflow.
- **Pandas** — Handling and preparing tabular data during import.

## Analysis Performed

### Dataset Exploration

Queries the database to inspect records, filter data, sort results, and examine the structure and contents of the dataset.

### Video Performance Analysis

Examines video-level performance metrics to identify high-performing videos and compare observed results.

### Content Category Analysis

Groups videos by animation-related content category to summarize and compare performance metrics across categories.

### Channel Performance Analysis

Aggregates and compares video performance by channel to explore differences in the collected dataset.

### Engagement Analysis

Uses calculated metrics and conditional logic to examine audience engagement and distinguish between different performance levels.

### Ranking Analysis

Applies SQL ranking techniques to compare videos within relevant groups and identify top-performing records.

These analyses describe patterns in the available dataset and do not establish that any particular category, channel, or characteristic causes higher performance.

## SQL Concepts Demonstrated

The project applies SQL techniques ranging from foundational queries to more advanced analytical operations.

### Core Querying

- `SELECT`
- `WHERE`
- `ORDER BY`

### Aggregation and Grouping

- `GROUP BY`
- `HAVING`
- Aggregate functions such as `COUNT()`, `AVG()`, `SUM()`, `MIN()`, and `MAX()`

### Conditional Logic and Derived Results

- `CASE` statements
- Calculated metrics
- Subqueries and derived tables

### Relational Querying

- `JOIN` operations
- Combining and analyzing related query results

### Window Functions and Ranking

- `ROW_NUMBER()`
- `RANK()`
- Window functions for ordering and ranking records within defined groups

Together, these techniques demonstrate how SQL can be used to retrieve, summarize, compare, and rank data for analytical reporting.

## Project Files

### `sql/`

Contains the primary SQL script:

- `youtube_animation_analytics.sql` — Contains the SQL queries used to explore the dataset and perform performance, category, engagement, channel, and ranking analyses.

### `src/`

Contains the Python helper script:

- `sql_import.py` — Supports preparing and importing the dataset into MySQL for database analysis.

## Skills Demonstrated

- SQL query development
- MySQL database querying
- Relational database concepts
- Data exploration and filtering
- Aggregation and grouped reporting
- Conditional logic with `CASE`
- Subqueries and derived tables
- Joins
- Window functions and ranking
- Performance and engagement analysis
- Python-assisted data import
- Analytical problem-solving

## Connection to Other Projects

This project builds on **Project 1 — YouTube Animation Data Collection**, which establishes the dataset used throughout the portfolio.

It complements:

- **Project 2 — YouTube Animation Performance Analytics**, which uses Python to explore video performance, engagement, and content categories.
- **Project 3 — YouTube Animation Title Strategy Analysis**, which investigates title keywords and their relationship to video views.

Project 4 approaches the data from a database perspective, demonstrating how SQL can be used to perform similar and additional analyses within MySQL.

Together, these projects demonstrate a workflow spanning data collection, Python-based analysis, text analysis, and relational database analytics.