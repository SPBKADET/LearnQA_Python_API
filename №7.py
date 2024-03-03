import requests

response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response.text)

response_head=requests.Request(method='HEAD',url='https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response_head)

response_head_1=requests.head ('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response_head_1.status_code)

response_post=requests.Request(method='POST',url='https://playground.learnqa.ru/ajax/api/compare_query_type')
prepare_request=response_post.prepare()
print(prepare_request.body)

