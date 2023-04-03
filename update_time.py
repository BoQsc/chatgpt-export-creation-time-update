import os
import json

json_dir = "filtered_files_json/"
markdown_dir = "filtered_files/"

for json_file in os.listdir(json_dir):
    if json_file.endswith(".json"):
        json_basename = os.path.splitext(json_file)[0]
        markdown_file = os.path.join(markdown_dir, f"{json_basename}.md")
        with open(os.path.join(json_dir, json_file), encoding="utf-8") as f:
            try:
                data = json.load(f)
                create_time = data["create_time"]
                try:
                    os.utime(markdown_file, (create_time, create_time))
                except FileNotFoundError:
                    print(f"File not found: {markdown_file}")
            except json.JSONDecodeError as e:
                print(f"Error decoding {json_file}: {e}")
                continue
