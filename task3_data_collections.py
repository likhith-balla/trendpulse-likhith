import pandas as pd

# Load data/trends_clean.csv into a Pandas DataFrame
df_clean = pd.read_csv("data/trends_clean.csv")

# Print the first 5 rows
print("First 5 rows of the DataFrame:")
display(df_clean.head())

# Print the shape of the DataFrame (rows and columns)
print(f"Shape of the DataFrame (rows, columns): {df_clean.shape}")

# Print the average score and average num_comments across all stories
avg_score = df_clean['score'].mean()
avg_comments = df_clean['num_comments'].mean()

print(f"Average Score: {avg_score:.2f}")
print(f"Average Number of Comments: {avg_comments:.2f}")

# Calculate mean, median, and standard deviation of 'score'
mean_score = df_clean['score'].mean()
median_score = df_clean['score'].median()
std_dev_score = df_clean['score'].std()

print(f"Mean Score: {mean_score:.2f}")
print(f"Median Score: {median_score:.2f}")
print(f"Standard Deviation of Score: {std_dev_score:.2f}")

# Find the highest and lowest score
highest_score = df_clean['score'].max()
lowest_score = df_clean['score'].min()

print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")

# Find the category with the most stories
most_stories_category = df_clean['category'].value_counts().idxmax()
num_stories_in_category = df_clean['category'].value_counts().max()

print(f"Category with the most stories: '{most_stories_category}' with {num_stories_in_category} stories.")

# Find the story with the most comments
story_most_comments = df_clean.loc[df_clean['num_comments'].idxmax()]

print("Story with the most comments:")
print(f"  Title: {story_most_comments['title']}")
print(f"  Comment Count: {story_most_comments['num_comments']}")

# Add 'engagement' column
df_clean['engagement'] = df_clean['num_comments'] / (df_clean['score'] + 1)

# Add 'is_popular' column
df_clean['is_popular'] = df_clean['score'] > df_clean['score'].mean()

# Display the DataFrame with the new columns
print("DataFrame with new columns:")
display(df_clean.head())

output_file_analysed = "data/trends_analysed.csv"
df_clean.to_csv(output_file_analysed, index=False)

print(f"Saved the updated DataFrame with {len(df_clean)} rows to {output_file_analysed}")

