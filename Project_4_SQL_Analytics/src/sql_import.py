
import csv
from pathlib import Path

import mysql.connector

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CSV_FILE_PATH = (
    PROJECT_ROOT
    / "Project_1_Data_Collection"
    / "data"
    / "youtube_animation_data_expanded.csv"
)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hero#0Pass",
    database="youtube_animation_analytics",
)

cursor = connection.cursor()

insert_query = """
INSERT INTO youtube_videos (
    video_id, search_query, title, channel, published_at,
    views, likes, comments, publish_year, publish_month,
    title_length, engagement_total, engagement_ratio
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    search_query = VALUES(search_query),
    title = VALUES(title),
    channel = VALUES(channel),
    published_at = VALUES(published_at),
    views = VALUES(views),
    likes = VALUES(likes),
    comments = VALUES(comments),
    publish_year = VALUES(publish_year),
    publish_month = VALUES(publish_month),
    title_length = VALUES(title_length),
    engagement_total = VALUES(engagement_total),
    engagement_ratio = VALUES(engagement_ratio)
"""

try:
    if not CSV_FILE_PATH.is_file():
        raise FileNotFoundError(f"Dataset not found: {CSV_FILE_PATH}")

    with CSV_FILE_PATH.open(
        mode="r", encoding="utf-8", newline=""
    ) as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            cursor.execute(
                insert_query,
                (
                    row["video_id"],
                    row["search_query"],
                    row["title"],
                    row["channel"],
                    row["published_at"],
                    int(row["views"]),
                    int(row["likes"]),
                    int(row["comments"]),
                    int(row["publish_year"]),
                    int(row["publish_month"]),
                    int(row["title_length"]),
                    int(row["engagement_total"]),
                    float(row["engagement_ratio"]),
                ),
            )

    connection.commit()
    print("Data import completed successfully.")

except Exception:
    connection.rollback()
    raise

finally:
    cursor.close()
    connection.close()
