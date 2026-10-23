
import re
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# Define project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_FILE = (
    PROJECT_ROOT
    / "Project_1_Data_Collection"
    / "data"
    / "youtube_animation_data_expanded.csv"
)

VISUALS_DIR = PROJECT_ROOT / "Project_3_Title_Strategy_Analysis" / "visuals"
VISUALS_DIR.mkdir(parents=True, exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_FILE)

# Clean titles
df["clean_title"] = df["title"].fillna("").str.lower()
df["clean_title"] = df["clean_title"].apply(
    lambda title: re.sub(r"[^a-z0-9\s]", "", title)
)

# Split titles into words
df["words"] = df["clean_title"].apply(lambda title: title.split())

# Stopwords
stopwords = {
    "the", "a", "to", "by", "for", "is", "and", "of", "in", "on", "with"
}

# Collect views per word
word_views = defaultdict(list)

for _, row in df.iterrows():
    words = set(row["words"])

    for word in words:
        if word not in stopwords:
            word_views[word].append(row["views"])

# Calculate average views per word
avg_word_views = []

for word, views in word_views.items():
    if len(views) >= 5:
        avg_word_views.append((word, sum(views) / len(views)))

# Sort by average views, highest first
avg_word_views = sorted(
    avg_word_views,
    key=lambda item: item[1],
    reverse=True
)

# Select top 10 words
top_words = avg_word_views[:10]

if not top_words:
    raise ValueError(
        "No words have at least five videos associated with them."
    )

words = [word for word, _ in top_words]
views = [average_views for _, average_views in top_words]

# Create chart
plt.figure(figsize=(10, 6))
plt.barh(words, views)
plt.title("Top Words by Average Views")
plt.xlabel("Average Views")
plt.gca().invert_yaxis()
plt.tight_layout()

# Save chart
chart_path = VISUALS_DIR / "title_word_performance.png"
plt.savefig(chart_path, dpi=150, bbox_inches="tight")
plt.close()

print(f"\nLoaded dataset: {DATA_FILE}")
print(f"Videos analyzed: {len(df)}")
print(f"Words meeting the minimum of five videos: {len(avg_word_views)}")
print(f"Saved chart: {chart_path}")
