import pandas as pd
from youtube_trending import publishedAt

def clean_youtube_data(df):
    # Convert publish_time to datetime
    df[publishedAt] = pd.to_datetime(df[publishedAt])
    
    # Extract publish date and hour
    df['publish_date'] = df[publishedAt].dt.date
    df['publish_hour'] = df[publishedAt].dt.hour
    
    # Fill missing values in tags
    df['tags'] = df['tags'].fillna['No Tags']
    
    # Filter low-view videos
    df['views'] = df['views'].astype(int)
    df = df[df['views'] > 10000]
    
    return df