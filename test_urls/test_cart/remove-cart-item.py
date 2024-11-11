# remove_cart_item.py
import requests

item_id = 1  # ID товара в корзине
url = f'http://127.0.0.1:8000/cart/remove-item/{item_id}/'
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

response = requests.delete(url, headers=headers)
if response.status_code == 204:
    print("Item removed from cart.")
else:
    print("Error removing item from cart:", response.status_code, response.json())
