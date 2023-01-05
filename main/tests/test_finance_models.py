from django.core.exceptions import ValidationError

from .test_finance_base import FinanceTestBase


class FinanceModelTest(FinanceTestBase):
    def setUp(self) -> None:
        self.finance = self.make_finance()
        return super().setUp()
    
    
    def test_finance_validation(self):
        
        self.finance.moradia = 53345353453534543534
        self.finance.saude = 53345353534535345
        self.finance.educacao = 53345353534535345
        self.finance.renda = 53345353534535345
        with self.assertRaises(ValidationError):
            self.finance.full_clean()
    
    
    
    
        
        