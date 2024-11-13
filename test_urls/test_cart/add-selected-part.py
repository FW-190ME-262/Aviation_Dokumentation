import requests

part_id = 1
url = f'http://127.0.0.1:8000/cart/add-selected-part/{part_id}/'
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxMzM3Mzk5LCJpYXQiOjE3MzEzMzAxOTksImp0aSI6IjQzMzhkMmNlM2Y2YTQ4MTU4NmFmYWU3NWRhZGVhNGNlIiwidXNlcl9pZCI6MX0.Idxo80MO1Vd2TVeOZxA1XAr0CVgqX8S-0100GQezkE8"
}

response = requests.post(url, headers=headers)


print(response.status_code)

if response.status_code == 201:
    try:
        print("Selected part added to cart:", response.json())
    except requests.exceptions.JSONDecodeError as e:
        print("Failed to parse JSON response:", e)
        print("Raw Response Text:", response.text)
else:
    # Handle error cases based on status code
    if response.status_code == 400:
        print("Bad Request. Check the request data or parameters.")
    elif response.status_code == 401:
        print("Unauthorized. Check the JWT token or authentication credentials.")
    elif response.status_code == 404:
        print("Not Found. The requested endpoint may not exist.")
    elif response.status_code == 500:
        print("Internal Server Error. Something went wrong on the server-side.")
        print("Raw Error Response:", response.text)  # Print the raw response for further debugging
    else:
        print("Error adding selected part to cart:", response.status_code)
        print("Response Text:", response.text)
