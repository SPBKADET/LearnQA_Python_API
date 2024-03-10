import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
class TestUserRegister(BaseCase):
    def test_user_register_with_invalid_email(self):
        email='vinkotovexample.com'
        data={
            'password':'123',
            'username':'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
        response = requests.post('https://playground.learnqa.ru/api/user/',data = data)
        Assertions.assert_code_status(response,400)
        assert response.content.decode('utf8') == f'Invalid email format'
    @pytest.mark.parametrize("test_input", [(''),(''),(''),(''),('')])
    def test_user_register_with_invalid_fields(self,test_input):
        email='vinkotovexample.com'
        data={
            'password':test_input,
            'username':test_input,
            'firstName':test_input,
            'lastName':test_input,
            'email':email
        }
        response = requests.post('https://playground.learnqa.ru/api/user/',data = data)
        Assertions.assert_code_status(response, 400)
        assert f'field is too short' in response.content.decode('utf8')

    def test_user_register_with_short_name(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'l',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
        Assertions.assert_code_status(response, 400)
        print(response.content.decode('utf8'))
        assert response.content.decode('utf8') == f"The value of 'username' field is too short"

    def test_user_register_with_long_name(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
        Assertions.assert_code_status(response, 400)
        print(response.content.decode('utf8'))
        assert response.content.decode('utf8') == f"The value of 'username' field is too long"