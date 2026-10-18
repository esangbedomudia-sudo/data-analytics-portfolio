import pandas as pd


# --------------------------------------------------
# FILE PATHS
# --------------------------------------------------

MOVIES_FILE = "data/animation_movie_details.csv"
GENRES_FILE = "data/animation_movie_genres.csv"
COMPANIES_FILE = "data/animation_movie_companies.csv"
COUNTRIES_FILE = "data/animation_movie_countries.csv"

CLEAN_MOVIES_FILE = "data/animation_movie_details_cleaned.csv"
CLEAN_GENRES_FILE = "data/animation_movie_genres_cleaned.csv"
CLEAN_COMPANIES_FILE = "data/animation_movie_companies_cleaned.csv"
CLEAN_COUNTRIES_FILE = "data/animation_movie_countries_cleaned.csv"


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

movies = pd.read_csv(MOVIES_FILE)
genres = pd.read_csv(GENRES_FILE)
companies = pd.read_csv(COMPANIES_FILE)
countries = pd.read_csv(COUNTRIES_FILE)


print("\n=== ANIMATION BI DATA CLEANING ===")


# --------------------------------------------------
# 1. CONVERT RELEASE DATE
# --------------------------------------------------

movies["release_date"] = pd.to_datetime(
    movies["release_date"],
    errors="coerce"
)


# --------------------------------------------------
# 2. TREAT ZERO RUNTIME AS MISSING
# --------------------------------------------------

zero_runtime_count = (movies["runtime"] == 0).sum()

movies["runtime"] = movies["runtime"].replace(0, pd.NA)


# --------------------------------------------------
# 3. TREAT ZERO BUDGET AS MISSING
# --------------------------------------------------

zero_budget_count = (movies["budget"] == 0).sum()

movies["budget"] = movies["budget"].replace(0, pd.NA)


# --------------------------------------------------
# 4. TREAT ZERO REVENUE AS MISSING
# --------------------------------------------------

zero_revenue_count = (movies["revenue"] == 0).sum()

movies["revenue"] = movies["revenue"].replace(0, pd.NA)


# --------------------------------------------------
# 5. ADD FINANCIAL AVAILABILITY FLAGS
# --------------------------------------------------

movies["budget_available"] = movies["budget"].notna()

movies["revenue_available"] = movies["revenue"].notna()

movies["financials_available"] = (
    movies["budget_available"]
    & movies["revenue_available"]
)


# --------------------------------------------------
# 6. ADD RELEASE YEAR
# --------------------------------------------------

movies["release_year"] = movies["release_date"].dt.year


# --------------------------------------------------
# 7. SAVE CLEANED DATA
# --------------------------------------------------

movies.to_csv(
    CLEAN_MOVIES_FILE,
    index=False
)

genres.to_csv(
    CLEAN_GENRES_FILE,
    index=False
)

companies.to_csv(
    CLEAN_COMPANIES_FILE,
    index=False
)

countries.to_csv(
    CLEAN_COUNTRIES_FILE,
    index=False
)


# --------------------------------------------------
# 8. CLEANING SUMMARY
# --------------------------------------------------

print("\n--- CLEANING SUMMARY ---")

print(f"Movies retained: {len(movies):,}")
print(f"Genre records retained: {len(genres):,}")
print(f"Production company records retained: {len(companies):,}")
print(f"Production country records retained: {len(countries):,}")

print(f"\nZero runtimes converted to missing: {zero_runtime_count}")
print(f"Zero budgets converted to missing: {zero_budget_count}")
print(f"Zero revenues converted to missing: {zero_revenue_count}")

print(
    f"\nMovies with budget available: "
    f"{movies['budget_available'].sum():,}"
)

print(
    f"Movies with revenue available: "
    f"{movies['revenue_available'].sum():,}"
)

print(
    f"Movies with both budget and revenue available: "
    f"{movies['financials_available'].sum():,}"
)

print(
    f"\nRuntime missing after cleaning: "
    f"{movies['runtime'].isna().sum():,}"
)

print(
    f"Budget missing after cleaning: "
    f"{movies['budget'].isna().sum():,}"
)

print(
    f"Revenue missing after cleaning: "
    f"{movies['revenue'].isna().sum():,}"
)


print("\n--- OUTPUT FILES ---")
print(f"- {CLEAN_MOVIES_FILE}")
print(f"- {CLEAN_GENRES_FILE}")
print(f"- {CLEAN_COMPANIES_FILE}")
print(f"- {CLEAN_COUNTRIES_FILE}")

print("\n=== CLEANING COMPLETE ===")
