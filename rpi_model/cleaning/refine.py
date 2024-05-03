import csv
import os

# Open the CSV file
csv_file_path = r"C:\Users\Biancaa. R\rpi_disease\pest_classification\training_set.csv"
with open(csv_file_path, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    categories = {row[0]: row[1] for row in reader}

# Define source and destination directories
source_dir = r"C:\Users\Biancaa. R\rpi_disease\pest_classification\training_dataset"
destination_dir = r"C:\Users\Biancaa. R\rpi_disease\pest_classification\images"

# Move files to appropriate folders
for filename in os.listdir(source_dir):
    if filename in categories:
        category = categories[filename]
        source_file_path = os.path.join(source_dir, filename)
        destination_file_path = os.path.join(destination_dir, category, filename)
        os.rename(source_file_path, destination_file_path)

print("Done")
