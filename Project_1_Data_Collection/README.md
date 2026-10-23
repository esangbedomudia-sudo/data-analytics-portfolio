# Project 1 — YouTube Animation Data Collection

## Overview
This project collects and prepares YouTube video data related to animation using the YouTube Data API and Python. The resulting dataset supports the performance analysis, title strategy analysis, and SQL analytics developed in subsequent projects.

## Objective
Build a dataset of animation-related YouTube videos and prepare it for analysis by removing duplicate videos and creating additional analytical features.

## Tools & Technologies
- **Python** — Data collection and processing
- **YouTube Data API** — Retrieving video information and statistics
- **Pandas** — Data cleaning, transformation, and preparation

## Data Collected
The dataset includes:
- Video ID
- Search query
- Video title
- Channel name
- Publication date
- View count
- Like count
- Comment count

The expanded dataset also includes publication year, publication month, title length, total engagement, and engagement ratio.

## Workflow
1. Search YouTube for videos across six animation-related queries.
2. Retrieve video metadata and engagement statistics.
3. Combine the results into a single dataset.
4. Remove duplicate videos using video IDs.
5. Convert publication dates and derive additional analytical features.
6. Calculate total engagement and engagement ratio.
7. Export the prepared dataset to CSV.

## Project Files
- `youtube_project.py` — Python script for collecting and preparing YouTube data.
- `youtube_animation_data.csv` — Initial collected dataset.
- `youtube_animation_data_cleaned.csv` — Cleaned dataset.
- `youtube_animation_data_expanded.csv` — Expanded dataset containing additional analytical features.

## Skills Demonstrated
- API data collection
- Python scripting
- Data cleaning and deduplication
- Feature engineering
- Data transformation with Pandas
- CSV data management

## Connection to Other Projects
This project provides the YouTube animation dataset used in the subsequent portfolio projects:

- **Project 2 — Performance Analytics:** Examines video views and engagement.
- **Project 3 — Title Strategy Analysis:** Investigates title characteristics and performance.
- **Project 4 — SQL Analytics:** Uses SQL to analyze video performance and channel trends.

## Notes
The collected data reflects the results returned by the YouTube Data API when the collection script was run. Video statistics can change over time.
