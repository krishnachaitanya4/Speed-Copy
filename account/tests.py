from django.test import TestCase,SimpleTestCase,Client
from django.urls import reverse,resolve
from .views import *
# Create your tests here.
class UrlTests(SimpleTestCase):
    def test_login(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func,login)
    def test_register(self):
        url = reverse("register")
        self.assertEquals(resolve(url).func,register)
    def test_logout(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func,logout)

class TestViews(TestCase):

    def SetUp(self):
        self.client = Client()

    def test_login_get(self):
        response = self.client.get(reverse("login"))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')
    
    def test_login_post(self):
        response = self.client.post(reverse('login'),{
            'email':'asdf@gmail.com',
            'password':'asdf'
        })
        self.assertAlmostEquals(response.status_code,302)
    
