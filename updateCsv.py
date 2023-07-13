import json
import csv
import os

from datetime import datetime


def update_csv_with_json(csv_file, json_file):
    existing_data = []
    if os.path.isfile(csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            existing_data = list(reader)

    with open(json_file, 'r') as file:
        additional_data = json.load(file)
    if type(additional_data) ==list:
        for row in additional_data:
            row['time_created'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updated_data = existing_data + additional_data
    elif type(additional_data) ==dict:
        additional_data['time_created'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updated_data = existing_data
        updated_data.append(additional_data)
    
    unique_keys = []
    for key_set in updated_data:
        for key in key_set.keys():
            if key not in unique_keys:
                unique_keys.append(key)

    headers = list(unique_keys)
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(updated_data)

    print(f"CSV file '{csv_file}' updated successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} !")


csv_file = 'data.csv'
json_file = 'data.json'
update_csv_with_json(csv_file, json_file)
