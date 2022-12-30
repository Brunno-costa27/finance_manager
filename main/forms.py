from django import forms

from main.models import Finance


class RegisterForm(forms.ModelForm):
    
    renda = forms.DecimalField(
        required= True,
        widget=forms.NumberInput(
            attrs={"placeholder": "R$ 0,00", "class": "form-group",
            }
        ),
        error_messages={
                'required': 'Campo obrigatório'
        },
    )
     
    class Meta:
        model = Finance
        fields = '__all__'
        
        