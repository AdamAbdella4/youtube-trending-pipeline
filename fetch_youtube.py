from dotenv import load_dotenv
import os
import requests



# Load environment variables from .env file
load_dotenv()

# Get API key
API_KEY = os.getenv("YOUTUBE_API_KEY")
if not API_KEY:
    print("API key not found. Make sure it's in your .env file.")
    exit()

# Define API request
url = 'https://www.googleapis.com/youtube/v3/videos'
params = {
    'part': 'snippet,statistics',
    'chart': 'mostPopular',
    'regionCode': 'US',
    'maxResults': 10,
    'key': API_KEY
}

# Make the request
response = requests.get(url, params=params)

# Error check
if response.status_code != 200:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
    exit()

# Parse the data
data = response.json()
import json
from datetime import datetime
# Create a filename based on timestamp
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = f"youtube_trending_{timestamp}.json"
# Save the response data to a JSON file
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)
print(f"Data saved locally as {filename}")

# Create a filename with today's date
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = f"youtube_trending_{timestamp}.json"

# Save data to local file
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)
print(f"✅ Data saved locally as {filename}")

# Print video titles and views
for video in data['items']:
    title = video['snippet']['title']
    views = video['statistics'].get('viewCount', 'N/A')
    print(f"{title} - {views} views")