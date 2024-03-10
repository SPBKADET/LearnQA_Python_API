import requests
import allure
from lib.base_case import BaseCase


class TestUserGet(BaseCase):
    @allure.description("test_user_get_with_invalid_id")
    def test_user_get_with_invalid_id(self):
        email = 'vinkotovexample.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
        response1 = requests.get('https://playground.learnqa.ru/api/user/2')
        assert response1.status_code == 200
        assert response1.json()['username'] == 'Vitaliy'
