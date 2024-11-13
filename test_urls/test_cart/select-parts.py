import requests

url = 'http://127.0.0.1:8000/parts/select/'
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwOTA3ODEwLCJpYXQiOjE3MzA5MDA2MTAsImp0aSI6ImMxNDlhYzFhNDg3ZTQ3M2Y5NGExMTZhNTIxNmJjNDViIiwidXNlcl9pZCI6MX0.zZeZP4lo4s5-pEsu4qIrAhI1dwx0RtYAbUdKZ_qhKuM"
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
