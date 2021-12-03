from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class UserModelTest(TestCase):
    def test_new_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',email="email@email.com",telefone="0",primeiro_nome="nome",sobrenome="sobrenome",password="testpass123")