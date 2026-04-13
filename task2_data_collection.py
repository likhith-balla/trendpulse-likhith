from google.colab import files
import os

# Create the 'data' directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Upload files
uploaded = files.upload()

for filename in uploaded.keys():
    # Move the uploaded file to the 'data' directory
    destination_path = os.path.join('data', filename)
    os.rename(filename, destination_path)
    print(f'Moved file "{filename}" to "{destination_path}"')

import pandas as pd

# Load the JSON file from the data/ folder
df = pd.read_json("data/trends_20260413.json")

# Print how many rows were loaded
print(f"Loaded {len(df)} rows.")

# 1. Remove duplicates based on post_id
df = df.drop_duplicates(subset="post_id")

# 2. Drop rows where post_id, title, or score is missing
df = df.dropna(subset=["post_id", "title", "score"])

# 3. Convert score and num_comments to integers
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# 4. Remove low-quality stories (score < 5)
df = df[df["score"] >= 5]

# 5. Strip extra whitespace from title column
df["title"] = df["title"].str.strip()

# Print number of rows remaining after cleaning
print(f"Rows remaining after cleaning: {len(df)}")

# Save the cleaned DataFrame to CSV
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)

# Print confirmation message
print(f"Saved {len(df)} rows to {output_file}")

# Print stories per category
print("\nStories per category:")
print(df["category"].value_counts())

