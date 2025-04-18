import os
import json

def read_json_files(folder_path):
    json_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            with open(os.path.join(folder_path, filename), 'r') as file:
                try:
                    data = json.load(file)
                    json_data.append(data)
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON file: {filename}")
    return json_data


