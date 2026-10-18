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

# Inside Out's TMDB movie ID
movie_id = 150540

url = f"https://api.themoviedb.org/3/movie/{movie_id}"

params = {
    "language": "en-US"
}

response = requests.get(
    url,
    headers=headers,
    params=params,
    timeout=30
)

response.raise_for_status()

movie = response.json()

print("Movie details successfully retrieved!")
print()

print("Title:", movie.get("title"))
print("Release date:", movie.get("release_date"))
print("Runtime:", movie.get("runtime"))
print("Budget:", movie.get("budget"))
print("Revenue:", movie.get("revenue"))
print("Rating:", movie.get("vote_average"))
print("Vote count:", movie.get("vote_count"))
print("Popularity:", movie.get("popularity"))
print("Original language:", movie.get("original_language"))
print()

print("Genres:")
for genre in movie.get("genres", []):
    print(f"  - {genre['name']}")

print()

print("Production companies:")
for company in movie.get("production_companies", []):
    print(f"  - {company['name']} (ID: {company['id']})")

print()

print("Production countries:")
for country in movie.get("production_countries", []):
    print(f"  - {country['name']} ({country['iso_3166_1']})")
