import os
import shutil

# --- CONFIGURATION ---
SOURCE_FOLDER = "../data/raw/ttl"      # folder with downloaded TTL files
DEST_FOLDER = "../data/raw/shacl"      # folder to copy SHACL files
SHACL_URI = "http://www.w3.org/ns/shacl#"

# Create destination folder if it doesn't exist
os.makedirs(DEST_FOLDER, exist_ok=True)

# Iterate over all files in source folder
for filename in os.listdir(SOURCE_FOLDER):
    file_path = os.path.join(SOURCE_FOLDER, filename)

    # Skip directories
    if not os.path.isfile(file_path):
        continue

    try:
        # Read file content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check for SHACL namespace
        if SHACL_URI in content:
            shutil.copy(file_path, DEST_FOLDER)
            print(f"Copied: {filename}")

    except Exception as e:
        print(f"Skipping {filename}: {e}")

print("Done! All SHACL files copied.")
