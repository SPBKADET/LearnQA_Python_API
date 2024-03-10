import requests
from faker import Faker

fake = Faker()

from lib.assertions import Assertions
from lib.base_case import BaseCase

class TestUserDelete():
    def test_user_delete_invalide(self):
        response=requests.delete('https://playground.learnqa.ru/api/user/2',data= {

            'email': 'vinkotov@example.com',

            'password': '1234'

        })
        print(response.text)
        Assertions.assert_code_status(response, 400)
        assert response.json()['error'] == f"Auth token not supplied"

    def test_user_delete_valid(self):
        password = fake.password()
        email = fake.email()
        response = requests.post(f"https://playground.learnqa.ru/api/user/",
                                 data={
                                     'password': password,
                                     'username': fake.name(),
                                     'firstName': fake.name(),
                                     'lastName': fake.name(),
                                     'email': email
                                 }
                                 )
        print(response.json())
        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = response2.cookies['auth_sid']
        token = response2.headers['x-csrf-token']
        id=response.json()['id']
        response3 = requests.delete(f'https://playground.learnqa.ru/api/user/{id}', data={

            'email': email,
            'password': password

        },headers={"x-csrf-token": token},
                                 cookies={"auth_sid":auth_sid})

        Assertions.assert_code_status(response3, expected_status_code=200)
        assert 'success' in response3.json()

    def test_delete_user_negative(self):
        password = fake.password()
        email = fake.email()
        response = requests.post(f"https://playground.learnqa.ru/api/user/",
                                 data={
                                     'password': password,
                                     'username': fake.name(),
                                     'firstName': fake.name(),
                                     'lastName': fake.name(),
                                     'email': email
                                 }
                                 )
        print(response.json())
        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = response2.cookies['auth_sid']
        token = response2.headers['x-csrf-token']
        id = response.json()['id']
        response3 = requests.delete(f'https://playground.learnqa.ru/api/user/2', data={

            'email': email,
            'password': password

        }, headers={"x-csrf-token": token},
                                    cookies={"auth_sid": auth_sid})

        Assertions.assert_code_status(response3, expected_status_code=400)
        print(response3.text)
        assert response3.json()['error'] == 'Please, do not delete test users with ID 1, 2, 3, 4 or 5.'
