# Project 3 — YouTube Animation Title Strategy Analysis

## Overview

This project analyzes the language used in YouTube animation video titles to explore relationships between title keywords and video performance.

Using the dataset collected in Project 1, the analysis applies text preprocessing and keyword analysis to examine word frequency and compare average video views associated with individual title terms.

The project introduces text-based analysis into the portfolio's analytics workflow, demonstrating how unstructured text can be processed and analyzed alongside numerical performance data to identify patterns in content positioning.

## Objectives

The objectives of this project are to:

- Clean and preprocess YouTube video titles.
- Extract and analyze individual words from titles.
- Identify frequently occurring title keywords.
- Compare average video views associated with different keywords.
- Explore relationships between title language and observed video performance.

## Tools & Technologies

- **Python** — Analysis scripting and workflow.
- **Pandas** — Data manipulation and analysis.
- **Regular Expressions (Regex)** — Text cleaning and preprocessing.
- **Matplotlib** — Data visualization.
- **CSV** — Source data format.

## Analysis Performed

### Title Preprocessing

Cleans video title text using lowercase conversion, regular expressions, and other preprocessing steps to prepare titles for analysis.

### Word Frequency Analysis

Examines the frequency of individual words across video titles to identify recurring terms and language patterns.

### Keyword Performance Analysis

Compares average video views associated with individual title keywords to explore how different terms relate to observed performance in the dataset.

### High-Performing Title Keywords

Identifies keywords associated with higher average view counts, providing a starting point for investigating patterns in animation video title strategies.

These findings describe associations within the collected dataset. They do not establish that using a particular keyword causes a video to receive more views.

## Visualization

### `title_word_performance.png`

Visualizes average video views associated with selected title keywords, making it easier to compare the observed performance of different terms.

## Project Files

### `src/`

Contains the primary analysis script:

- `title_analysis.py` — Processes video titles, analyzes word frequency and keyword performance, and generates the visualization.

### `visuals/`

Contains the generated visualization:

- `title_word_performance.png` — Compares average video views associated with selected title keywords.

## Skills Demonstrated

- Python programming
- Text preprocessing and cleaning
- Regular expressions (Regex)
- Pandas data manipulation
- Exploratory data analysis (EDA)
- Keyword and word frequency analysis
- Comparative performance analysis
- Data visualization with Matplotlib
- Analytical interpretation

## Connection to Other Projects

This project builds on the dataset collected in **Project 1 — YouTube Animation Data Collection** and complements **Project 2 — YouTube Animation Performance Analytics**.

While Project 2 examines broader video performance and engagement patterns, Project 3 focuses on title language and its relationship to video views.

Its text-based analytical approach complements **Project 4 — YouTube Animation SQL Analytics**, which explores video, category, engagement, and channel performance using SQL.

Together, these projects demonstrate multiple approaches to investigating YouTube animation data, from collection and performance analysis to text analysis and database querying.