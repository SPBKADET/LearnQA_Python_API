import requests

response = requests.get('https://playground.learnqa.ru/api/homework_header')
assert 'success' in response.json()
assert response.status_code == 200
assert 'x-secret-homework-header' in response.headers
assert response.headers['x-secret-homework-header'] == 'Some secret value'
