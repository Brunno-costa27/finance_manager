from django.contrib.auth.models import User
from django.test import TestCase


class FinanceTestBase(TestCase):
    def setUp(self) -> None:
        user = self.make_user()
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