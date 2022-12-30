
from django.contrib import admin
from django.urls import path

from main.views import home, trazerTodosOsDadosDaTableFinance

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', trazerTodosOsDadosDaTableFinance),
    
]
