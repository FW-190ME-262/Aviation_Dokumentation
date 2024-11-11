import requests


url = 'http://127.0.0.1:8000/countries/'


data = {


    "name": 1,
  }


response = requests.get(url, json=data)


if response.status_code == 200:
    print("успешно!", response.json())
else:
    print("Ошибка из за Никиты:", response.status_code, response.json())
