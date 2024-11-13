# selected_parts_request.py
import requests

url = 'http://127.0.0.1:8000/parts/selected/'
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwOTA3ODEwLCJpYXQiOjE3MzA5MDA2MTAsImp0aSI6ImMxNDlhYzFhNDg3ZTQ3M2Y5NGExMTZhNTIxNmJjNDViIiwidXNlcl9pZCI6MX0.zZeZP4lo4s5-pEsu4qIrAhI1dwx0RtYAbUdKZ_qhKuM"}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("Selected parts:", response.json())
else:
    print("Error retrieving selected parts:", response.status_code, response.json())
