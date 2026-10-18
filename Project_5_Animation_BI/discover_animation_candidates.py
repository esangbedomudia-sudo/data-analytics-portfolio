import os
import requests
import pandas as pd
from dotenv import load_dotenv

# --------------------------------------------------
# Load TMDB credentials
# --------------------------------------------------

load_dotenv()

token = os.getenv("TMDB_READ_ACCESS_TOKEN")

if not token:
    raise RuntimeError(
        "TMDB_READ_ACCESS_TOKEN was not found."
    )

headers = {
    "Authorization": f"Bearer {token}",
    "accept": "application/json"
}


# --------------------------------------------------
# Get the official Animation genre ID
# --------------------------------------------------

genre_url = "https://api.themoviedb.org/3/genre/movie/list"

genre_response = requests.get(
    genre_url,
    headers=headers,
    params={"language": "en-US"},
    timeout=30
)

genre_response.raise_for_status()

genres = genre_response.json()["genres"]

animation_genre = next(
    genre for genre in genres
    if genre["name"] == "Animation"
)

animation_genre_id = animation_genre["id"]

print("Animation genre ID:", animation_genre_id)


# --------------------------------------------------
# Discover candidate animated feature films
# --------------------------------------------------

discover_url = "https://api.themoviedb.org/3/discover/movie"

base_params = {
    "language": "en-US",
    "include_adult": "false",
    "include_video": "false",
    "sort_by": "popularity.desc",

    # Our project criteria
    "with_genres": animation_genre_id,
    "primary_release_date.gte": "2000-01-01",
    "primary_release_date.lte": "2025-12-31",
    "with_runtime.gte": 60,
    "vote_count.gte": 100
}


# --------------------------------------------------
# Get page 1 first so we know how many pages exist
# --------------------------------------------------

first_response = requests.get(
    discover_url,
    headers=headers,
    params={**base_params, "page": 1},
    timeout=30
)

first_response.raise_for_status()

first_data = first_response.json()

total_results = first_data["total_results"]
total_pages = first_data["total_pages"]

print("Total candidate results:", total_results)
print("Total candidate pages:", total_pages)


# --------------------------------------------------
# Collect all candidate pages
# --------------------------------------------------

all_movies = []

for page in range(1, total_pages + 1):

    response = requests.get(
        discover_url,
        headers=headers,
        params={**base_params, "page": page},
        timeout=30
    )

    response.raise_for_status()

    page_data = response.json()

    all_movies.extend(page_data["results"])

    print(
        f"Collected page {page}/{total_pages} "
        f"({len(page_data['results'])} movies)"
    )


# --------------------------------------------------
# Convert to DataFrame
# --------------------------------------------------

df = pd.DataFrame(all_movies)


# --------------------------------------------------
# Keep only fields we need for the candidate list
# --------------------------------------------------

candidate_columns = [
    "id",
    "title",
    "release_date",
    "vote_average",
    "vote_count",
    "popularity"
]

df = df[candidate_columns].copy()


# --------------------------------------------------
# Remove duplicate movie IDs just in case
# --------------------------------------------------

df = df.drop_duplicates(subset="id")


# --------------------------------------------------
# Save candidate list
# --------------------------------------------------

output_path = "data/animation_movie_candidates.csv"

df.to_csv(
    output_path,
    index=False
)


# --------------------------------------------------
# Final summary
# --------------------------------------------------

print()
print("=" * 60)
print("CANDIDATE DATASET CREATED")
print("=" * 60)

print("Unique candidate movies:", len(df))
print("Saved to:", output_path)

print()
print("First 10 candidates:")

print(
    df.head(10).to_string(index=False)
)
