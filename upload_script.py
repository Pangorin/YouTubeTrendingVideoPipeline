from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    # Uploads a file to the bucket.
    # ID of the GCS bucket
    bucket_name = 'youtube-trending-data-bucket'
    # Path to local file
    source_file_name = 'youtube_trending.csv'
    # ID of GCS object
    destination_blob_name = 'youtube_trending.csv'
    
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    
    blob.upload_from_filename(source_file_name)
    
    print(f'File {source_file_name} uploaded to {destination_blob_name} in {bucket_name}.')
    
if __name__ == "__main__":
    bucket_name = 'youtube-trending-data-bucket'
    source_file_name = 'youtube_trending.csv'
    destination_blob_name = 'youtube_trending.csv'
    
    upload_blob('youtube-trending-data-bucket', 'youtube_trending.csv', 'youtube_trending.csv')