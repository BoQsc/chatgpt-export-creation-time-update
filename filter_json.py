import os
import shutil
import chardet

# Define the search term
search_term = "printf"

# Define the source directory and the destination directory as relative paths
source_directory = "json_files"
destination_directory = "filtered_files_json"

# Create the destination directory if it doesn't already exist
if not os.path.exists(destination_directory):
    os.mkdir(destination_directory)

# Loop through all files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith(".json"):
        # Read the contents of the file, auto-detecting the file encoding
        with open(os.path.join(source_directory, filename), "rb") as f:
            contents = f.read()
        detected_encoding = chardet.detect(contents)["encoding"]
        # Decode the file contents using the detected encoding
        with open(os.path.join(source_directory, filename), "r", encoding=detected_encoding, errors='ignore') as f:
            contents = f.read()
        # Check if the search term is in the contents
        if search_term in contents:
            # Copy the file to the destination directory
            shutil.copy(os.path.join(source_directory, filename), destination_directory)
