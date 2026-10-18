import csv
import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()

# Project data file
csv_file = Path("data/animation_movie_countries_cleaned.csv")

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database="animation_bi"
)

cursor = connection.cursor()

# Read the CSV file
with csv_file.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    rows = []

    for row in reader:
        rows.append(
            (
                int(row["movie_id"]),
                row["country_code"],
                row["country_name"]
            )
        )

# Insert country relationship records into the staging table
insert_query = """
INSERT INTO countries_staging (
    movie_id,
    country_code,
    country_name
)
VALUES (%s, %s, %s)
"""

cursor.executemany(insert_query, rows)

connection.commit()

print(f"Rows loaded: {cursor.rowcount}")

cursor.close()
connection.close()
