import os
import requests

# URL of the Parquet file
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-05.parquet"

# Create folder if it doesn't exist
output_dir = "data/raw"
os.makedirs(output_dir, exist_ok=True)

# Filepath to save
output_file = os.path.join(output_dir, "yellow_tripdata_2025-05.parquet")

print("Downloading file...")
r = requests.get(url, stream=True)
with open(output_file, "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)

print(f"Download complete: {output_file}")
