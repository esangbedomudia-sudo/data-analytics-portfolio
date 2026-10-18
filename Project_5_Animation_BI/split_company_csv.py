import csv
from pathlib import Path

data_folder = Path("data")

source_file = data_folder / "animation_movie_companies_cleaned.csv"

rows_per_file = 1000

with source_file.open("r", encoding="utf-8", newline="") as infile:
    reader = csv.reader(infile)
    header = next(reader)

    file_number = 1
    row_count = 0
    output_file = None
    writer = None

    for row in reader:
        if row_count % rows_per_file == 0:
            if output_file:
                output_file.close()

            output_path = data_folder / f"companies_part{file_number}.csv"

            output_file = output_path.open(
                "w",
                encoding="utf-8",
                newline=""
            )

            writer = csv.writer(output_file)
            writer.writerow(header)

            file_number += 1

        writer.writerow(row)
        row_count += 1

    if output_file:
        output_file.close()

print(f"Total data rows split: {row_count}")
print(f"Files created: {file_number - 1}")
