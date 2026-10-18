import pandas as pd


# --------------------------------------------------
# FILE PATHS
# --------------------------------------------------

MOVIES_FILE = "data/animation_movie_details_cleaned.csv"
GENRES_FILE = "data/animation_movie_genres_cleaned.csv"
COMPANIES_FILE = "data/animation_movie_companies_cleaned.csv"
COUNTRIES_FILE = "data/animation_movie_countries_cleaned.csv"


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

movies = pd.read_csv(MOVIES_FILE)
genres = pd.read_csv(GENRES_FILE)
companies = pd.read_csv(COMPANIES_FILE)
countries = pd.read_csv(COUNTRIES_FILE)


print("\n=== ANIMATION BI DATA MODEL VALIDATION ===")


# --------------------------------------------------
# 1. PRIMARY KEY CHECK
# --------------------------------------------------

print("\n--- PRIMARY KEY CHECK ---")

movie_ids = movies["movie_id"]

print(
    f"Movie records: "
    f"{len(movie_ids):,}"
)

print(
    f"Unique movie IDs: "
    f"{movie_ids.nunique():,}"
)

print(
    f"Duplicate movie IDs: "
    f"{movie_ids.duplicated().sum()}"
)


# --------------------------------------------------
# 2. FOREIGN KEY CHECKS
# --------------------------------------------------

print("\n--- FOREIGN KEY CHECKS ---")

movie_id_set = set(movies["movie_id"])

genre_movie_ids = set(genres["movie_id"])
company_movie_ids = set(companies["movie_id"])
country_movie_ids = set(countries["movie_id"])


orphan_genres = genres[
    ~genres["movie_id"].isin(movie_id_set)
]

orphan_companies = companies[
    ~companies["movie_id"].isin(movie_id_set)
]

orphan_countries = countries[
    ~countries["movie_id"].isin(movie_id_set)
]


print(
    f"Orphan genre records: "
    f"{len(orphan_genres):,}"
)

print(
    f"Orphan production company records: "
    f"{len(orphan_companies):,}"
)

print(
    f"Orphan production country records: "
    f"{len(orphan_countries):,}"
)


# --------------------------------------------------
# 3. MANY-TO-MANY RELATIONSHIP CHECK
# --------------------------------------------------

print("\n--- RELATIONSHIP CHECK ---")

genre_counts = genres.groupby("movie_id").size()
company_counts = companies.groupby("movie_id").size()
country_counts = countries.groupby("movie_id").size()


print(
    f"Movies with multiple genres: "
    f"{(genre_counts > 1).sum():,}"
)

print(
    f"Movies with multiple production companies: "
    f"{(company_counts > 1).sum():,}"
)

print(
    f"Movies with multiple production countries: "
    f"{(country_counts > 1).sum():,}"
)


# --------------------------------------------------
# 4. RELATIONSHIP COVERAGE
# --------------------------------------------------

print("\n--- RELATIONSHIP COVERAGE ---")

movies_without_genres = movie_id_set - genre_movie_ids
movies_without_companies = movie_id_set - company_movie_ids
movies_without_countries = movie_id_set - country_movie_ids


print(
    f"Movies without genres: "
    f"{len(movies_without_genres):,}"
)

print(
    f"Movies without production companies: "
    f"{len(movies_without_companies):,}"
)

print(
    f"Movies without production countries: "
    f"{len(movies_without_countries):,}"
)


# --------------------------------------------------
# 5. UNIQUE DIMENSION VALUES
# --------------------------------------------------

print("\n--- UNIQUE DIMENSION VALUES ---")

print(
    f"Unique genres: "
    f"{genres['genre_id'].nunique():,}"
)

print(
    f"Unique production companies: "
    f"{companies['company_id'].nunique():,}"
)

print(
    f"Unique production countries: "
    f"{countries['country_code'].nunique():,}"
)


# --------------------------------------------------
# 6. DUPLICATE RELATIONSHIP CHECK
# --------------------------------------------------

print("\n--- DUPLICATE RELATIONSHIP CHECK ---")

genre_duplicates = genres.duplicated(
    subset=["movie_id", "genre_id"]
).sum()

company_duplicates = companies.duplicated(
    subset=["movie_id", "company_id"]
).sum()

country_duplicates = countries.duplicated(
    subset=["movie_id", "country_code"]
).sum()


print(
    f"Duplicate movie-genre relationships: "
    f"{genre_duplicates:,}"
)

print(
    f"Duplicate movie-company relationships: "
    f"{company_duplicates:,}"
)

print(
    f"Duplicate movie-country relationships: "
    f"{country_duplicates:,}"
)


print("\n=== DATA MODEL VALIDATION COMPLETE ===")
