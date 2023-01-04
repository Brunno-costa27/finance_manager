from django.test import TestCase
from django.urls import reverse


class FinanceURLsTest(TestCase):
    
    def test_home_url(self):
       url = reverse('home')
       self.assertEqual(url, '/')
    
    def test_create_register_url(self):
       url = reverse('register')
       self.assertEqual(url, '/register')
       
    def test_update_register_url(self):
       url = reverse('register_update', kwargs={'id': 1})
       self.assertEqual(url, '/register/1/update')
    
    def test_total_url(self):
       url = reverse('total')
       self.assertEqual(url, '/total')
       
    def test_result_register_url(self):
       url = reverse('result')
       self.assertEqual(url, '/result')
       
    def test_home_view_returns_status_code_200_ok(self):
       response = self.client.get(reverse('home'))
       self.assertEqual(response.status_code, 200)
       
    def test_home_view_loads_correct_template(self):
       response = self.client.get(reverse('home'))
       self.assertTemplateUsed(response, 'main/pages/home.html')