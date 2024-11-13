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
import requests

# Настройки API
BASE_URL = "http://127.0.0.1:8000"
LOGIN_URL = f"{BASE_URL}/api/token/"

# Данные для авторизации
USERNAME = "admin"
PASSWORD = "admin"

HEADERS = {}


def get_jwt_token():
    """Получает JWT токен и устанавливает его в заголовки для последующих запросов."""
    global HEADERS
    response = requests.post(LOGIN_URL, json={"username": USERNAME, "password": PASSWORD})
    if response.status_code == 200:
        token = response.json().get("access")
        HEADERS = {
            "Authorization": f"Bearer {token}"
        }
        print("JWT токен получен успешно!")
    else:
        print(f"Ошибка при получении токена: {response.status_code}, {response.json()}")


def test_add_selected_parts():
    url = f"{BASE_URL}/parts/select/"
    data = {
        "part": 1,  # ID компонента
        "quantity": 2
    }
    response = requests.post(url, json=data, headers=HEADERS)
    print(f"Add Selected Parts: {response.status_code}, {response.json()}")


def test_get_selected_parts():
    url = f"{BASE_URL}/parts/selected/"
    response = requests.get(url, headers=HEADERS)
    print(f"Get Selected Parts: {response.status_code}, {response.json()}")


def test_view_cart():
    url = f"{BASE_URL}/cart/"
    response = requests.get(url, headers=HEADERS)
    print(f"View Cart: {response.status_code}, {response.json()}")


def test_add_selected_part_to_cart(part_id):
    url = f"{BASE_URL}/cart/add-selected-part/{part_id}/"
    response = requests.post(url, headers=HEADERS)
    print(f"Add Selected Part to Cart: {response.status_code}, {response.json()}")


def test_remove_cart_item(item_id):
    url = f"{BASE_URL}/cart/remove-item/{item_id}/"
    response = requests.delete(url, headers=HEADERS)
    print(
        f"Remove Cart Item: {response.status_code}, {response.json() if response.status_code != 204 else 'No Content'}")


# Запуск тестов
if __name__ == "__main__":
    # Получаем токен перед выполнением тестов
    get_jwt_token()

    if "Authorization" in HEADERS:
        # Тест на добавление выбранных частей
        test_add_selected_parts()

        # Тест на получение выбранных частей
        test_get_selected_parts()

        # Тест на просмотр корзины
        test_view_cart()

        # Тест на добавление части в корзину (здесь 1 — это ID части, которую добавляем)
        test_add_selected_part_to_cart()

        # Тест на удаление элемента из корзины (здесь 1 — это ID элемента в корзине, который удаляем)
        test_remove_cart_item(1)
    else:
        print("Не удалось выполнить тесты из-за отсутствия токена.")
