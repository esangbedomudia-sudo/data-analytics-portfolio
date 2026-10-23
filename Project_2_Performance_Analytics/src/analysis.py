from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Resolve paths relative to the portfolio repository.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = (
    PROJECT_ROOT
    / "Project_1_Data_Collection"
    / "data"
    / "youtube_animation_data_expanded.csv"
)
VISUALS_DIR = PROJECT_ROOT / "Project_2_Performance_Analytics" / "visuals"
VISUALS_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_FILE)

print("\nTop 10 videos by views:")
print(
    df[["title", "channel", "views"]]
    .sort_values(by="views", ascending=False)
    .head(10)
)

print("\nTop 10 videos by engagement:")
print(
    df[["title", "channel", "engagement_total"]]
    .sort_values(by="engagement_total", ascending=False)
    .head(10)
)

print("\nTop 10 videos by engagement ratio:")
print(
    df[["title", "channel", "engagement_ratio"]]
    .sort_values(by="engagement_ratio", ascending=False)
    .head(10)
)

print("\nAverage views by year:")
print(df.groupby("publish_year")["views"].mean().sort_index())

print("\nMedian views by year:")
print(df.groupby("publish_year")["views"].median().sort_index())

print("\nAverage engagement ratio by year:")
print(df.groupby("publish_year")["engagement_ratio"].mean().sort_index())

print("\nAverage views by month:")
print(df.groupby("publish_month")["views"].mean().sort_index())

print("\nAverage views by search query:")
print(
    df.groupby("search_query")["views"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage engagement ratio by search query:")
print(
    df.groupby("search_query")["engagement_ratio"]
    .mean()
    .sort_values(ascending=False)
)

# Top 10 videos by views
top_views = df.sort_values(by="views", ascending=False).head(10)

plt.figure()
plt.barh(top_views["title"], top_views["views"])
plt.xlabel("Views")
plt.title("Top 10 Animation Videos by Views")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(VISUALS_DIR / "top_views.png")
plt.close()

# Engagement ratio distribution
plt.figure()
plt.hist(df["engagement_ratio"], bins=10)
plt.title("Distribution of Engagement Ratio")
plt.xlabel("Engagement Ratio")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(VISUALS_DIR / "engagement_distribution.png")
plt.close()

# Average views by search query
query_views = df.groupby("search_query")["views"].mean().sort_values()

plt.figure()
plt.barh(query_views.index, query_views.values)
plt.title("Average Views by Content Type")
plt.xlabel("Average Views")
plt.tight_layout()
plt.savefig(VISUALS_DIR / "views_by_type.png")
plt.close()

print(f"\nSaved charts to: {VISUALS_DIR}")
