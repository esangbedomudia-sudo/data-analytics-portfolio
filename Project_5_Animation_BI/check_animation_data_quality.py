import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

# Load the TMDB Read Access Token
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
# 1. Get the Animation genre ID
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
# 2. Get the first 20 popular animated movies
# --------------------------------------------------

discover_url = "https://api.themoviedb.org/3/discover/movie"

discover_params = {
    "language": "en-US",
    "include_adult": "false",
    "page": 1,
    "sort_by": "popularity.desc",
    "with_genres": animation_genre_id
}

discover_response = requests.get(
    discover_url,
    headers=headers,
    params=discover_params,
    timeout=30
)

discover_response.raise_for_status()

movies = discover_response.json()["results"][:20]

print(f"Movies selected for inspection: {len(movies)}")


# --------------------------------------------------
# 3. Retrieve detailed information for each movie
# --------------------------------------------------

records = []

for number, movie in enumerate(movies, start=1):

    movie_id = movie["id"]

    detail_url = (
        f"https://api.themoviedb.org/3/movie/{movie_id}"
    )

    detail_response = requests.get(
        detail_url,
        headers=headers,
        params={"language": "en-US"},
        timeout=30
    )

    detail_response.raise_for_status()

    detail = detail_response.json()

    production_companies = detail.get(
        "production_companies", []
    )

    genres = detail.get("genres", [])

    records.append({
        "movie_id": detail.get("id"),
        "title": detail.get("title"),
        "release_date": detail.get("release_date"),
        "runtime": detail.get("runtime"),
        "budget": detail.get("budget"),
        "revenue": detail.get("revenue"),
        "vote_average": detail.get("vote_average"),
        "vote_count": detail.get("vote_count"),
        "popularity": detail.get("popularity"),
        "original_language": detail.get(
            "original_language"
        ),
        "genre_count": len(genres),
        "production_company_count": len(
            production_companies
        ),
        "production_country_count": len(
            detail.get("production_countries", [])
        )
    })

    print(f"Processed {number}/20: {detail.get('title')}")

    # Small pause between requests
    time.sleep(0.1)


# --------------------------------------------------
# 4. Create a DataFrame
# --------------------------------------------------

df = pd.DataFrame(records)


# --------------------------------------------------
# 5. Check missing values
# --------------------------------------------------

print()
print("=" * 60)
print("DATA QUALITY RESULTS")
print("=" * 60)

print()
print("Total movies inspected:", len(df))

print()
print("Missing values:")
print(df.isna().sum())

print()
print("Budget values equal to zero:", (df["budget"] == 0).sum())
print("Revenue values equal to zero:", (df["revenue"] == 0).sum())
print("Runtime values equal to zero:", (df["runtime"] == 0).sum())

print()
print("Average vote count:", round(df["vote_count"].mean(), 2))

print()
print("Movies with production companies:",
      (df["production_company_count"] > 0).sum(),
      "out of", len(df))

print()
print("Movies with genres:",
      (df["genre_count"] > 0).sum(),
      "out of", len(df))

print()
print("Movies with production countries:",
      (df["production_country_count"] > 0).sum(),
      "out of", len(df))
