import pandas as pd

# Load the candidate dataset
file_path = "data/animation_movie_candidates.csv"
df = pd.read_csv(file_path)

print("\n=== CANDIDATE DATASET INSPECTION ===")

# Basic size
print(f"\nRows: {len(df)}")
print(f"Columns: {len(df.columns)}")

# Column names
print("\nColumns:")
for column in df.columns:
    print(f"- {column}")

# Duplicate IDs
duplicate_ids = df["id"].duplicated().sum()
print(f"\nDuplicate movie IDs: {duplicate_ids}")

# Missing values
print("\nMissing values:")
missing_values = df.isnull().sum()

for column, count in missing_values.items():
    print(f"- {column}: {count}")

# Convert release date
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

# Date range
print("\nRelease date range:")
print(f"Earliest: {df['release_date'].min().date()}")
print(f"Latest:   {df['release_date'].max().date()}")

# Year distribution
df["release_year"] = df["release_date"].dt.year

print("\nMovies by release year:")
year_counts = df["release_year"].value_counts().sort_index()

for year, count in year_counts.items():
    print(f"- {int(year)}: {count}")

# Vote count statistics
print("\nVote count statistics:")
print(f"Minimum: {df['vote_count'].min():,.0f}")
print(f"Maximum: {df['vote_count'].max():,.0f}")
print(f"Average: {df['vote_count'].mean():,.1f}")
print(f"Median:  {df['vote_count'].median():,.1f}")

# Rating statistics
print("\nVote average statistics:")
print(f"Minimum: {df['vote_average'].min():.2f}")
print(f"Maximum: {df['vote_average'].max():.2f}")
print(f"Average: {df['vote_average'].mean():.2f}")
print(f"Median:  {df['vote_average'].median():.2f}")

# Lowest-vote candidates
print("\n10 movies with the lowest vote counts:")
lowest_votes = df.sort_values("vote_count").head(10)

for _, row in lowest_votes.iterrows():
    print(
        f"- {row['title']} | "
        f"Votes: {int(row['vote_count']):,} | "
        f"Rating: {row['vote_average']:.2f}"
    )

# Highest-vote candidates
print("\n10 movies with the highest vote counts:")
highest_votes = df.sort_values("vote_count", ascending=False).head(10)

for _, row in highest_votes.iterrows():
    print(
        f"- {row['title']} | "
        f"Votes: {int(row['vote_count']):,} | "
        f"Rating: {row['vote_average']:.2f}"
    )

print("\n=== INSPECTION COMPLETE ===")
