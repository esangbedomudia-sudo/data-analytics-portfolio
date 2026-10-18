import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

# Load cleaned relationship data
genres = pd.read_csv(DATA_DIR / "animation_movie_genres_cleaned.csv")
companies = pd.read_csv(DATA_DIR / "animation_movie_companies_cleaned.csv")
countries = pd.read_csv(DATA_DIR / "animation_movie_countries_cleaned.csv")

# Create unique genre dimension
genre_dimension = (
    genres[["genre_id", "genre_name"]]
    .drop_duplicates()
    .sort_values("genre_id")
)

# Create unique production company dimension
company_dimension = (
    companies[["company_id", "company_name"]]
    .drop_duplicates()
    .sort_values("company_id")
)

# Create unique production country dimension
country_dimension = (
    countries[["country_code", "country_name"]]
    .drop_duplicates()
    .sort_values("country_code")
)

# Save dimension files
genre_dimension.to_csv(
    DATA_DIR / "genres.csv",
    index=False
)

company_dimension.to_csv(
    DATA_DIR / "production_companies.csv",
    index=False
)

country_dimension.to_csv(
    DATA_DIR / "production_countries.csv",
    index=False
)

print("=== DIMENSION FILES CREATED ===")
print()
print("Genres:", len(genre_dimension))
print("Production companies:", len(company_dimension))
print("Production countries:", len(country_dimension))
print()
print("Files created:")
print("- data/genres.csv")
print("- data/production_companies.csv")
print("- data/production_countries.csv")
