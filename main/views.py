from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import redirect, render

from main.forms import RegisterForm

from .models import Finance


def home(request):
    return render(request, 'main/pages/home.html', context={
        'name': 'brunno',
    })

def register_finance(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            data = Finance.objects.all().order_by('-id')
            print(data)
        
        
        return redirect("result")
    else:
        form = RegisterForm()
    return render(request, 'main/pages/register.html', context={
        'finance': form,
    })
    
def result_finale(request):
    
    return render(request, 'main/pages/finale.html', context={
        'saldo': 2000
    })
    
def return_total_gastos(request):
    finance = Finance.objects.all()
    ultimo_gerenciamento = finance.order_by('id').last() 
    total = ultimo_gerenciamento.moradia + ultimo_gerenciamento.saude + ultimo_gerenciamento.educacao
    saldo = ultimo_gerenciamento.renda - total
    moradia = ultimo_gerenciamento.moradia
    saude = ultimo_gerenciamento.saude
    educacao = ultimo_gerenciamento.educacao
    renda = ultimo_gerenciamento.renda
    porcentagem_moradia = (moradia/renda)
    porcentagem_saude = (saude/renda)
    porcentagem_educacao = (educacao/renda)
    return JsonResponse({
        'total_gastos': total,
        'saldo' : saldo,
        'moradia': moradia,
        'saude': saude,
        'educacao':educacao,
        'renda': renda,
        'porcentagem_moradia': f'{porcentagem_moradia:.0%}',
        'porcentagem_saude': f'{porcentagem_saude:.0%}',
        'porcentagem_educacao': f'{porcentagem_educacao:.0%}',
    })
    