import requests
import pandas as pd
import os

API_KEY = os.getenv("YOUTUBE_API_KEY")
REGION = 'VN'
MAX_RESULTS = 50

url = (
    f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics"
    f"&chart=mostPopular&regionCode={REGION}&maxResults={MAX_RESULTS}&key={API_KEY}"
)

response = requests.get(url)
data = response.json()

videos = []
for item in data['items']:
    video = {
        'title': item['snippet']['title'],
        'channel': item['snippet']['channelTitle'],
        'publishedAt': item['snippet']['publishedAt'],
        'views': item['statistics'].get('viewCount', 0),
        'likes': item['statistics'].get('likeCount', 0),
        'dislikes': item['statistics'].get('dislikeCount', 0),
        'comments': item['statistics'].get('commentCount', 0),
        'categoryId': item['snippet']['categoryId'],
    }
    videos.append(video)
    
df = pd.DataFrame(videos)
df.to_csv('youtube_trending.csv', index=False)
print("Data saved to youtube_trending.csv")

