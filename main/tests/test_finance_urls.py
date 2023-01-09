from django.urls import reverse

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
       
    def test_total_view_returns_status_code_200_ok(self):
       response = self.client.get(reverse('total'))
       self.assertEqual(response.status_code, 200)
       
    def test_register_view_returns_status_code_200_ok(self):
       response = self.client.get(reverse('register'))
       self.assertEqual(response.status_code, 200)
       
    def test_result_view_returns_status_code_200_ok(self):
       response = self.client.get(reverse('result'))
       self.assertEqual(response.status_code, 200)
       
    def test_result_update_view_returns_status_code_200_ok(self):
       response = self.client.get(reverse('register_update', kwargs={'id': 1}))
       self.assertEqual(response.status_code, 200)
       
    def test_register_returns_status_code(self):
       response = self.client.post(reverse('register'),{
            'moradia': 345,
            'saude': 305,
            'educacao': 505,
            'renda': 705,
       },
       follow=True,

      )
       self.assertEqual(response.status_code, 200)
       
    def test_register_update__returns_status_code(self):
       response = self.client.post(reverse('register_update', kwargs={'id': 1}),{
            'moradia': 345,
            'saude': 305,
            'educacao': 505,
            'renda': 705,
       },
       follow=True,

      )
       self.assertEqual(response.status_code, 200)
       
   
      
      
      
      
    def test_home_view_loads_correct_template(self):
       response = self.client.get(reverse('home'))
       self.assertTemplateUsed(response, 'main/pages/home.html')
       
    def test_finance_templates_loads_finances(self):
      self.make_finance(
        moradia=345,
        saude=305,
        educacao=505,
        renda=705,
      )
      pass      
   
    def test_finance_templates_loads_finances_return(self):
      self.make_finance(
        moradia=345,
        saude=305,
        educacao=505,
        renda=705,
      )
      res = self.make_finance()
      if res:
          pass 
    
    def test_create_users_finances(self):
      self.make_user(
        first_name='user123',
        last_name='name123',
        username='username123',
        password='123456123',
        email='username@email.com123',
      )
      
      pass