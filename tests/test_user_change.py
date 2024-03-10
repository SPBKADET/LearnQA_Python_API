import requests
from faker import Faker

fake = Faker()

from lib.assertions import Assertions
from lib.base_case import BaseCase


class TestUserChange(BaseCase):
    def test_user_change_unauthorized(self):
        # EDIT
        new_name = 'Changed Name'

        response3 = requests.put(f"https://playground.learnqa.ru/api/user/2",
                                 headers={"x-csrf-token": 'tokentoken'},
                                 cookies={"auth_sid": 'auth sid'},
                                 data={"firstName": new_name}
                                 )
        Assertions.assert_code_status(response3, expected_status_code=400)
        assert response3.json()['error'] == 'Auth token not supplied'

    def test_user_change_authorized_other_user(self):
            login_data = {
                'email': '11123@mail.ru',
                'password': '123'
            }
            response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
            auth_sid = response2.cookies['auth_sid']
            token = response2.headers['x-csrf-token']

            new_name = 'Changed Name'

            response3 = requests.put(f"https://playground.learnqa.ru/api/user/2",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid},
                                     data={"firstName": new_name}
                                     )
            Assertions.assert_code_status(response3,expected_status_code=400)
            assert response3.json()['error'] == 'Please, do not edit test users with ID 1, 2, 3, 4 or 5.'
            print(response3.text)

    def test_user_change_authorized_user(self):
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
        print(token)

        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{response.json().get('id')}",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid},
                                     data={"email": fake.email()}
                                     )
        Assertions.assert_code_status(response3,expected_status_code=200)
        assert 'success' in response3.json()


    def test_user_change_authorized_user_first_name(self):
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
        print(token)

        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{response.json().get('id')}",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid},
                                     data={"firstName": fake.name()}
                                     )
        Assertions.assert_code_status(response3,expected_status_code=200)
        assert 'success' in response3.json()
