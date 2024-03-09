import requests
import time

response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
print(response.text)
response1=requests.get(url='https://playground.learnqa.ru/ajax/api/longtime_job',params={'token':response.json()['token']})
print(response1.text)

time.sleep(10)
if response1.json()['status']=='Job is NOT ready':
    print('Задача не готова')
else:
    print('Задача готова')


