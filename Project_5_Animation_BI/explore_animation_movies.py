import os
import requests
from dotenv import load_dotenv

# Load the TMDB Read Access Token from .env
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
# 1. Get TMDB's official movie genre list
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

# Find the Animation genre
animation_genre = next(
    (genre for genre in genres if genre["name"] == "Animation"),
    None
)

if animation_genre is None:
    raise RuntimeError("Animation genre was not found.")

animation_genre_id = animation_genre["id"]

print("Animation genre ID:", animation_genre_id)


# --------------------------------------------------
# 2. Discover movies in the Animation genre
# --------------------------------------------------

discover_url = "https://api.themoviedb.org/3/discover/movie"

params = {
    "language": "en-US",
    "include_adult": "false",
    "page": 1,
    "sort_by": "popularity.desc",
    "with_genres": animation_genre_id
}

discover_response = requests.get(
    discover_url,
    headers=headers,
    params=params,
    timeout=30
)

discover_response.raise_for_status()

data = discover_response.json()

print("Total results:", data["total_results"])
print("Total pages:", data["total_pages"])
print()


# --------------------------------------------------
# 3. Display the first 10 movies
# --------------------------------------------------

print("First 10 animated movies returned:")
print("-" * 60)

for movie in data["results"][:10]:

    print(
        f"ID: {movie.get('id')} | "
        f"Title: {movie.get('title')} | "
        f"Release: {movie.get('release_date')} | "
        f"Rating: {movie.get('vote_average')} | "
        f"Votes: {movie.get('vote_count')}"
    )
