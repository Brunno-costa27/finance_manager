from django.core.exceptions import ValidationError

from .test_finance_base import FinanceTestBase


class FinanceModelTest(FinanceTestBase):
    def setUp(self) -> None:
        self.finance = self.make_finance()
        return super().setUp()
    
    def test_the_test(self):
        self.finance.moradia = 53345353453534543534
        with self.assertRaises(ValidationError):
            self.finance.full_clean()
    
    
        
        