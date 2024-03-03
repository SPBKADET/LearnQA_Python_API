import requests


response = requests.get('https://playground.learnqa.ru/api/long_redirect')
print("количество редиректов:", len(response.history))
print("итоговый url:", response.url)
