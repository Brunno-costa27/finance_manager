from django import forms
from django.forms import ValidationError

from main.models import Finance


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()

class RegisterForm(forms.ModelForm):
     
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        add_attr(self.fields['moradia'], 'placeholder', 'R$ 0,00')
        add_attr(self.fields['renda'], 'placeholder', 'R$ 0,00')
        add_attr(self.fields['saude'], 'placeholder', 'R$ 0,00')
        add_attr(self.fields['educacao'], 'placeholder', 'R$ 0,00')
    
          
    
    def clean(self):
        data_renda = super().clean()
        data = self.cleaned_data.get('moradia')

        print('Entrou no clean')
        print(data)
        
        if 0 == data:
            raise ValidationError(
                'errado'
            )
        return data_renda
     
    class Meta:
        model = Finance
        fields = '__all__'
        