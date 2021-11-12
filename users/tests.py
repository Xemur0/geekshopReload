from django.conf import settings
from django.test import TestCase
from django.test.client import Client

# Create your tests here.
from mainapp.models import ProductCategory, Product
from users.models import User


class TestMainSmokeTest(TestCase):
    status_code_success = 200
    status_code_render = 302
    username = 'Xemuro'
    email = 'aleks111@mail.ru'
    password = 'Intheend1'

    new_user_data = {
        'username':'aleks',
        'first_name':'Aleks',
        'last_name': 'Aleksprfnk',
        'password1': 'daxn92daxn',
        'password2': 'daxn92daxn',
        'email': 'aleks.prfnk@mail.ru',

    }

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(self.username,email=self.email,password=self.password)
        self.client = Client()

    def test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,self.status_code_success)
        self.assertTrue(response.context['user'].is_anonymous)
        self.client.login(username=self.username,password=self.password)
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, self.status_code_render)

    def test_register(self):
        response = self.client.post('/users/register/',data=self.new_user_data)
        self.assertEqual(response.status_code,self.status_code_render)


        new_user = User.objects.get(username=self.new_user_data['username'])
        print(new_user)
        activation_url = f"{settings.DOMAIN_NAME}/users/verify/{self.new_user_data['email']}/{new_user.activation_key}/"
        response = self.client.get(activation_url)
        self.assertEqual(response.status_code, self.status_code_success)
        new_user.refresh_from_db()
        self.assertTrue(new_user.is_active)

    def tearDown(self) -> None:
        pass
