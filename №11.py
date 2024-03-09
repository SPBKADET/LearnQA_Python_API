import requests


response = requests.get(url='https://playground.learnqa.ru/api/homework_cookie')
print(response.cookies['HomeWork'])
assert response.cookies['HomeWork']
