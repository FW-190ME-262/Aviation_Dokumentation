import requests

url = 'http://127.0.0.1:8000/parts/select/'
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwOTA3ODEwLCJpYXQiOjE3MzA5MDA2MTAsImp0aSI6ImMxNDlhYzFhNDg3ZTQ3M2Y5NGExMTZhNTIxNmJjNDViIiwidXNlcl9pZCI6MX0.zZeZP4lo4s5-pEsu4qIrAhI1dwx0RtYAbUdKZ_qhKuM"
}
data = {
    "part": 1,  # ID of the selected part
    "quantity": 2  # Quantity
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Print status code and response content
print("Status Code:", response.status_code)
print("Response Text:", response.text)  # Check raw response

# Check if the response status code indicates success
if response.status_code == 201:
    try:
        # Try to parse the JSON response
        print("Part added successfully:", response.json())
    except requests.exceptions.JSONDecodeError as e:
        # Handle case where the response is not in JSON format
        print("Failed to parse JSON:", e)
else:
    # If status code is not 201, handle different errors based on the response code
    if response.status_code == 400:
        print("Bad Request. Check the request data or parameters.")
    elif response.status_code == 401:
        print("Unauthorized. Check the JWT token or authentication credentials.")
    elif response.status_code == 403:
        print("Forbidden. You do not have permission to perform this action.")
    elif response.status_code == 404:
        print("Not Found. The requested endpoint may not exist.")
    elif response.status_code == 500:
        print("Internal Server Error. Something went wrong on the server-side.")
    else:
        print("Error:", response.status_code)
