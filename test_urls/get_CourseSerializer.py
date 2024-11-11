import requests

url = 'http://127.0.0.1:8000/courses/'

response = requests.get(url)

if response.status_code == 200:
    print("успешно!", response.json())
else:
    print("Ошибка из за Никиты:", response.status_code, response.json())

url = 'http://127.0.0.1:8000/courses/'

try:
    response = requests.get(url)
    response.raise_for_status()  # Проверяем, был ли ответ успешным (код 200)
    print("Успешно!", response.json())
except requests.exceptions.HTTPError as http_err:
    print("Ошибка из-за Никиты:", response.status_code, response.json())
except Exception as err:
    print("Произошла ошибка:", err)
