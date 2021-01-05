from django.test import TestCase
from core.models import Item, Registry
from django.test import Client

class LoginTestCase(TestCase):
    def test_users_can_login(self):
        client = Client()
        response = client.post('auth/token/login/', {'username:djoser', password:'alpine12'})
        response.status_code
        response.auth_token
        response.content
        

        