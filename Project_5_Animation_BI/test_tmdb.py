import os
import requests
from dotenv import load_dotenv

# Load the variables stored in the .env file
load_dotenv()

# Retrieve the TMDB Read Access Token
token = os.getenv("TMDB_READ_ACCESS_TOKEN")

# Make sure the token exists
if not token:
    raise RuntimeError(
        "TMDB_READ_ACCESS_TOKEN was not found. "
        "Check that your .env file exists and contains the token."
    )

# TMDB movie endpoint
# Movie ID 862 is Toy Story
url = "https://api.themoviedb.org/3/movie/862"

# Authentication information
headers = {
    "Authorization": f"Bearer {token}",
    "accept": "application/json"
}

# Send the request to TMDB
response = requests.get(
    url,
    headers=headers,
    params={"language": "en-US"},
    timeout=30
)

# Raise an error if TMDB rejects the request
response.raise_for_status()

# Convert TMDB's JSON response into a Python dictionary
movie = response.json()

# Display a few fields so we can confirm everything worked
print("TMDB connection successful!")
print("Title:", movie.get("title"))
print("Release date:", movie.get("release_date"))
print("Budget:", movie.get("budget"))
print("Revenue:", movie.get("revenue"))
print("Rating:", movie.get("vote_average"))
