from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from main.models import Finance

from .test_finance_base import FinanceTestBase


class FinanceURLsTest(FinanceTestBase):
    
    def tearDown(self) -> None:
        return super().tearDown()
    
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
       
    def test_finance_templates_loads_finances(self):
       finance = Finance.objects.create(
          moradia=34,
          saude=30,
          educacao=30,
          renda=100
       )
       pass 
    
    def test_create_users_finances(self):
      self.make_user(
        first_name='user123',
        last_name='name123',
        username='username123',
        password='123456123',
        email='username@email.com123',
      )
      #  user = User.objects.create_user(
      #   first_name='user1',
      #   last_name='name1',
      #   username='username1',
      #   password='1234561',
      #   email='username@email.com1',
      #  )
       
      pass