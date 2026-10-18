import pandas as pd


# --------------------------------------------------
# FILE PATH
# --------------------------------------------------

ANALYTICS_FILE = "data/animation_movie_analytics.csv"


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv(ANALYTICS_FILE)


print("\n=== ANIMATION BI ANALYTICS DATASET VALIDATION ===")


# --------------------------------------------------
# 1. DATASET SIZE
# --------------------------------------------------

print("\n--- DATASET SIZE ---")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns):,}")


# --------------------------------------------------
# 2. COLUMNS
# --------------------------------------------------

print("\n--- COLUMNS ---")

for column in df.columns:
    print(f"- {column}")


# --------------------------------------------------
# 3. DUPLICATE MOVIE CHECK
# --------------------------------------------------

print("\n--- DUPLICATE CHECK ---")

duplicate_movie_ids = df["movie_id"].duplicated().sum()

print(f"Duplicate movie IDs: {duplicate_movie_ids}")


# --------------------------------------------------
# 4. MISSING VALUES
# --------------------------------------------------

print("\n--- MISSING VALUES ---")

missing = df.isnull().sum()

for column, count in missing.items():
    print(f"- {column}: {count}")


# --------------------------------------------------
# 5. FINANCIAL DATA CHECK
# --------------------------------------------------

print("\n--- FINANCIAL DATA ---")

financial_movies = df["financials_available"].sum()

print(f"Movies with financial data: {financial_movies:,}")

if "budget" in df.columns:
    print(f"Budget missing: {df['budget'].isna().sum():,}")

if "revenue" in df.columns:
    print(f"Revenue missing: {df['revenue'].isna().sum():,}")


# --------------------------------------------------
# 6. PROFIT VALIDATION
# --------------------------------------------------

print("\n--- PROFIT VALIDATION ---")

if "profit" in df.columns and "budget" in df.columns and "revenue" in df.columns:

    profit_check = (
        df["profit"]
        - (df["revenue"] - df["budget"])
    ).abs()

    incorrect_profit = (profit_check > 0.01).sum()

    print(f"Incorrect profit calculations: {incorrect_profit}")

else:
    print("Required financial columns not found for profit validation.")


# --------------------------------------------------
# 7. PROFITABILITY VALIDATION
# --------------------------------------------------

print("\n--- PROFITABILITY VALIDATION ---")

if "profitable" in df.columns and "profit" in df.columns:

    expected_profitable = df["profit"] > 0

    incorrect_profitable = (
        df["profitable"] != expected_profitable
    ).sum()

    print(
        f"Incorrect profitable flags: "
        f"{incorrect_profitable}"
    )

else:
    print("Required columns not found for profitability validation.")


# --------------------------------------------------
# 8. RELEASE YEAR VALIDATION
# --------------------------------------------------

print("\n--- RELEASE YEAR VALIDATION ---")

if "release_year" in df.columns:

    missing_years = df["release_year"].isna().sum()

    years_below_range = (
        df["release_year"] < 2000
    ).sum()

    years_above_range = (
        df["release_year"] > 2025
    ).sum()

    print(f"Missing release years: {missing_years}")
    print(f"Years before 2000: {years_below_range}")
    print(f"Years after 2025: {years_above_range}")


# --------------------------------------------------
# 9. RATING VALIDATION
# --------------------------------------------------

print("\n--- RATING VALIDATION ---")

if "vote_average" in df.columns:

    ratings_below_zero = (
        df["vote_average"] < 0
    ).sum()

    ratings_above_ten = (
        df["vote_average"] > 10
    ).sum()

    print(f"Ratings below 0: {ratings_below_zero}")
    print(f"Ratings above 10: {ratings_above_ten}")


# --------------------------------------------------
# 10. VOTE COUNT VALIDATION
# --------------------------------------------------

print("\n--- VOTE COUNT VALIDATION ---")

if "vote_count" in df.columns:

    negative_vote_counts = (
        df["vote_count"] < 0
    ).sum()

    print(
        f"Negative vote counts: "
        f"{negative_vote_counts}"
    )


# --------------------------------------------------
# 11. POPULARITY VALIDATION
# --------------------------------------------------

print("\n--- POPULARITY VALIDATION ---")

if "popularity" in df.columns:

    negative_popularity = (
        df["popularity"] < 0
    ).sum()

    print(
        f"Negative popularity values: "
        f"{negative_popularity}"
    )


# --------------------------------------------------
# 12. SUMMARY METRICS
# --------------------------------------------------

print("\n--- ANALYTICS SUMMARY ---")

if "profit" in df.columns:

    print(
        f"Total budget: "
        f"${df['budget'].sum():,.0f}"
    )

    print(
        f"Total revenue: "
        f"${df['revenue'].sum():,.0f}"
    )

    print(
        f"Total profit: "
        f"${df['profit'].sum():,.0f}"
    )

if "vote_average" in df.columns:
    print(
        f"Median rating: "
        f"{df['vote_average'].median():.2f}"
    )

if "popularity" in df.columns:
    print(
        f"Median popularity: "
        f"{df['popularity'].median():.2f}"
    )


# --------------------------------------------------
# COMPLETE
# --------------------------------------------------

print("\n=== ANALYTICS DATASET VALIDATION COMPLETE ===")
