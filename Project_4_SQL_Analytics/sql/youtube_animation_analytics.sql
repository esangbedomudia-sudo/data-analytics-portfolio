
/*
=========================================================
Project 4: YouTube Animation SQL Analytics

Author: Ose Esangbedo

Database: youtube_animation_analytics
Table: youtube_videos

Project Objective:
Analyze YouTube animation videos to identify trends in
video performance, audience engagement, category success,
and channel performance using SQL.

Business Questions:
1. Which animation categories receive the highest views?
2. Which categories have the strongest engagement?
3. Which videos outperform their category averages?
4. Which channels perform well across multiple videos?
5. Which videos rank highest within each category?

SQL Concepts Demonstrated:
- SELECT, WHERE, ORDER BY, LIMIT
- Aggregate Functions
- GROUP BY and HAVING
- CASE Statements
- Subqueries and Derived Tables
- Window Functions
- ROW_NUMBER() and RANK()

=========================================================
*/

USE youtube_animation_analytics;


/*
=========================================================
SECTION 1: DATASET EXPLORATION
=========================================================
*/


/*
Business Question:
How many videos are included in the dataset?
*/

SELECT
    COUNT(*) AS total_videos
FROM youtube_videos;


/*
Business Question:
How many unique animation categories are represented?
*/

SELECT
    COUNT(DISTINCT search_query) AS total_categories
FROM youtube_videos;


/*
Business Question:
How many unique YouTube channels are represented?
*/

SELECT
    COUNT(DISTINCT channel) AS total_channels
FROM youtube_videos;


/*
Business Question:
How are videos distributed across categories?
*/

SELECT
    search_query,
    COUNT(*) AS total_videos
FROM youtube_videos
GROUP BY search_query
ORDER BY total_videos DESC;


/*
=========================================================
SECTION 2: CATEGORY PERFORMANCE ANALYSIS
=========================================================
*/


/*
Business Question:
Which categories have the highest average views?
*/

SELECT
    search_query,
    COUNT(*) AS total_videos,
    ROUND(AVG(views), 2) AS average_views
FROM youtube_videos
GROUP BY search_query
ORDER BY average_views DESC;


/*
Business Question:
Which categories have the strongest average like rate?

Metric:
Like Rate = Likes / Views

Videos with zero views are excluded from the rate
calculation to avoid division by zero.
*/

SELECT
    search_query,
    COUNT(*) AS total_videos,
    ROUND(
        AVG(likes / NULLIF(views, 0)),
        4
    ) AS average_like_rate
FROM youtube_videos
GROUP BY search_query
ORDER BY average_like_rate DESC;


/*
Business Question:
Which categories have the highest percentage of videos
with a like rate of at least 5%?

Videos with zero views are excluded from the percentage
denominator because their like rate cannot be calculated.
*/

SELECT
    search_query,
    COUNT(
        CASE
            WHEN views > 0 THEN 1
        END
    ) AS videos_with_valid_view_counts,

    SUM(
        CASE
            WHEN views > 0
             AND likes / NULLIF(views, 0) >= 0.05
            THEN 1
            ELSE 0
        END
    ) AS high_engagement_videos,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN views > 0
                 AND likes / NULLIF(views, 0) >= 0.05
                THEN 1
                ELSE 0
            END
        ) / NULLIF(
            COUNT(
                CASE
                    WHEN views > 0 THEN 1
                END
            ),
            0
        ),
        2
    ) AS high_engagement_percentage

FROM youtube_videos
GROUP BY search_query
ORDER BY high_engagement_percentage DESC;


/*
Business Question:
How many videos exceed their own category's average
view count?
*/

SELECT
    search_query,
    COUNT(*) AS videos_above_category_average
FROM
(
    SELECT
        search_query,
        views,
        AVG(views) OVER (
            PARTITION BY search_query
        ) AS category_average
    FROM youtube_videos
) AS category_performance
WHERE views > category_average
GROUP BY search_query
ORDER BY videos_above_category_average DESC;


/*
=========================================================
SECTION 3: VIDEO PERFORMANCE ANALYSIS
=========================================================
*/


/*
Business Question:
Which individual videos have the highest view counts?
*/

SELECT
    title,
    channel,
    search_query,
    views
FROM youtube_videos
ORDER BY views DESC
LIMIT 10;


/*
Business Question:
Which videos exceed the overall dataset's average
view count?
*/

SELECT
    title,
    channel,
    search_query,
    views
FROM youtube_videos
WHERE views > (
    SELECT AVG(views)
    FROM youtube_videos
)
ORDER BY views DESC;


/*
Business Question:
Which videos exceed their own category's average
view count?
*/

SELECT
    title,
    channel,
    search_query,
    views,
    category_average
FROM
(
    SELECT
        title,
        channel,
        search_query,
        views,
        AVG(views) OVER (
            PARTITION BY search_query
        ) AS category_average
    FROM youtube_videos
) AS category_comparison
WHERE views > category_average
ORDER BY search_query, views DESC;


/*
Business Question:
What are the top three videos in each category?

ROW_NUMBER() assigns each video a unique position
within its category.
*/

SELECT
    title,
    channel,
    search_query,
    views,
    category_rank
FROM
(
    SELECT
        title,
        channel,
        search_query,
        views,
        ROW_NUMBER() OVER (
            PARTITION BY search_query
            ORDER BY views DESC, video_id
        ) AS category_rank
    FROM youtube_videos
) AS ranked_videos
WHERE category_rank <= 3
ORDER BY search_query, category_rank;


/*
=========================================================
SECTION 4: CHANNEL PERFORMANCE ANALYSIS
=========================================================
*/


/*
Business Question:
Which channels appear most frequently in the dataset?
*/

SELECT
    channel,
    COUNT(*) AS total_videos
FROM youtube_videos
GROUP BY channel
ORDER BY total_videos DESC;


/*
Business Question:
Which channels with multiple videos have the highest
average view counts?
*/

SELECT
    channel,
    COUNT(*) AS total_videos,
    ROUND(AVG(views), 2) AS average_views
FROM youtube_videos
GROUP BY channel
HAVING COUNT(*) > 1
ORDER BY average_views DESC;


/*
Business Question:
Which channels have the most videos above the overall
dataset's average view count?
*/

SELECT
    channel,
    COUNT(*) AS above_average_videos
FROM
(
    SELECT
        channel,
        views,
        AVG(views) OVER () AS overall_average
    FROM youtube_videos
) AS channel_performance
WHERE views > overall_average
GROUP BY channel
ORDER BY above_average_videos DESC;


/*
=========================================================
SECTION 5: ADVANCED SQL ANALYSIS
=========================================================
*/


/*
Business Question:
How do ROW_NUMBER() and RANK() differ when ranking
videos within each category?

ROW_NUMBER() assigns a unique position to each row.
RANK() gives tied values the same rank and leaves gaps
in subsequent ranking positions.
*/

SELECT
    title,
    channel,
    search_query,
    views,

    ROW_NUMBER() OVER (
        PARTITION BY search_query
        ORDER BY views DESC, video_id
    ) AS row_number_rank,

    RANK() OVER (
        PARTITION BY search_query
        ORDER BY views DESC
    ) AS rank_position

FROM youtube_videos
ORDER BY search_query, views DESC;


/*
Business Question:
Which videos rank in the top three positions per
category when tied view counts share the same rank?

Unlike ROW_NUMBER(), RANK() can return more than
three videos in a category if there are ties.
*/

SELECT
    title,
    channel,
    search_query,
    views,
    category_rank
FROM
(
    SELECT
        title,
        channel,
        search_query,
        views,
        RANK() OVER (
            PARTITION BY search_query
            ORDER BY views DESC
        ) AS category_rank
    FROM youtube_videos
) AS ranked_categories
WHERE category_rank <= 3
ORDER BY search_query, category_rank, views DESC;


/*
=========================================================
SECTION 6: PROJECT VALIDATION
=========================================================
*/


/*
Business Question:
How many records and unique video IDs exist in the table?

The counts should match if each video ID is unique.
*/

SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT video_id) AS unique_video_ids
FROM youtube_videos;


/*
Business Question:
Are there any records with missing video IDs?
*/

SELECT
    COUNT(*) AS missing_video_ids
FROM youtube_videos
WHERE video_id IS NULL;


/*
=========================================================
PROJECT SUMMARY
=========================================================

This project demonstrates how SQL can be used to:

1. Explore dataset size and category distribution.
2. Compare average views across animation categories.
3. Calculate audience like rates and engagement thresholds.
4. Benchmark individual videos against category averages.
5. Rank videos within categories using window functions.
6. Compare channel upload volume and average performance.
7. Validate record counts and video ID uniqueness.

Interpretation Note:
Analytical findings should be based on the actual query
results. Category and channel performance in this dataset
does not, by itself, establish causation or guarantee
future performance.

Data Source:
youtube_animation_data_expanded.csv

Database:
youtube_animation_analytics

Table:
youtube_videos

=========================================================
END OF PROJECT
=========================================================
*/
