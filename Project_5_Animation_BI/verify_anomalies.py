import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TMDB_READ_ACCESS_TOKEN")

if not token:
    raise RuntimeError(
        "TMDB_READ_ACCESS_TOKEN was not found. "
        "Check that your .env file exists and contains the token."
    )

MOVIE_IDS = [
    33065,
    33534,
    52939,
    552095,
    337302,
]

headers = {
    "Authorization": f"Bearer {token}",
    "accept": "application/json"
}

print("\n=== TMDB ANOMALY VERIFICATION ===")

for movie_id in MOVIE_IDS:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    response = requests.get(
        url,
        headers=headers,
        params={"language": "en-US"},
        timeout=30
    )

    response.raise_for_status()
    movie = response.json()

    print("\n" + "=" * 70)
    print(f"Movie ID: {movie.get('id')}")
    print(f"Title: {movie.get('title')}")
    print(f"Release date: {movie.get('release_date')}")
    print(f"Runtime: {movie.get('runtime')}")
    print(f"Budget: {movie.get('budget')}")
    print(f"Revenue: {movie.get('revenue')}")
    print(f"Rating: {movie.get('vote_average')}")
    print(f"Vote count: {movie.get('vote_count')}")
    print(f"Popularity: {movie.get('popularity')}")
    print(f"Original language: {movie.get('original_language')}")

    print("\nGenres:")
    for genre in movie.get("genres", []):
        print(f"- {genre.get('name')}")

    print("\nProduction companies:")
    production_companies = movie.get("production_companies", [])

    if production_companies:
        for company in production_companies:
            print(
                f"- {company.get('name')} "
                f"(ID: {company.get('id')})"
            )
    else:
        print("- NONE")

    print("\nProduction countries:")
    production_countries = movie.get("production_countries", [])

    if production_countries:
        for country in production_countries:
            print(
                f"- {country.get('name')} "
                f"({country.get('iso_3166_1')})"
            )
    else:
        print("- NONE")

print("\n" + "=" * 70)
print("=== VERIFICATION COMPLETE ===")
