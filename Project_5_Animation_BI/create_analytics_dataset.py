import pandas as pd


# --------------------------------------------------
# FILE PATHS
# --------------------------------------------------

MOVIES_FILE = "data/animation_movie_details_cleaned.csv"

OUTPUT_FILE = "data/animation_movie_analytics.csv"


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

movies = pd.read_csv(MOVIES_FILE)


print("\n=== CREATING ANIMATION BI ANALYTICS DATASET ===")


# --------------------------------------------------
# 1. CALCULATE FINANCIAL METRICS
# --------------------------------------------------

movies["profit"] = (
    movies["revenue"] - movies["budget"]
)

movies["profit_margin"] = (
    movies["profit"] / movies["revenue"]
)

movies["return_on_budget"] = (
    movies["revenue"] / movies["budget"]
)


# --------------------------------------------------
# 2. HANDLE FINANCIAL METRICS WHEN DATA IS MISSING
# --------------------------------------------------

movies.loc[
    ~movies["financials_available"],
    [
        "profit",
        "profit_margin",
        "return_on_budget"
    ]
] = pd.NA


# --------------------------------------------------
# 3. ADD PERFORMANCE FLAGS
# --------------------------------------------------

movies["high_rating"] = (
    movies["vote_average"] >= 7.5
)

movies["high_popularity"] = (
    movies["popularity"] >= movies["popularity"].median()
)

movies["high_vote_count"] = (
    movies["vote_count"] >= movies["vote_count"].median()
)


# --------------------------------------------------
# 4. ADD FINANCIAL PERFORMANCE FLAGS
# --------------------------------------------------

movies["profitable"] = (
    movies["profit"] > 0
)

movies["financial_success"] = (
    movies["financials_available"]
    & (movies["profit"] > 0)
)


# --------------------------------------------------
# 5. SAVE ANALYTICS DATASET
# --------------------------------------------------

movies.to_csv(
    OUTPUT_FILE,
    index=False
)


# --------------------------------------------------
# 6. SUMMARY
# --------------------------------------------------

print("\n--- ANALYTICS SUMMARY ---")

print(
    f"Movies analyzed: "
    f"{len(movies):,}"
)

print(
    f"Movies with financial data: "
    f"{movies['financials_available'].sum():,}"
)

print(
    f"Profitable movies: "
    f"{movies['financial_success'].sum():,}"
)

print(
    f"High-rated movies: "
    f"{movies['high_rating'].sum():,}"
)

print(
    f"High-popularity movies: "
    f"{movies['high_popularity'].sum():,}"
)

print(
    f"High-vote-count movies: "
    f"{movies['high_vote_count'].sum():,}"
)


# --------------------------------------------------
# 7. CORE METRIC SUMMARY
# --------------------------------------------------

print("\n--- CORE FINANCIAL METRICS ---")

print(
    f"Total budget: "
    f"${movies['budget'].sum():,.0f}"
)

print(
    f"Total revenue: "
    f"${movies['revenue'].sum():,.0f}"
)

print(
    f"Total profit: "
    f"${movies['profit'].sum():,.0f}"
)

print(
    f"Median rating: "
    f"{movies['vote_average'].median():.2f}"
)

print(
    f"Median popularity: "
    f"{movies['popularity'].median():.2f}"
)


print("\n--- OUTPUT FILE ---")
print(f"- {OUTPUT_FILE}")

print("\n=== ANALYTICS DATASET CREATED ===")
