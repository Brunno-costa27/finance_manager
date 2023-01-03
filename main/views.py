from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from main.forms import RegisterForm
from main.update_forms import UpdateForm

from .models import Finance


def result_total(request):
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
        valor_ideal_moradia =  int(renda) * 0.2
        valor_ideal_saude = int(renda) * 0.08
        valor_ideal_educacao = int(renda) * 0.12
        
        return JsonResponse({
            'total_gastos': total,
            'saldo' : saldo,
            'moradia': moradia,
            'saude': saude,
            'educacao':educacao,
            'renda': renda,
            'porcentagem_moradia': f'{porcentagem_moradia:.1%}',
            'porcentagem_saude': f'{porcentagem_saude:.1%}',
            'porcentagem_educacao': f'{porcentagem_educacao:.1%}',
            'valor_ideal_moradia': f'R$ {valor_ideal_moradia:.2f}',
            'valor_ideal_saude': f'R$ {valor_ideal_saude:.2f}',
            'valor_ideal_educacao': f'R$ {valor_ideal_educacao:.2f}'
        })

class Home(View):

    def get(self, request):
        return render(request, 'main/pages/home.html', context={
            'name': 'brunno',
        })
class Register(View):
    
    def get(self, request):
       
        return render(request, 'main/pages/register.html', context={
            'finance': RegisterForm()
        })
        
    def post(self, request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            
            if form.is_valid():
                form.save()
                
                return redirect("result")
            else:
                
                form = RegisterForm()
                
            return render(request, 'main/pages/register.html', context={
                'finance': form,
            })
        
        
class RegisterUpdate(View):
    
    def get_finance(self, id):
        finance = None
        if id:
            finance = Finance.objects.filter(pk=id).last()
            
            if not finance:
                raise Http404()
        return finance
    
    def get(self, request, id):
        finance = self.get_finance(id)
        form = UpdateForm(instance=finance)
        
        return render(request, 'main/pages/register_update.html', context={
            'finance': form
        }) 
    
    
    def post(self, request, id):
        finance = self.get_finance(id)
        form = UpdateForm(
            data=request.POST or None,
            instance=finance
        )
        
        if form.is_valid():
            form.save()
            
            return redirect("result")
        
        return render(request, 'main/pages/register_update.html', context={
            'finance': form
        }) 
        
class Result(View):
    
    def get(self, request):
        finance = Finance.objects.filter().last()
    
        return render(request, 'main/pages/finale.html', context={
            'form': finance
        })

        
    # def home(request):
    #     return render(request, 'main/pages/home.html', context={
    #         'name': 'brunno',
    #     })

    # def register_finance(request):
        
    #     if request.method == 'POST':
    #         form = RegisterForm(request.POST)
            
    #         print(form.errors)
    #         if form.is_valid():
    #             form.save()
                
                
            
            
    #         return redirect("result")
    #     else:
    #         form = RegisterForm()
    #     return render(request, 'main/pages/register.html', context={
    #         'finance': form,
    #     })
        
    # def result_finale(request):
    #     finance = Finance.objects.filter().last()
    
    #     return render(request, 'main/pages/finale.html', context={
    #         'form': finance
    #     })
        
    # def return_total_gastos(request):
    #     finance = Finance.objects.all()
    #     ultimo_gerenciamento = finance.order_by('id').last() 
    #     total = ultimo_gerenciamento.moradia + ultimo_gerenciamento.saude + ultimo_gerenciamento.educacao
    #     saldo = ultimo_gerenciamento.renda - total
    #     moradia = ultimo_gerenciamento.moradia
    #     saude = ultimo_gerenciamento.saude
    #     educacao = ultimo_gerenciamento.educacao
    #     renda = ultimo_gerenciamento.renda
    #     porcentagem_moradia = (moradia/renda)
    #     porcentagem_saude = (saude/renda)
    #     porcentagem_educacao = (educacao/renda)
    #     valor_ideal_moradia =  int(renda) * 0.2
    #     valor_ideal_saude = int(renda) * 0.08
    #     valor_ideal_educacao = int(renda) * 0.12
        
    #     return JsonResponse({
    #         'total_gastos': total,
    #         'saldo' : saldo,
    #         'moradia': moradia,
    #         'saude': saude,
    #         'educacao':educacao,
    #         'renda': renda,
    #         'porcentagem_moradia': f'{porcentagem_moradia:.1%}',
    #         'porcentagem_saude': f'{porcentagem_saude:.1%}',
    #         'porcentagem_educacao': f'{porcentagem_educacao:.1%}',
    #         'valor_ideal_moradia': f'R$ {valor_ideal_moradia:.2f}',
    #         'valor_ideal_saude': f'R$ {valor_ideal_saude:.2f}',
    #         'valor_ideal_educacao': f'R$ {valor_ideal_educacao:.2f}'
    #     })
        
    # def update_gastos(request, id):
    #     finance = Finance.objects.filter(
    #         pk=id,
    #         ).last()
        
    #     if not finance:
    #         raise Http404()
    #     form = UpdateForm(
    #         data=request.POST or None,
    #         instance=finance
    #     )
        
    #     if form.is_valid():
    #         form.save()
            
    #         return redirect("result")
        
    #     return render(request, 'main/pages/register_update.html', context={
    #         'finance': form
    #     }) 