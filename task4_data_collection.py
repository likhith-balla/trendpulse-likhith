import pandas as pd
import os

# Load the analysed data into a DataFrame
df_analysed = pd.read_csv('data/trends_analysed.csv')

# Display the first 5 rows to confirm loading
print("First 5 rows of df_analysed:")
display(df_analysed.head())

# Create the 'outputs' directory if it doesn't exist
output_dir = 'outputs'
os.makedirs(output_dir, exist_ok=True)
print(f"Directory '{output_dir}' ensured.")

import matplotlib.pyplot as plt
import seaborn as sns
import os

# Sort by score and get the top 10 stories
top_10_stories = df_analysed.sort_values(by='score', ascending=False).head(10)

# Shorten titles for better visualization on the y-axis
top_10_stories['short_title'] = top_10_stories['title'].apply(lambda x: x[:50] + '...' if len(x) > 50 else x)

# Create the horizontal bar chart
plt.figure(figsize=(12, 8))
sns.barplot(x='score', y='short_title', data=top_10_stories, palette='viridis')

# Add title and labels
plt.title('Top 10 Stories by Score')
plt.xlabel('Score')
plt.ylabel('Story Title')
plt.tight_layout() # Adjust layout to prevent labels from overlapping

# Save the plot before showing it
output_path = os.path.join('outputs', 'chart1_top_stories.png')
plt.savefig(output_path)
print(f"Chart saved to {output_path}")

# Display the plot
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import os

# Count stories per category
category_counts = df_analysed['category'].value_counts().reset_index()
category_counts.columns = ['category', 'count']

# Create the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='count', data=category_counts, palette='Paired')

# Add title and labels
plt.title('Number of Stories Per Category')
plt.xlabel('Category')
plt.ylabel('Number of Stories')
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.tight_layout() # Adjust layout to prevent labels from overlapping

# Save the plot before showing it
output_path = os.path.join('outputs', 'chart2_categories.png')
plt.savefig(output_path)
print(f"Chart saved to {output_path}")

# Display the plot
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create the scatter plot
plt.figure(figsize=(10, 7))
sns.scatterplot(x='score', y='num_comments', hue='is_popular', data=df_analysed, palette='coolwarm', s=100)

# Add title and labels
plt.title('Story Score vs. Number of Comments (Popularity Highlighted)')
plt.xlabel('Score')
plt.ylabel('Number of Comments')

# Add a legend
plt.legend(title='Is Popular')
plt.grid(True, linestyle='--', alpha=0.7)

# Save the plot before showing it
output_path = os.path.join('outputs', 'chart3_scatter.png')
plt.savefig(output_path)
print(f"Chart saved to {output_path}")

# Display the plot
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create a figure and a set of subplots
fig, axes = plt.subplots(1, 3, figsize=(24, 7)) # 1 row, 3 columns
fig.suptitle('TrendPulse Dashboard', fontsize=16) # Overall title

# --- Chart 1: Top 10 Stories by Score ---
# Sort by score and get the top 10 stories
top_10_stories = df_analysed.sort_values(by='score', ascending=False).head(10)
top_10_stories['short_title'] = top_10_stories['title'].apply(lambda x: x[:50] + '...' if len(x) > 50 else x)

sns.barplot(x='score', y='short_title', data=top_10_stories, palette='viridis', ax=axes[0])
axes[0].set_title('Top 10 Stories by Score')
axes[0].set_xlabel('Score')
axes[0].set_ylabel('Story Title')

# --- Chart 2: Number of Stories Per Category ---
# Count stories per category
category_counts = df_analysed['category'].value_counts().reset_index()
category_counts.columns = ['category', 'count']

sns.barplot(x='category', y='count', data=category_counts, palette='Paired', ax=axes[1])
axes[1].set_title('Number of Stories Per Category')
axes[1].set_xlabel('Category')
axes[1].set_ylabel('Number of Stories')
axes[1].tick_params(axis='x', rotation=45) # Removed ha='right'

# --- Chart 3: Story Score vs. Number of Comments (Popularity Highlighted) ---
sns.scatterplot(x='score', y='num_comments', hue='is_popular', data=df_analysed, palette='coolwarm', s=100, ax=axes[2])
axes[2].set_title('Story Score vs. Number of Comments (Popularity Highlighted)')
axes[2].set_xlabel('Score')
axes[2].set_ylabel('Number of Comments')
axes[2].legend(title='Is Popular')
axes[2].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to prevent title overlap

# Save the dashboard
output_path = os.path.join('outputs', 'dashboard.png')
plt.savefig(output_path)
print(f"Dashboard saved to {output_path}")

# Display the dashboard
plt.show()
