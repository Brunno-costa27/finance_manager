
import time

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FinanceBaseFunctionalTeste(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        return super().setUp()

    def tearDown(self):
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5):
        time.sleep(seconds)

class FinanceHomePageFunctionalTest(FinanceBaseFunctionalTeste):
    
    
    def test_finance_home_page_text(self):
        self.browser.get('http://127.0.0.1:8000/')
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Responda algumas perguntas e saiba:', body.text)
        