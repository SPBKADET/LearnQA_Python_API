from json import loads


json_string=('{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},'
             '{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}')
data=loads(json_string)
print(data['messages'][1]['message'])
