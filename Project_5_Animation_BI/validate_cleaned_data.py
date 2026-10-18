import pandas as pd


MOVIES_FILE = "data/animation_movie_details_cleaned.csv"
GENRES_FILE = "data/animation_movie_genres_cleaned.csv"
COMPANIES_FILE = "data/animation_movie_companies_cleaned.csv"
COUNTRIES_FILE = "data/animation_movie_countries_cleaned.csv"


movies = pd.read_csv(MOVIES_FILE)
genres = pd.read_csv(GENRES_FILE)
companies = pd.read_csv(COMPANIES_FILE)
countries = pd.read_csv(COUNTRIES_FILE)


print("\n=== CLEANED ANIMATION BI DATA VALIDATION ===")


# --------------------------------------------------
# 1. DATASET SIZES
# --------------------------------------------------

print("\n--- DATASET SIZES ---")
print(f"Movies: {len(movies):,}")
print(f"Genres: {len(genres):,}")
print(f"Production companies: {len(companies):,}")
print(f"Production countries: {len(countries):,}")


# --------------------------------------------------
# 2. COLUMNS
# --------------------------------------------------

print("\n--- MOVIE COLUMNS ---")
for column in movies.columns:
    print(f"- {column}")


# --------------------------------------------------
# 3. DUPLICATE CHECKS
# --------------------------------------------------

print("\n--- DUPLICATE CHECKS ---")

print(
    f"Duplicate movie IDs: "
    f"{movies['movie_id'].duplicated().sum()}"
)

print(
    f"Duplicate genre relationship rows: "
    f"{genres.duplicated().sum()}"
)

print(
    f"Duplicate production company relationship rows: "
    f"{companies.duplicated().sum()}"
)

print(
    f"Duplicate production country relationship rows: "
    f"{countries.duplicated().sum()}"
)


# --------------------------------------------------
# 4. MISSING VALUES
# --------------------------------------------------

print("\n--- MISSING VALUES ---")

for column in movies.columns:
    missing = movies[column].isna().sum()
    print(f"- {column}: {missing}")


# --------------------------------------------------
# 5. FINANCIAL AVAILABILITY
# --------------------------------------------------

print("\n--- FINANCIAL AVAILABILITY ---")

print(
    f"Budget available: "
    f"{movies['budget_available'].sum():,}"
)

print(
    f"Budget unavailable: "
    f"{(~movies['budget_available']).sum():,}"
)

print(
    f"Revenue available: "
    f"{movies['revenue_available'].sum():,}"
)

print(
    f"Revenue unavailable: "
    f"{(~movies['revenue_available']).sum():,}"
)

print(
    f"Both budget and revenue available: "
    f"{movies['financials_available'].sum():,}"
)


# --------------------------------------------------
# 6. CHECK FOR REMAINING ZERO VALUES
# --------------------------------------------------

print("\n--- REMAINING ZERO VALUES ---")

print(
    f"Runtime equal to zero: "
    f"{(movies['runtime'] == 0).sum()}"
)

print(
    f"Budget equal to zero: "
    f"{(movies['budget'] == 0).sum()}"
)

print(
    f"Revenue equal to zero: "
    f"{(movies['revenue'] == 0).sum()}"
)


# --------------------------------------------------
# 7. RELEASE YEAR
# --------------------------------------------------

print("\n--- RELEASE YEAR ---")

print(
    f"Missing release years: "
    f"{movies['release_year'].isna().sum()}"
)

print(
    f"Earliest release year: "
    f"{movies['release_year'].min():.0f}"
)

print(
    f"Latest release year: "
    f"{movies['release_year'].max():.0f}"
)


# --------------------------------------------------
# 8. RUNTIME
# --------------------------------------------------

print("\n--- RUNTIME ---")

print(
    f"Missing runtime values: "
    f"{movies['runtime'].isna().sum()}"
)

print(
    f"Minimum available runtime: "
    f"{movies['runtime'].min():.0f} minutes"
)

print(
    f"Maximum runtime: "
    f"{movies['runtime'].max():.0f} minutes"
)


# --------------------------------------------------
# 9. RELATIONSHIP COVERAGE
# --------------------------------------------------

print("\n--- RELATIONSHIP COVERAGE ---")

movie_ids = set(movies["movie_id"])

genre_movie_ids = set(genres["movie_id"])
company_movie_ids = set(companies["movie_id"])
country_movie_ids = set(countries["movie_id"])

print(
    f"Movies without genres: "
    f"{len(movie_ids - genre_movie_ids)}"
)

print(
    f"Movies without production companies: "
    f"{len(movie_ids - company_movie_ids)}"
)

print(
    f"Movies without production countries: "
    f"{len(movie_ids - country_movie_ids)}"
)


# --------------------------------------------------
# 10. ORPHAN RELATIONSHIPS
# --------------------------------------------------

print("\n--- ORPHAN RELATIONSHIPS ---")

print(
    f"Orphan genre records: "
    f"{(~genres['movie_id'].isin(movie_ids)).sum()}"
)

print(
    f"Orphan production company records: "
    f"{(~companies['movie_id'].isin(movie_ids)).sum()}"
)

print(
    f"Orphan production country records: "
    f"{(~countries['movie_id'].isin(movie_ids)).sum()}"
)


print("\n=== CLEANED DATA VALIDATION COMPLETE ===")
