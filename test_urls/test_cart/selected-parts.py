# selected_parts_request.py
import requests

url = 'http://127.0.0.1:8000/parts/selected/'
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("Selected parts:", response.json())
else:
    print("Error retrieving selected parts:", response.status_code, response.json())
