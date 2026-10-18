import pandas as pd


# ============================================================
# FILE PATHS
# ============================================================

MOVIES_FILE = "data/animation_movie_details.csv"
GENRES_FILE = "data/animation_movie_genres.csv"
COMPANIES_FILE = "data/animation_movie_companies.csv"
COUNTRIES_FILE = "data/animation_movie_countries.csv"


# ============================================================
# LOAD DATA
# ============================================================

movies = pd.read_csv(MOVIES_FILE)
genres = pd.read_csv(GENRES_FILE)
companies = pd.read_csv(COMPANIES_FILE)
countries = pd.read_csv(COUNTRIES_FILE)


print("\n=== ANIMATION BI DATA VALIDATION ===")


# ============================================================
# BASIC DATASET SIZES
# ============================================================

print("\n--- DATASET SIZES ---")

print(f"Movies: {len(movies):,}")
print(f"Genres: {len(genres):,}")
print(f"Production companies: {len(companies):,}")
print(f"Production countries: {len(countries):,}")


# ============================================================
# COLUMN CHECK
# ============================================================

print("\n--- COLUMNS ---")

print("\nMovies:")
for column in movies.columns:
    print(f"- {column}")

print("\nGenres:")
for column in genres.columns:
    print(f"- {column}")

print("\nProduction companies:")
for column in companies.columns:
    print(f"- {column}")

print("\nProduction countries:")
for column in countries.columns:
    print(f"- {column}")


# ============================================================
# MISSING VALUES
# ============================================================

print("\n--- MISSING VALUES ---")

for name, dataframe in [
    ("Movies", movies),
    ("Genres", genres),
    ("Production companies", companies),
    ("Production countries", countries)
]:

    print(f"\n{name}:")

    missing = dataframe.isnull().sum()

    for column, count in missing.items():
        print(f"- {column}: {count}")


# ============================================================
# DUPLICATE CHECKS
# ============================================================

print("\n--- DUPLICATE CHECKS ---")

movie_duplicate_ids = movies["movie_id"].duplicated().sum()

genre_duplicate_rows = genres.duplicated().sum()

company_duplicate_rows = companies.duplicated().sum()

country_duplicate_rows = countries.duplicated().sum()

print(
    f"Duplicate movie IDs: "
    f"{movie_duplicate_ids}"
)

print(
    f"Duplicate genre relationship rows: "
    f"{genre_duplicate_rows}"
)

print(
    f"Duplicate production company relationship rows: "
    f"{company_duplicate_rows}"
)

print(
    f"Duplicate production country relationship rows: "
    f"{country_duplicate_rows}"
)


# ============================================================
# DATE VALIDATION
# ============================================================

print("\n--- RELEASE DATE VALIDATION ---")

movies["release_date"] = pd.to_datetime(
    movies["release_date"],
    errors="coerce"
)

invalid_dates = movies["release_date"].isna().sum()

print(f"Invalid/missing release dates: {invalid_dates}")

if invalid_dates == 0:

    print(
        f"Earliest release date: "
        f"{movies['release_date'].min().date()}"
    )

    print(
        f"Latest release date: "
        f"{movies['release_date'].max().date()}"
    )


# ============================================================
# RUNTIME VALIDATION
# ============================================================

print("\n--- RUNTIME VALIDATION ---")

runtime_missing = movies["runtime"].isna().sum()

runtime_zero = (movies["runtime"] == 0).sum()

runtime_negative = (movies["runtime"] < 0).sum()

print(f"Missing runtime values: {runtime_missing}")
print(f"Zero runtime values: {runtime_zero}")
print(f"Negative runtime values: {runtime_negative}")

print(
    f"Minimum runtime: "
    f"{movies['runtime'].min():.0f} minutes"
)

print(
    f"Maximum runtime: "
    f"{movies['runtime'].max():.0f} minutes"
)

print(
    f"Average runtime: "
    f"{movies['runtime'].mean():.1f} minutes"
)

print(
    f"Median runtime: "
    f"{movies['runtime'].median():.1f} minutes"
)


# ============================================================
# FINANCIAL VALIDATION
# ============================================================

print("\n--- FINANCIAL VALIDATION ---")

budget_missing = movies["budget"].isna().sum()
budget_zero = (movies["budget"] == 0).sum()
budget_negative = (movies["budget"] < 0).sum()

revenue_missing = movies["revenue"].isna().sum()
revenue_zero = (movies["revenue"] == 0).sum()
revenue_negative = (movies["revenue"] < 0).sum()

print(f"Budget missing: {budget_missing}")
print(f"Budget equal to zero: {budget_zero}")
print(f"Budget negative: {budget_negative}")

print(f"Revenue missing: {revenue_missing}")
print(f"Revenue equal to zero: {revenue_zero}")
print(f"Revenue negative: {revenue_negative}")


# ============================================================
# RATING VALIDATION
# ============================================================

print("\n--- RATING VALIDATION ---")

rating_missing = movies["vote_average"].isna().sum()

rating_below_zero = (
    movies["vote_average"] < 0
).sum()

rating_above_ten = (
    movies["vote_average"] > 10
).sum()

print(f"Missing ratings: {rating_missing}")
print(f"Ratings below 0: {rating_below_zero}")
print(f"Ratings above 10: {rating_above_ten}")

print(
    f"Minimum rating: "
    f"{movies['vote_average'].min():.2f}"
)

print(
    f"Maximum rating: "
    f"{movies['vote_average'].max():.2f}"
)

print(
    f"Average rating: "
    f"{movies['vote_average'].mean():.2f}"
)

print(
    f"Median rating: "
    f"{movies['vote_average'].median():.2f}"
)


# ============================================================
# VOTE COUNT VALIDATION
# ============================================================

print("\n--- VOTE COUNT VALIDATION ---")

vote_count_missing = movies["vote_count"].isna().sum()

vote_count_below_zero = (
    movies["vote_count"] < 0
).sum()

print(
    f"Missing vote counts: "
    f"{vote_count_missing}"
)

print(
    f"Negative vote counts: "
    f"{vote_count_below_zero}"
)

print(
    f"Minimum vote count: "
    f"{movies['vote_count'].min():,.0f}"
)

print(
    f"Maximum vote count: "
    f"{movies['vote_count'].max():,.0f}"
)

print(
    f"Average vote count: "
    f"{movies['vote_count'].mean():,.1f}"
)

print(
    f"Median vote count: "
    f"{movies['vote_count'].median():,.1f}"
)


# ============================================================
# POPULARITY VALIDATION
# ============================================================

print("\n--- POPULARITY VALIDATION ---")

popularity_missing = movies["popularity"].isna().sum()

popularity_negative = (
    movies["popularity"] < 0
).sum()

print(
    f"Missing popularity values: "
    f"{popularity_missing}"
)

print(
    f"Negative popularity values: "
    f"{popularity_negative}"
)

print(
    f"Minimum popularity: "
    f"{movies['popularity'].min():.4f}"
)

print(
    f"Maximum popularity: "
    f"{movies['popularity'].max():.4f}"
)

print(
    f"Average popularity: "
    f"{movies['popularity'].mean():.4f}"
)

print(
    f"Median popularity: "
    f"{movies['popularity'].median():.4f}"
)


# ============================================================
# RELATIONSHIP COVERAGE
# ============================================================

print("\n--- RELATIONSHIP COVERAGE ---")

movie_ids = set(movies["movie_id"])

genre_movie_ids = set(genres["movie_id"])

company_movie_ids = set(companies["movie_id"])

country_movie_ids = set(countries["movie_id"])


movies_without_genres = movie_ids - genre_movie_ids

movies_without_companies = movie_ids - company_movie_ids

movies_without_countries = movie_ids - country_movie_ids


print(
    f"Movies without genre records: "
    f"{len(movies_without_genres)}"
)

print(
    f"Movies without production company records: "
    f"{len(movies_without_companies)}"
)

print(
    f"Movies without production country records: "
    f"{len(movies_without_countries)}"
)


# ============================================================
# RELATIONSHIP COUNTS PER MOVIE
# ============================================================

print("\n--- RELATIONSHIP COUNTS PER MOVIE ---")

genre_counts = genres.groupby("movie_id").size()

company_counts = companies.groupby("movie_id").size()

country_counts = countries.groupby("movie_id").size()


print(
    f"Average genres per movie: "
    f"{genre_counts.mean():.2f}"
)

print(
    f"Average production companies per movie: "
    f"{company_counts.mean():.2f}"
)

print(
    f"Average production countries per movie: "
    f"{country_counts.mean():.2f}"
)


# ============================================================
# ORPHAN RECORD CHECK
# ============================================================

print("\n--- ORPHAN RELATIONSHIP CHECK ---")

orphan_genres = (
    ~genres["movie_id"].isin(movie_ids)
).sum()

orphan_companies = (
    ~companies["movie_id"].isin(movie_ids)
).sum()

orphan_countries = (
    ~countries["movie_id"].isin(movie_ids)
).sum()


print(
    f"Genre records without a matching movie: "
    f"{orphan_genres}"
)

print(
    f"Company records without a matching movie: "
    f"{orphan_companies}"
)

print(
    f"Country records without a matching movie: "
    f"{orphan_countries}"
)


# ============================================================
# FINAL STATUS
# ============================================================

print("\n=== VALIDATION COMPLETE ===")
