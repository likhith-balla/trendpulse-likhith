import requests

headers = {"User-Agent": "TrendPulse/1.0"}
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    story_ids = response.json()
    story_ids = story_ids[:500]
else:
    print("Failed to fetch story IDs")
    story_ids = []

stories = []

for story_id in story_ids:
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            story = response.json()
            stories.append(story)
        else:
            print(f"Failed to fetch story {story_id}")
    except Exception as e:
        print(f"Error fetching story {story_id}: {e}")

import time
from datetime import datetime
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

collected_stories = []
collected_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
for category, keywords in categories.items():
    count = 0

    for story in stories:
        title = story.get("title", "").lower()

        if any(keyword in title for keyword in keywords):
            collected_stories.append({
                "post_id": story.get("id"),
                "title": story.get("title"),
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", "unknown"),
                "collected_at": collected_at
            })
            count += 1

        if count == 25:
            break
    time.sleep(2)   

import os
import json
os.makedirs("data", exist_ok=True)
date_str = datetime.now().strftime("%Y%m%d")
file_path = f"data/trends_{date_str}.json"
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(collected_stories, file, indent=4)
print(f"Collected {len(collected_stories)} stories. Saved to {file_path}")

