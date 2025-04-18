# YouTubeTrendingVideoPipeline
A simple pipeline to learn how ETL works.

# Implementation
1. Setup & tools
   - Tech stack:
     - Language: Python
     - API: [YouTube Data API v3](https://developers.google.com/youtube/v3)
     - Storage: PostgreSQL or CSV files
     - Scheduling: Airflow
     - Dashboard: Streamlit/PowerBI/Tableau
  
2. Create Google Cloud Storage & YouTube Data API Access
   - Go to [Google Cloud](https://cloud.google.com/), use your Google account to start a new Google Cloud workspace.
   - Verify your identity (requires payments profile).
   - Go to [Google Cloud Console](https://console.cloud.google.com/), create a new project.
   - Enable `YouTube Data API v3`
   - Create an API key
   - Install Python client:
     ```
     pip install google-api-python-client
     ```
  
4. Execute `youtube_trending.py` script to extract trending videos to a CSV file
