from django.contrib.auth.models import User
from django.test import TestCase

from main.models import Finance


class FinanceTestBase(TestCase):
    def setUp(self) -> None:
        user = self.make_user()
        finance = self.make_finance()
        return super().setUp()
    
    def make_user(
        self,
        first_name='user1',
        last_name='name1',
        username='username1',
        password='1234561',
        email='username@email.com1',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )
        
    def make_finance(
        self,
        moradia=34,
        saude=30,
        educacao=50,
        renda=70,
    ):
        return Finance.objects.create(
            moradia=moradia,
            saude=saude,
            educacao=educacao,
            renda=renda,
        )