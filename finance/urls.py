
from django.contrib import admin
from django.urls import path

from main.views import Home, Register, RegisterUpdate, Result, result_total

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('register', Register.as_view(), name='register'),
    path('result', Result.as_view(), name='result'),
    path('total', result_total, name='total'),
    path('register/<int:id>/update', RegisterUpdate.as_view(), name='register_update'),
]
