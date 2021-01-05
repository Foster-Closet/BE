from django.test import TestCase
from core.models import Item, Registry
from django.test import Client

class LoginTestCase(TestCase):
    def setUp(self):
        
    
    def test_users_can_login(self):
        client = Client()
        response = client.post('auth/token/login/', {'username:djoser', 'password:alpine12'})
        print(response.status_code)
        print(response.auth_token)
        print(response.content)
        