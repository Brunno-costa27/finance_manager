
from django.contrib import admin
from django.urls import path

from main.views import (home, register_finance, result_finale,
                        return_total_gastos)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register', register_finance, name='register'),
    path('result', result_finale, name='result'),
    path('total', return_total_gastos, name='total'),
    
    
]
