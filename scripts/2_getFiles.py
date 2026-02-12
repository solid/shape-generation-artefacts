import os
import requests
from urllib.parse import urlparse, unquote
import re


DATA_FILEPATH = "../data/"
DATA_FILE = "list.txt"

FILE_FILEPATH = "../data/raw/ttl"


# Path to the results file
results_file = "1_results.txt"

# Create file folder if it doesn't exist
os.makedirs(FILE_FILEPATH, exist_ok=True)

# Convert GitHub blob URL to raw URL
def github_raw_url(url):
    if "github.com" not in url:
        return url
    url = url.replace("github.com", "raw.githubusercontent.com")
    url = url.replace("/blob/", "/")
    return url

# Generate a clean slugified filename without commit hashes
def slugify_clean(url):
    """
    Converts a GitHub URL path to a safe filename without commit hash.
    """
    path = urlparse(url).path.lstrip("/")

    # Split the path into parts
    parts = path.split("/")

    # Remove the commit hash if this is a blob URL: <repo>/blob/<hash>/path...
    if "blob" in parts:
        blob_index = parts.index("blob")
        # Keep repo name + file path, remove the hash
        parts = parts[:blob_index] + parts[blob_index + 2:]

    # Join the remaining path parts with underscores
    slug = "_".join(parts)

    # Replace unsafe characters with underscores
    slug = re.sub(r'[^0-9a-zA-Z]+', '_', slug)

    # Ensure it ends with .ttl
    if not slug.endswith(".ttl"):
        slug += ".ttl"

    return slug

# Read the results file
with open(os.path.join(DATA_FILEPATH, DATA_FILE), "r", encoding="utf-8") as f:
    lines = f.readlines()

# Extract URLs
urls = [line.strip() for line in lines if line.startswith("http")]

for url in urls:
    try:
        raw_url = github_raw_url(url)
        print(f"Downloading: {raw_url}")

        # Fetch file content
        response = requests.get(raw_url)
        response.raise_for_status()

        # Generate clean slug filename
        filename = slugify_clean(url)
        local_path = os.path.join(FILE_FILEPATH, filename)

        # Save the file
        with open(local_path, "wb") as f:
            f.write(response.content)

    except Exception as e:
        print(f"Failed to download {url}: {e}")

print("All files downloaded!")
