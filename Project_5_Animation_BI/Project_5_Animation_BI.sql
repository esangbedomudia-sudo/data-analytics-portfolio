
-- ============================================================
-- Project 5: Animation Industry BI
-- Database: animation_bi
-- Purpose: Analytical views for Power BI reporting
--
-- Prerequisite:
-- The animation_bi database and its source tables must already
-- exist before these views are created.
-- ============================================================

USE animation_bi;

-- ============================================================
-- 1. Movie-level analysis
-- ============================================================

CREATE OR REPLACE VIEW vw_movie_analysis AS
SELECT
    m.movie_id,
    m.title,
    m.release_date,
    m.release_year,
    m.runtime,
    m.budget,
    m.revenue,
    m.vote_average,
    m.vote_count,
    m.popularity,
    m.original_language,
    m.budget_available,
    m.revenue_available,
    m.financials_available,
    CASE
        WHEN m.financials_available = 1
        THEN m.revenue - m.budget
        ELSE NULL
    END AS profit,
    CASE
        WHEN m.financials_available = 1
             AND m.budget > 0
        THEN m.revenue / m.budget
        ELSE NULL
    END AS revenue_multiple
FROM movies AS m;

-- ============================================================
-- 2. Year-level analysis
-- ============================================================

CREATE OR REPLACE VIEW vw_year_analysis AS
SELECT
    m.release_year,
    COUNT(*) AS movie_count,
    ROUND(AVG(m.vote_average), 2) AS avg_rating,
    ROUND(AVG(m.popularity), 2) AS avg_popularity,
    ROUND(AVG(m.vote_count), 0) AS avg_vote_count,
    SUM(m.financials_available) AS financial_movies,
    ROUND(
        AVG(
            CASE WHEN m.financials_available = 1
                 THEN m.revenue END
        ), 0
    ) AS avg_revenue,
    ROUND(
        AVG(
            CASE WHEN m.financials_available = 1
                 THEN m.budget END
        ), 0
    ) AS avg_budget,
    ROUND(
        AVG(
            CASE WHEN m.financials_available = 1
                 THEN m.revenue - m.budget END
        ), 0
    ) AS avg_profit,
    ROUND(
        SUM(
            CASE WHEN m.financials_available = 1
                 THEN m.revenue ELSE 0 END
        )
        /
        NULLIF(
            SUM(
                CASE WHEN m.financials_available = 1
                     THEN m.budget ELSE 0 END
            ), 0
        ), 2
    ) AS portfolio_revenue_multiple
FROM movies AS m
GROUP BY m.release_year;

-- ============================================================
-- 3. Genre-level analysis
-- ============================================================

CREATE OR REPLACE VIEW vw_genre_analysis AS
SELECT
    g.genre_id,
    g.genre_name,
    COUNT(DISTINCT mg.movie_id) AS movie_count,
    ROUND(AVG(m.vote_average), 2) AS avg_rating,
    ROUND(AVG(m.popularity), 2) AS avg_popularity,
    ROUND(AVG(m.vote_count), 0) AS avg_vote_count
FROM genres AS g
JOIN movie_genres AS mg
    ON g.genre_id = mg.genre_id
JOIN movies AS m
    ON mg.movie_id = m.movie_id
GROUP BY
    g.genre_id,
    g.genre_name;

-- ============================================================
-- 4. Production-company analysis
-- ============================================================

CREATE OR REPLACE VIEW vw_company_analysis AS
SELECT
    pc.company_name,
    COUNT(DISTINCT mc.movie_id) AS movie_count,
    ROUND(AVG(m.vote_average), 2) AS avg_rating,
    ROUND(AVG(m.popularity), 2) AS avg_popularity,
    ROUND(AVG(m.vote_count), 0) AS avg_vote_count
FROM production_companies AS pc
JOIN movie_companies AS mc
    ON pc.company_id = mc.company_id
JOIN movies AS m
    ON mc.movie_id = m.movie_id
GROUP BY pc.company_name
HAVING COUNT(DISTINCT mc.movie_id) >= 10;

-- ============================================================
-- 5. Production-country analysis
-- ============================================================

CREATE OR REPLACE VIEW vw_country_analysis AS
SELECT
    pc.country_code,
    pc.country_name,
    COUNT(DISTINCT mc.movie_id) AS movie_count,
    ROUND(AVG(m.vote_average), 2) AS avg_rating,
    ROUND(AVG(m.popularity), 2) AS avg_popularity,
    ROUND(AVG(m.vote_count), 0) AS avg_vote_count
FROM production_countries AS pc
JOIN movie_countries AS mc
    ON pc.country_code = mc.country_code
JOIN movies AS m
    ON mc.movie_id = m.movie_id
GROUP BY
    pc.country_code,
    pc.country_name;

-- ============================================================
-- End of Project 5 analytical view definitions
-- ============================================================
