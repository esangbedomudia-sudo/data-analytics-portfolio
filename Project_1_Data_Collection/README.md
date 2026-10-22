# Project 1 — YouTube Animation Data Collection

## Overview

This project collects and prepares YouTube animation video data for analysis using the YouTube Data API and Python.

The workflow transforms collected video information into structured datasets that support exploratory data analysis, visualization, and downstream analytics projects.

This project represents the data collection and preparation stage of a broader analytics portfolio focused on YouTube animation content and performance.

---

## Objective

The objectives of this project are to:

- Collect YouTube animation video data through API requests.
- Extract relevant video metadata and performance metrics.
- Organize collected information into structured datasets.
- Clean and prepare data for downstream analysis.
- Provide a reusable dataset for subsequent analytics projects.

---

## Tools & Technologies

- **Python** — Data collection and processing.
- **YouTube Data API** — Retrieving video information and statistics.
- **Pandas** — Data manipulation and preparation.
- **CSV** — Storing datasets at different processing stages.

---

## Data Collected

The dataset includes information about YouTube animation videos, such as:

- Video IDs
- Search query categories
- Video titles
- Channel names
- Publication dates
- View counts
- Like counts
- Comment counts
- Engagement metrics

The available fields depend on the data retrieved and prepared by the collection workflow.

---

## Workflow

1. Connect to the YouTube Data API.
2. Search for animation-related video content using relevant queries.
3. Collect video metadata and available performance statistics.
4. Clean and organize the collected information.
5. Export the data into CSV files for analysis.

The resulting datasets support subsequent performance analysis, title strategy analysis, and SQL-based analytics.

---

## Project Files

### `youtube_project.py`

The main Python script responsible for collecting YouTube animation data through API requests and preparing the datasets for analysis.

### `data/`

Contains three CSV datasets representing different stages of the data preparation workflow:

- **`youtube_animation_data_raw.csv`** — The initially collected dataset.
- **`youtube_animation_data_cleaned.csv`** — The dataset after cleaning and preparation.
- **`youtube_animation_data_expanded.csv`** — The expanded dataset prepared for downstream analysis.

These datasets provide the foundation for the related analytics projects in this portfolio.

---

## Skills Demonstrated

- Python programming
- API integration
- Data collection
- Data cleaning and preparation
- Pandas data manipulation
- CSV data management
- Structuring datasets for analysis

---

## Connection to Other Projects

This project establishes the data collection foundation for the portfolio's YouTube animation analytics workflow.

The resulting dataset is used in:

- **Project 2 — YouTube Animation Performance Analytics:** Investigates video views, engagement, and content performance patterns.
- **Project 3 — YouTube Animation Title Strategy Analysis:** Examines title language and its relationship to video performance.
- **Project 4 — YouTube Animation SQL Analytics:** Uses SQL to analyze video, category, engagement, and channel performance.

Together, these projects demonstrate a progression from data collection and preparation to analysis and database querying.