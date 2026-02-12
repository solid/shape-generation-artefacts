import os
import time
import requests
from dotenv import load_dotenv

# Load .env.local
load_dotenv("../.env.local")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
ORG_NAME = "SolidOS"
DATA_FILEPATH = "../data/"
DATA_FILE = "list.txt"

if not GITHUB_TOKEN:
    raise ValueError("GitHub token not found. Make sure it's set in .env.local")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def search_all_ttl():
    ttl_files = []
    page = 1

    while True:
        url = "https://api.github.com/search/code"
        params = {
            "q": f"org:{ORG_NAME} extension:ttl",
            "per_page": 100,
            "page": page
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            print("Error:", response.json())
            break

        data = response.json()
        items = data.get("items", [])

        if not items:
            break

        for item in items:
            ttl_files.append({
                "repo": item["repository"]["name"],
                "path": item["path"],
                "url": item["html_url"]
            })

        if len(items) < 100:
            break

        page += 1
        time.sleep(3)  # stay under 30/min search API rate limit

    return ttl_files


def main():
    print(f"Searching all repositories in {ORG_NAME} for .ttl files...\n")
    ttl_files = search_all_ttl()

    # Write results to listFiles.txt
    with open(os.path.join(DATA_FILEPATH, DATA_FILE), "w", encoding="utf-8") as f:
        f.write(f"Total .ttl files found: {len(ttl_files)}\n\n")
        for file in ttl_files:
            f.write(f"{file['repo']} | {file['path']}\n")
            f.write(f"{file['url']}\n\n")

    print(f"Results saved to {DATA_FILE}")
    print(f"Total .ttl files found: {len(ttl_files)}")


if __name__ == "__main__":
    main()
