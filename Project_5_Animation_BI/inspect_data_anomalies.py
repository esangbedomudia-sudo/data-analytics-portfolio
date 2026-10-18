import pandas as pd

MOVIES_FILE = "data/animation_movie_details.csv"
COMPANIES_FILE = "data/animation_movie_companies.csv"

movies = pd.read_csv(MOVIES_FILE)
companies = pd.read_csv(COMPANIES_FILE)

print("\n=== ANIMATION BI DATA ANOMALY INSPECTION ===")


# --------------------------------------------------
# 1. MOVIES WITH ZERO RUNTIME
# --------------------------------------------------

zero_runtime_movies = movies[movies["runtime"] == 0].copy()

print("\n--- MOVIES WITH ZERO RUNTIME ---")
print(f"Count: {len(zero_runtime_movies)}")

if len(zero_runtime_movies) > 0:
    print(
        zero_runtime_movies[
            [
                "movie_id",
                "title",
                "release_date",
                "runtime",
                "budget",
                "revenue",
                "vote_average",
                "vote_count",
                "popularity",
                "original_language",
            ]
        ].to_string(index=False)
    )
else:
    print("No movies with zero runtime found.")


# --------------------------------------------------
# 2. MOVIES WITHOUT PRODUCTION COMPANY RECORDS
# --------------------------------------------------

company_movie_ids = set(companies["movie_id"])

movies_without_companies = movies[
    ~movies["movie_id"].isin(company_movie_ids)
].copy()

print("\n--- MOVIES WITHOUT PRODUCTION COMPANY RECORDS ---")
print(f"Count: {len(movies_without_companies)}")

if len(movies_without_companies) > 0:
    print(
        movies_without_companies[
            [
                "movie_id",
                "title",
                "release_date",
                "runtime",
                "budget",
                "revenue",
                "vote_average",
                "vote_count",
                "popularity",
                "original_language",
            ]
        ].to_string(index=False)
    )
else:
    print("Every movie has at least one production company record.")


# --------------------------------------------------
# 3. SUMMARY
# --------------------------------------------------

print("\n--- ANOMALY SUMMARY ---")
print(f"Zero-runtime movies: {len(zero_runtime_movies)}")
print(f"Movies without production companies: {len(movies_without_companies)}")

print("\n=== INSPECTION COMPLETE ===")
