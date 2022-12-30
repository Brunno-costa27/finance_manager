from django.shortcuts import render

from main.forms import RegisterForm

# from .models import Finance


def home(request):
    return render(request, 'main/pages/home.html', context={
        'name': 'brunno',
    })

def trazerTodosOsDadosDaTableFinance(request):
    # finance = Finance.objects.all().order_by('-id')
    # print(finance)
    form = RegisterForm()
    
    return render(request, 'main/pages/home.html', context={
        'finance': form,
    })