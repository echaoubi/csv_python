import json
import csv
from datetime import datetime


def save_json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    headers = list(data[0].keys())
    headers.append('time_created')

    for row in data:
        row['time_created'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"Data saved to {csv_file} successfully!")



json_file = 'data.json'
csv_file = 'data.csv'

save_json_to_csv(json_file, csv_file)
