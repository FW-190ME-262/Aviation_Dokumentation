import requests


url = 'http://127.0.0.1:8000/registration/'


data = {
    "user": {
        "username": "ertyu",
        "password": "12345",
    },
    "phone_number": "888888",
    "country": 1,
    "region": 1,
    "district": 1,
    "city_village": 1,
    "street": 1,
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Проверка ответа
if response.status_code == 201:
    print("Регистрация прошла успешно!", response.json())
else:
    print("Ошибка при регистрации:", response.status_code, response.json())
