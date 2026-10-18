USE animation_bi;

INSERT INTO movie_genres (
    movie_id,
    genre_id
)
SELECT
    CAST(movie_id AS UNSIGNED),
    CAST(genre_id AS UNSIGNED)
FROM genres_staging;



USE animation_bi;

DESCRIBE production_companies;



USE animation_bi;

CREATE TABLE companies_staging (
    movie_id VARCHAR(50),
    company_id VARCHAR(50),
    company_name VARCHAR(255)
);


SELECT COUNT(*) AS row_count
FROM companies_staging;

SELECT *
FROM companies_staging
LIMIT 10;



SELECT *
FROM companies_staging
ORDER BY CAST(movie_id AS UNSIGNED) DESC
LIMIT 10;





SELECT *
FROM companies_staging
ORDER BY CAST(movie_id AS UNSIGNED) DESC
LIMIT 10;



SELECT COUNT(DISTINCT movie_id) AS movie_count
FROM companies_staging;



TRUNCATE TABLE companies_staging;



USE animation_bi;

TRUNCATE TABLE companies_staging;



USE animation_bi;

LOAD DATA LOCAL INFILE 'C:/Prog/Portfolio_Projects/youtube-animation-analysis/Project_5_Animation_BI/data/animation_movie_companies_cleaned.csv'
INTO TABLE companies_staging
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(movie_id, company_id, company_name);


USE animation_bi;

SELECT COUNT(*) AS row_count
FROM companies_staging;


SELECT *
FROM companies_staging
ORDER BY CAST(movie_id AS UNSIGNED) DESC
LIMIT 10;




SELECT COUNT(*) AS total_rows
FROM companies_staging;





SELECT COUNT(DISTINCT movie_id) AS distinct_movies
FROM companies_staging;



SHOW VARIABLES LIKE 'local_infile';

SET GLOBAL local_infile = 1;


TRUNCATE TABLE companies_staging;




LOAD DATA LOCAL INFILE 'C:/Prog/Portfolio_Projects/youtube-animation-analysis/Project_5_Animation_BI/data/animation_movie_companies_cleaned.csv'
INTO TABLE companies_staging
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(movie_id, company_id, company_name);


USE animation_bi;

SELECT COUNT(*) AS total_rows
FROM companies_staging;


DESCRIBE production_companies;



INSERT INTO production_companies (
    company_id,
    company_name
)
SELECT DISTINCT
    CAST(company_id AS UNSIGNED),
    company_name
FROM companies_staging;


DESCRIBE movies_companies;


SHOW TABLES;


DESCRIBE movie_companies;




INSERT INTO movie_companies (
    movie_id,
    company_id
)
SELECT
    CAST(movie_id AS UNSIGNED),
    CAST(company_id AS UNSIGNED)
FROM companies_staging;



DESCRIBE movie_countries;



DESCRIBE production_countries;




SELECT COUNT(*) AS total_rows
FROM movie_countries;


SHOW TABLES LIKE 'countries_staging';


USE animation_bi;

CREATE TABLE countries_staging (
    movie_id VARCHAR(50),
    country_code CHAR(2),
    country_name VARCHAR(100)
);


SELECT COUNT(*) AS total_rows
FROM countries_staging;


INSERT INTO production_countries (
    country_code,
    country_name
)
SELECT DISTINCT
    country_code,
    country_name
FROM countries_staging;









INSERT INTO movie_countries (
    movie_id,
    country_code
)
SELECT
    CAST(movie_id AS UNSIGNED),
    country_code
FROM countries_staging;




SELECT COUNT(*) AS total_rows
FROM movie_countries;





SELECT
    movie_id,
    country_code,
    COUNT(*) AS duplicate_count
FROM movie_countries
GROUP BY
    movie_id,
    country_code
HAVING COUNT(*) > 1;





SELECT COUNT(*) AS orphan_movie_relationships
FROM movie_countries mc
LEFT JOIN movies m
    ON mc.movie_id = m.movie_id
WHERE m.movie_id IS NULL;






SELECT 'movies' AS table_name, COUNT(*) AS row_count
FROM movies

UNION ALL

SELECT 'genres', COUNT(*)
FROM genres

UNION ALL

SELECT 'movie_genres', COUNT(*)
FROM movie_genres

UNION ALL

SELECT 'production_companies', COUNT(*)
FROM production_companies

UNION ALL

SELECT 'movie_companies', COUNT(*)
FROM movie_companies

UNION ALL

SELECT 'production_countries', COUNT(*)
FROM production_countries

UNION ALL

SELECT 'movie_countries', COUNT(*)
FROM movie_countries;




SELECT
    COUNT(*) AS total_movies,
    ROUND(AVG(vote_average), 2) AS avg_rating,
    ROUND(AVG(vote_count), 0) AS avg_vote_count,
    ROUND(AVG(popularity), 2) AS avg_popularity,
    ROUND(AVG(runtime), 1) AS avg_runtime,
    SUM(financials_available) AS movies_with_financials
FROM movies;








SELECT
    release_year,
    COUNT(*) AS movie_count,
    ROUND(AVG(vote_average), 2) AS avg_rating,
    ROUND(AVG(popularity), 2) AS avg_popularity,
    ROUND(AVG(vote_count), 0) AS avg_vote_count
FROM movies
GROUP BY release_year
ORDER BY release_year;










SELECT
    g.genre_name,
    COUNT(DISTINCT mg.movie_id) AS movie_count,
    ROUND(AVG(m.vote_average), 2) AS avg_rating,
    ROUND(AVG(m.popularity), 2) AS avg_popularity,
    ROUND(AVG(m.vote_count), 0) AS avg_vote_count
FROM genres g
JOIN movie_genres mg
    ON g.genre_id = mg.genre_id
JOIN movies m
    ON mg.movie_id = m.movie_id
GROUP BY
    g.genre_id,
    g.genre_name
ORDER BY
    movie_count DESC;
    
    
    
    
    
    
    
    
    
    SELECT
    pc.company_name,
    COUNT(DISTINCT mc.movie_id) AS movie_count,
    ROUND(AVG(m.vote_average), 2) AS avg_rating,
    ROUND(AVG(m.popularity), 2) AS avg_popularity,
    ROUND(AVG(m.vote_count), 0) AS avg_vote_count
FROM production_companies pc
JOIN movie_companies mc
    ON pc.company_id = mc.company_id
JOIN movies m
    ON mc.movie_id = m.movie_id
GROUP BY
    pc.company_id,
    pc.company_name
HAVING COUNT(DISTINCT mc.movie_id) >= 5
ORDER BY
    movie_count DESC,
    avg_rating DESC;
    
    
    
    
    
    
    
    
    
    
    
    SELECT
    pc.company_id,
    pc.company_name,
    COUNT(DISTINCT mc.movie_id) AS movie_count
FROM production_companies pc
JOIN movie_companies mc
    ON pc.company_id = mc.company_id
WHERE pc.company_name = 'The LEGO Group'
GROUP BY
    pc.company_id,
    pc.company_name
ORDER BY
    movie_count DESC;
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    SELECT
    pc.company_id,
    pc.company_name,
    m.movie_id,
    m.title,
    m.release_year
FROM production_companies pc
JOIN movie_companies mc
    ON pc.company_id = mc.company_id
JOIN movies m
    ON mc.movie_id = m.movie_id
WHERE pc.company_name = 'The LEGO Group'
ORDER BY
    pc.company_id,
    m.release_year,
    m.title;
    
    
    
    
    
    
    
    
    
SELECT
    company_name,
    COUNT(DISTINCT company_id) AS company_id_count,
    SUM(movie_count) AS total_movies
FROM (
    SELECT
        pc.company_id,
        pc.company_name,
        COUNT(DISTINCT mc.movie_id) AS movie_count
    FROM production_companies pc
    JOIN movie_companies mc
        ON pc.company_id = mc.company_id
    GROUP BY
        pc.company_id,
        pc.company_name
) AS company_counts
GROUP BY
    company_name
HAVING COUNT(DISTINCT company_id) > 1
ORDER BY
    company_id_count DESC,
    total_movies DESC;
    
    
    
    
    
    
    
    
    
SELECT
    pc.company_name,
    COUNT(DISTINCT mc.movie_id) AS movie_count,
    ROUND(AVG(m.vote_average), 2) AS avg_rating,
    ROUND(AVG(m.popularity), 2) AS avg_popularity,
    ROUND(AVG(m.vote_count), 0) AS avg_vote_count
FROM production_companies pc
JOIN movie_companies mc
    ON pc.company_id = mc.company_id
JOIN movies m
    ON mc.movie_id = m.movie_id
GROUP BY
    pc.company_name
HAVING COUNT(DISTINCT mc.movie_id) >= 5
ORDER BY
    movie_count DESC,
    avg_rating DESC;
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    SELECT
    COUNT(*) AS companies_5_plus,
    SUM(CASE WHEN movie_count >= 10 THEN 1 ELSE 0 END) AS companies_10_plus,
    SUM(CASE WHEN movie_count >= 15 THEN 1 ELSE 0 END) AS companies_15_plus,
    SUM(CASE WHEN movie_count >= 20 THEN 1 ELSE 0 END) AS companies_20_plus
FROM (
    SELECT
        pc.company_name,
        COUNT(DISTINCT mc.movie_id) AS movie_count
    FROM production_companies pc
    JOIN movie_companies mc
        ON pc.company_id = mc.company_id
    GROUP BY
        pc.company_name
) AS company_counts
WHERE movie_count >= 5;








SELECT
    pc.company_name,
    COUNT(DISTINCT mc.movie_id) AS movie_count,
    ROUND(AVG(m.vote_average), 2) AS avg_rating,
    ROUND(AVG(m.popularity), 2) AS avg_popularity,
    ROUND(AVG(m.vote_count), 0) AS avg_vote_count
FROM production_companies pc
JOIN movie_companies mc
    ON pc.company_id = mc.company_id
JOIN movies m
    ON mc.movie_id = m.movie_id
GROUP BY
    pc.company_name
HAVING COUNT(DISTINCT mc.movie_id) >= 10
ORDER BY
    avg_popularity DESC;
    
    
    
    
    
    
    
    
    
    
    
    
    
    SELECT
    pc.company_name,
    COUNT(DISTINCT mc.movie_id) AS movie_count,
    ROUND(AVG(m.vote_average), 2) AS avg_rating,
    ROUND(AVG(m.popularity), 2) AS avg_popularity,
    ROUND(AVG(m.vote_count), 0) AS avg_vote_count
FROM production_companies pc
JOIN movie_companies mc
    ON pc.company_id = mc.company_id
JOIN movies m
    ON mc.movie_id = m.movie_id
GROUP BY
    pc.company_name
HAVING COUNT(DISTINCT mc.movie_id) >= 10
ORDER BY
    avg_rating DESC;
    
    
    
    
    SELECT
    release_year,
    COUNT(*) AS movie_count,
    SUM(budget_available) AS budget_available,
    SUM(revenue_available) AS revenue_available,
    SUM(financials_available) AS both_financials_available
FROM movies
GROUP BY
    release_year
ORDER BY
    release_year;
    
    
    
    SELECT
    COUNT(*) AS financial_movies,
    ROUND(SUM(budget), 0) AS total_budget,
    ROUND(SUM(revenue), 0) AS total_revenue,
    ROUND(SUM(revenue - budget), 0) AS total_profit,
    ROUND(AVG(budget), 0) AS avg_budget,
    ROUND(AVG(revenue), 0) AS avg_revenue,
    ROUND(AVG(revenue - budget), 0) AS avg_profit
FROM movies
WHERE financials_available = 1;




SELECT
    release_year,
    COUNT(*) AS financial_movies,
    ROUND(AVG(budget), 0) AS avg_budget,
    ROUND(AVG(revenue), 0) AS avg_revenue,
    ROUND(AVG(revenue - budget), 0) AS avg_profit,
    ROUND(SUM(revenue - budget), 0) AS total_profit
FROM movies
WHERE financials_available = 1
GROUP BY release_year
ORDER BY release_year;






SELECT
    release_year,
    COUNT(*) AS financial_movies,
    ROUND(AVG(revenue / NULLIF(budget, 0)), 2) AS avg_revenue_multiple,
    ROUND(
        SUM(revenue) / NULLIF(SUM(budget), 0),
        2
    ) AS portfolio_revenue_multiple
FROM movies
WHERE financials_available = 1
GROUP BY release_year
ORDER BY release_year;

SELECT
    pc.company_name,
    COUNT(DISTINCT mc.movie_id) AS movie_count,
    ROUND(AVG(m.budget), 0) AS avg_budget,
    ROUND(AVG(m.revenue), 0) AS avg_revenue,
    ROUND(AVG(m.revenue - m.budget), 0) AS avg_profit,
    ROUND(
        SUM(m.revenue) / NULLIF(SUM(m.budget), 0),
        2
    ) AS portfolio_revenue_multiple
FROM production_companies pc
JOIN movie_companies mc
    ON pc.company_id = mc.company_id
JOIN movies m
    ON mc.movie_id = m.movie_id
WHERE m.financials_available = 1
GROUP BY pc.company_name
HAVING COUNT(DISTINCT mc.movie_id) >= 10
ORDER BY portfolio_revenue_multiple DESC;



SELECT
    pc.company_name,
    COUNT(DISTINCT mc.movie_id) AS movie_count,
    ROUND(AVG(m.vote_average), 2) AS avg_rating,
    ROUND(AVG(m.popularity), 2) AS avg_popularity,
    ROUND(
        SUM(m.revenue) / NULLIF(SUM(m.budget), 0),
        2
    ) AS portfolio_revenue_multiple
FROM production_companies pc
JOIN movie_companies mc
    ON pc.company_id = mc.company_id
JOIN movies m
    ON mc.movie_id = m.movie_id
WHERE m.financials_available = 1
GROUP BY pc.company_name
HAVING COUNT(DISTINCT mc.movie_id) >= 10
ORDER BY avg_popularity DESC;



SELECT
    m.movie_id,
    m.title,
    m.release_year,
    m.budget,
    m.revenue,
    (m.revenue - m.budget) AS profit,
    ROUND(m.revenue / NULLIF(m.budget, 0), 2) AS revenue_multiple,
    m.vote_average,
    m.vote_count,
    m.popularity
FROM movies m
WHERE m.financials_available = 1
ORDER BY m.revenue DESC
LIMIT 20;

SELECT
    m.movie_id,
    m.title,
    m.release_year,
    m.budget,
    m.revenue,
    (m.revenue - m.budget) AS profit,
    ROUND(m.revenue / NULLIF(m.budget, 0), 2) AS revenue_multiple,
    m.vote_average,
    m.vote_count,
    m.popularity
FROM movies m
WHERE m.financials_available = 1
  AND m.revenue < m.budget
ORDER BY revenue_multiple ASC
LIMIT 20;



USE animation_bi;

SHOW TABLES;



SELECT
    COUNT(*) AS movie_count,
    COUNT(DISTINCT movie_id) AS distinct_movies
FROM movie_genres;



SELECT
    COUNT(*) AS company_relationships,
    COUNT(DISTINCT movie_id) AS distinct_movies,
    COUNT(DISTINCT company_id) AS distinct_companies
FROM movie_companies;



SELECT
    COUNT(*) AS country_relationships,
    COUNT(DISTINCT movie_id) AS distinct_movies,
    COUNT(DISTINCT country_code) AS distinct_countries
FROM movie_countries;




SELECT
    COUNT(*) AS total_movies,
    COUNT(DISTINCT movie_id) AS distinct_movie_ids
FROM movies;


id="n2x581"
SHOW FULL TABLES IN animation_bi WHERE TABLE_TYPE = 'VIEW';



SHOW FULL TABLES IN animation_bi WHERE TABLE_TYPE = 'VIEW';


CREATE VIEW vw_movie_analysis AS
SELECT
    movie_id,
    title,
    release_date,
    release_year,
    runtime,
    budget,
    revenue,
    vote_average,
    vote_count,
    popularity,
    original_language,
    budget_available,
    revenue_available,
    financials_available,

    CASE
        WHEN financials_available = 1
        THEN revenue - budget
        ELSE NULL
    END AS profit,

    CASE
        WHEN financials_available = 1
             AND budget > 0
        THEN revenue / budget
        ELSE NULL
    END AS revenue_multiple

FROM movies;




SELECT
    COUNT(*) AS total_movies,
    COUNT(DISTINCT movie_id) AS distinct_movie_ids,
    COUNT(profit) AS movies_with_profit,
    COUNT(revenue_multiple) AS movies_with_revenue_multiple
FROM vw_movie_analysis;



SELECT
    title,
    budget,
    revenue,
    profit,
    revenue_multiple
FROM vw_movie_analysis
WHERE title IN (
    'Ne Zha 2',
    'Pixar'
)
ORDER BY revenue DESC;



DESCRIBE vw_movie_analysis;



CREATE VIEW vw_genre_analysis AS
SELECT
    g.genre_id,
    g.genre_name,
    COUNT(DISTINCT mg.movie_id) AS movie_count,
    ROUND(AVG(m.vote_average), 2) AS avg_rating,
    ROUND(AVG(m.popularity), 2) AS avg_popularity,
    ROUND(AVG(m.vote_count), 0) AS avg_vote_count
FROM genres g
JOIN movie_genres mg
    ON g.genre_id = mg.genre_id
JOIN movies m
    ON mg.movie_id = m.movie_id
GROUP BY
    g.genre_id,
    g.genre_name;
    
    
    
    SELECT
    COUNT(*) AS genre_count,
    COUNT(DISTINCT genre_id) AS distinct_genres
FROM vw_genre_analysis;

CREATE VIEW vw_company_analysis AS
SELECT
    pc.company_name,
    COUNT(DISTINCT mc.movie_id) AS movie_count,
    ROUND(AVG(m.vote_average), 2) AS avg_rating,
    ROUND(AVG(m.popularity), 2) AS avg_popularity,
    ROUND(AVG(m.vote_count), 0) AS avg_vote_count
FROM production_companies pc
JOIN movie_companies mc
    ON pc.company_id = mc.company_id
JOIN movies m
    ON mc.movie_id = m.movie_id
GROUP BY
    pc.company_name
HAVING COUNT(DISTINCT mc.movie_id) >= 10;



SELECT
    COUNT(*) AS company_count,
    COUNT(DISTINCT company_name) AS distinct_companies
FROM vw_company_analysis;





CREATE VIEW vw_country_analysis AS
SELECT
    pc.country_code,
    pc.country_name,
    COUNT(DISTINCT mc.movie_id) AS movie_count,
    ROUND(AVG(m.vote_average), 2) AS avg_rating,
    ROUND(AVG(m.popularity), 2) AS avg_popularity,
    ROUND(AVG(m.vote_count), 0) AS avg_vote_count
FROM production_countries pc
JOIN movie_countries mc
    ON pc.country_code = mc.country_code
JOIN movies m
    ON mc.movie_id = m.movie_id
GROUP BY
    pc.country_code,
    pc.country_name;
    
    SELECT
    COUNT(*) AS country_count,
    COUNT(DISTINCT country_code) AS distinct_countries
FROM vw_country_analysis;

CREATE VIEW vw_year_analysis AS
SELECT
    release_year,
    COUNT(*) AS movie_count,
    ROUND(AVG(vote_average), 2) AS avg_rating,
    ROUND(AVG(popularity), 2) AS avg_popularity,
    ROUND(AVG(vote_count), 0) AS avg_vote_count,
    SUM(financials_available) AS financial_movies,
    ROUND(AVG(
        CASE
            WHEN financials_available = 1
            THEN revenue
        END
    ), 0) AS avg_revenue,
    ROUND(AVG(
        CASE
            WHEN financials_available = 1
            THEN budget
        END
    ), 0) AS avg_budget,
    ROUND(AVG(
        CASE
            WHEN financials_available = 1
            THEN revenue - budget
        END
    ), 0) AS avg_profit
FROM movies
GROUP BY release_year;



SELECT
    COUNT(*) AS year_count,
    MIN(release_year) AS first_year,
    MAX(release_year) AS last_year
FROM vw_year_analysis;






USE animation_bi;

CREATE OR REPLACE VIEW vw_year_analysis AS
SELECT
    release_year,
    COUNT(*) AS movie_count,
    ROUND(AVG(vote_average), 2) AS avg_rating,
    ROUND(AVG(popularity), 2) AS avg_popularity,
    ROUND(AVG(vote_count), 0) AS avg_vote_count,
    SUM(financials_available) AS financial_movies,
    ROUND(AVG(
        CASE WHEN financials_available = 1
        THEN revenue END
    ), 0) AS avg_revenue,
    ROUND(AVG(
        CASE WHEN financials_available = 1
        THEN budget END
    ), 0) AS avg_budget,
    ROUND(AVG(
        CASE WHEN financials_available = 1
        THEN revenue - budget END
    ), 0) AS avg_profit,
    ROUND(
        SUM(CASE WHEN financials_available = 1
            THEN revenue ELSE 0 END)
        /
        NULLIF(
            SUM(CASE WHEN financials_available = 1
                THEN budget ELSE 0 END),
            0
        ),
        2
    ) AS portfolio_revenue_multiple
FROM movies
GROUP BY release_year;



USE animation_bi;

DESCRIBE vw_year_analysis;