import requests

user_login = "http://127.0.0.1:8000/api/token/"
data = {
    "username": "qwerty",
    "password": "1234567890qaz"
}
request_login = requests.post(user_login, data=data)

if request_login.status_code == 200:
    response_data = request_login.json()
    print("Ответ при авторизации:", response_data)

    access_token = response_data.get("access")
    if access_token:
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        print("Заголовки с токеном:", headers)

        # Пробуем отправить запрос с токеном
        url = 'http://127.0.0.1:8000/parts/selected/'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print("Успешный запрос:", response.json())
        else:
            print("Ошибка сервера:", response.status_code, response.json())
    else:
        print("Ошибка: Токен доступа не найден в ответе.")
else:
    print("Ошибка авторизации:", request_login.status_code, request_login.json())
