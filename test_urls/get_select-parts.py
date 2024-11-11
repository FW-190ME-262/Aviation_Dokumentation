# select_parts_request.py
import requests

url = 'http://127.0.0.1:8000/parts/select/'
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxMzM3Mzk5LCJpYXQiOjE3MzEzMzAxOTksImp0aSI6IjQzMzhkMmNlM2Y2YTQ4MTU4NmFmYWU3NWRhZGVhNGNlIiwidXNlcl9pZCI6MX0.Idxo80MO1Vd2TVeOZxA1XAr0CVgqX8S-0100GQezkE8"
}
data = {
    "part": 1,  # ID выбранной части
    "quantity": 2  # Количество
}

response = requests.post(url, headers=headers, json=data)
if response.status_code == 201:
    print("Part added successfully:", response.json())
else:
    print("Error adding part:", response.status_code, response.json())
