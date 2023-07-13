import json
import csv

import os
from datetime import datetime
import json


def update_csv_with_json(csv_file, additional_data):
    existing_data = []
    if os.path.isfile(csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            existing_data = list(reader)
    if type(additional_data) == list:
        for row in additional_data:
            row['time_created'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updated_data = existing_data + additional_data
    elif type(additional_data) == dict:
        additional_data['time_created'] = datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S')
        updated_data = existing_data
        updated_data.append(additional_data)

    unique_keys = []
    for key_set in updated_data:
        for key in key_set.keys():
            if key not in unique_keys:
                unique_keys.append(key)
    new_data = []
    new_unique_keys = []
    for key in updated_data:
        spic_data = {}
        for v in key:
            if (type(key[v]) == dict):
                for k, t in key[v].items():
                    new_key = f"{v}::{k}"
                    spic_data[new_key] = t
                    if new_key not in new_unique_keys:
                        new_unique_keys.append(new_key)
            else:
                if v not in new_unique_keys:
                    new_unique_keys.append(v)
                spic_data[v] = key[v]
        new_data.append(spic_data)
    headers = list(new_unique_keys)
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(new_data)

    print(f"CSV file '{csv_file}' updated successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} !")


csv_file = 'data.csv'
json_file = 'data.json'
with open(json_file, 'r') as file:
    loadJson = json.load(file)
update_csv_with_json(csv_file, loadJson)
