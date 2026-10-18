import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv


# ============================================================
# CONFIGURATION
# ============================================================

CANDIDATE_FILE = "data/animation_movie_candidates.csv"

OUTPUT_FILE = "data/animation_movie_details.csv"
GENRES_FILE = "data/animation_movie_genres.csv"
COMPANIES_FILE = "data/animation_movie_companies.csv"
COUNTRIES_FILE = "data/animation_movie_countries.csv"

CHECKPOINT_INTERVAL = 25
REQUEST_DELAY = 0.25
MAX_RETRIES = 3


# ============================================================
# SAVE FUNCTION
# ============================================================

def save_movie_data(
    movie_records,
    genre_records,
    company_records,
    country_records,
    existing_movies
):

    # --------------------------------------------------------
    # Movies
    # --------------------------------------------------------

    new_movies = pd.DataFrame(movie_records)

    if existing_movies.empty:
        all_movies = new_movies
    else:
        all_movies = pd.concat(
            [existing_movies, new_movies],
            ignore_index=True
        )

    all_movies = all_movies.drop_duplicates(
        subset="movie_id",
        keep="last"
    )

    all_movies.to_csv(
        OUTPUT_FILE,
        index=False
    )

    # --------------------------------------------------------
    # Genres
    # --------------------------------------------------------

    new_genres = pd.DataFrame(genre_records)

    if os.path.exists(GENRES_FILE):
        existing_genres = pd.read_csv(GENRES_FILE)

        all_genres = pd.concat(
            [existing_genres, new_genres],
            ignore_index=True
        )
    else:
        all_genres = new_genres

    all_genres = all_genres.drop_duplicates()

    all_genres.to_csv(
        GENRES_FILE,
        index=False
    )

    # --------------------------------------------------------
    # Production companies
    # --------------------------------------------------------

    new_companies = pd.DataFrame(company_records)

    if os.path.exists(COMPANIES_FILE):
        existing_companies = pd.read_csv(COMPANIES_FILE)

        all_companies = pd.concat(
            [existing_companies, new_companies],
            ignore_index=True
        )
    else:
        all_companies = new_companies

    all_companies = all_companies.drop_duplicates()

    all_companies.to_csv(
        COMPANIES_FILE,
        index=False
    )

    # --------------------------------------------------------
    # Production countries
    # --------------------------------------------------------

    new_countries = pd.DataFrame(country_records)

    if os.path.exists(COUNTRIES_FILE):
        existing_countries = pd.read_csv(COUNTRIES_FILE)

        all_countries = pd.concat(
            [existing_countries, new_countries],
            ignore_index=True
        )
    else:
        all_countries = new_countries

    all_countries = all_countries.drop_duplicates()

    all_countries.to_csv(
        COUNTRIES_FILE,
        index=False
    )


# ============================================================
# LOAD TMDB TOKEN
# ============================================================

load_dotenv()

token = os.getenv("TMDB_READ_ACCESS_TOKEN")

if not token:
    raise RuntimeError(
        "TMDB_READ_ACCESS_TOKEN was not found. "
        "Check that your .env file exists and contains the token."
    )


# ============================================================
# TMDB REQUEST SETUP
# ============================================================

headers = {
    "Authorization": f"Bearer {token}",
    "accept": "application/json"
}


# ============================================================
# LOAD CANDIDATE MOVIES
# ============================================================

df_candidates = pd.read_csv(CANDIDATE_FILE)

print("\n=== DETAILED TMDB MOVIE COLLECTION ===")
print(f"Candidate movies: {len(df_candidates)}")


# ============================================================
# LOAD EXISTING PROGRESS
# ============================================================

if os.path.exists(OUTPUT_FILE):

    df_existing = pd.read_csv(OUTPUT_FILE)

    completed_ids = set(
        df_existing["movie_id"].astype(int)
    )

    print(
        f"Existing detailed records: "
        f"{len(df_existing)}"
    )

    print(
        f"Movies already collected: "
        f"{len(completed_ids)}"
    )

else:

    df_existing = pd.DataFrame()
    completed_ids = set()

    print("No previous collection found.")
    print("Starting from the beginning.")


# ============================================================
# STORAGE FOR NEW DATA
# ============================================================

movie_records = []
genre_records = []
company_records = []
country_records = []


# ============================================================
# COLLECT MOVIE DETAILS
# ============================================================

total_movies = len(df_candidates)

for index, candidate in df_candidates.iterrows():

    movie_id = int(candidate["id"])
    title = candidate["title"]

    # --------------------------------------------------------
    # Skip movies already collected
    # --------------------------------------------------------

    if movie_id in completed_ids:
        continue

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    movie = None

    # --------------------------------------------------------
    # Request with retries
    # --------------------------------------------------------

    for attempt in range(1, MAX_RETRIES + 1):

        try:

            response = requests.get(
                url,
                headers=headers,
                params={"language": "en-US"},
                timeout=30
            )

            response.raise_for_status()

            movie = response.json()

            break

        except requests.RequestException as error:

            print(
                f"\nRequest failed for {title} "
                f"(ID {movie_id}) - "
                f"attempt {attempt}/{MAX_RETRIES}"
            )

            print(f"Error: {error}")

            if attempt < MAX_RETRIES:
                time.sleep(2)

    # --------------------------------------------------------
    # Skip movie if all attempts failed
    # --------------------------------------------------------

    if movie is None:

        print(
            f"Skipping {title} "
            f"after {MAX_RETRIES} failed attempts."
        )

        continue

    # --------------------------------------------------------
    # Main movie record
    # --------------------------------------------------------

    movie_records.append(
        {
            "movie_id": movie.get("id"),
            "title": movie.get("title"),
            "release_date": movie.get("release_date"),
            "runtime": movie.get("runtime"),
            "budget": movie.get("budget"),
            "revenue": movie.get("revenue"),
            "vote_average": movie.get("vote_average"),
            "vote_count": movie.get("vote_count"),
            "popularity": movie.get("popularity"),
            "original_language": movie.get("original_language"),
        }
    )

    # --------------------------------------------------------
    # Genre records
    # --------------------------------------------------------

    for genre in movie.get("genres", []):

        genre_records.append(
            {
                "movie_id": movie_id,
                "genre_id": genre.get("id"),
                "genre_name": genre.get("name"),
            }
        )

    # --------------------------------------------------------
    # Production company records
    # --------------------------------------------------------

    for company in movie.get("production_companies", []):

        company_records.append(
            {
                "movie_id": movie_id,
                "company_id": company.get("id"),
                "company_name": company.get("name"),
            }
        )

    # --------------------------------------------------------
    # Production country records
    # --------------------------------------------------------

    for country in movie.get("production_countries", []):

        country_records.append(
            {
                "movie_id": movie_id,
                "country_code": country.get("iso_3166_1"),
                "country_name": country.get("name"),
            }
        )

    completed_ids.add(movie_id)

    # --------------------------------------------------------
    # Progress display
    # --------------------------------------------------------

    collected_count = len(completed_ids)

    print(
        f"[{collected_count}/{total_movies}] "
        f"Collected: {title}"
    )

    # --------------------------------------------------------
    # Checkpoint
    # --------------------------------------------------------

    if len(movie_records) >= CHECKPOINT_INTERVAL:

        print("\nSaving checkpoint...")

        save_movie_data(
            movie_records,
            genre_records,
            company_records,
            country_records,
            df_existing
        )

        df_existing = pd.read_csv(OUTPUT_FILE)

        movie_records = []
        genre_records = []
        company_records = []
        country_records = []

        print("Checkpoint saved.\n")

    # --------------------------------------------------------
    # Small delay between requests
    # --------------------------------------------------------

    time.sleep(REQUEST_DELAY)


# ============================================================
# FINAL SAVE
# ============================================================

if movie_records:

    print("\nSaving final batch...")

    save_movie_data(
        movie_records,
        genre_records,
        company_records,
        country_records,
        df_existing
    )


# ============================================================
# COLLECTION SUMMARY
# ============================================================

print("\n=== COLLECTION COMPLETE ===")

if os.path.exists(OUTPUT_FILE):

    final_movies = pd.read_csv(OUTPUT_FILE)

    print(
        f"Detailed movies collected: "
        f"{len(final_movies)}"
    )

if os.path.exists(GENRES_FILE):

    final_genres = pd.read_csv(GENRES_FILE)

    print(
        f"Genre records: "
        f"{len(final_genres)}"
    )

if os.path.exists(COMPANIES_FILE):

    final_companies = pd.read_csv(COMPANIES_FILE)

    print(
        f"Production company records: "
        f"{len(final_companies)}"
    )

if os.path.exists(COUNTRIES_FILE):

    final_countries = pd.read_csv(COUNTRIES_FILE)

    print(
        f"Production country records: "
        f"{len(final_countries)}"
    )
