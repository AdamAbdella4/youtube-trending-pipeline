import json
from datetime import datetime
import os

# Load the latest raw file (update this manually for now)
raw_filename = 'youtube_trending_2025-05-30_19-29-46.json'

# Load raw JSON data
with open(raw_filename, 'r') as f:
    raw_data = json.load(f)

# Extract useful fields only
cleaned_data = []

for video in raw_data['items']:
    cleaned_data.append({
        'videoId': video['id'],
        'title': video['snippet']['title'],
        'channel': video['snippet']['channelTitle'],
        'publishedAt': video['snippet']['publishedAt'],
        'viewCount': video['statistics'].get('viewCount', None),
        'likeCount': video['statistics'].get('likeCount', None),
        'commentCount': video['statistics'].get('commentCount', None),
    })

# Save cleaned data
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
processed_filename = f"youtube_trending_cleaned_{timestamp}.json"

with open(processed_filename, 'w') as f:
    for row in cleaned_data:
        json.dump(row, f)
        f.write('\n')  # write one JSON object per line

print(f"Cleaned data saved as {processed_filename}")
