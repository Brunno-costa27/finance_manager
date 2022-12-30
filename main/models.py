from django.db import models


class Finance(models.Model):
    moradia = models.DecimalField(decimal_places=2, max_digits=10)
    saude = models.DecimalField(decimal_places=2, max_digits=10)
    educacao = models.DecimalField(decimal_places=2, max_digits=10)
    renda = models.DecimalField(decimal_places=2, max_digits=10)
    
