from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from .views import *
# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func,home)

    def test_account_details(self):
        url = reverse('account_details')
        self.assertEquals(resolve(url).func,account_details)

    def test_printing(self):
        url = reverse('printing')
        self.assertEquals(resolve(url).func,printing)

    def test_record_binding(self):
        url = reverse('record_binding')
        self.assertEquals(resolve(url).func,record_binding)

    def test_printing_3d(self):
        url = reverse('printing_3d')
        self.assertEquals(resolve(url).func,printing_3d)

    def test_spiral_binding(self):
        url = reverse('spiral_binding')
        self.assertEquals(resolve(url).func,spiral_binding)