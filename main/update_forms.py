from django import forms
from django.forms import ValidationError

from main.forms import add_attr
from main.models import Finance


class UpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_attr(self.fields['moradia'], 'placeholder', 'R$ 0,00')
        add_attr(self.fields['renda'], 'placeholder', 'R$ 0,00')
        add_attr(self.fields['saude'], 'placeholder', 'R$ 0,00')
        add_attr(self.fields['educacao'], 'placeholder', 'R$ 0,00')
        
    def clean(self):
        data_renda = super().clean()
        data = self.cleaned_data.get('renda')
        
        print('Entrou no clean')
        print(data)
        
        if 3 == data:
            raise ValidationError(
                'errado'
            )
        return data_renda
    
    
    class Meta:
        model = Finance
        fields = '__all__'

