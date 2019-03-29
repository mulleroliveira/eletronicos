from django.forms import ModelForm, TextInput, DateInput, NumberInput
from . models import Computador

class ComputadorForm(ModelForm):
    class Meta:
        model = Computador
        fields = ('__all__')
        widgets = {
            'marca': TextInput(attrs={'class':'form-control'}),
            'modelo': TextInput(attrs={'class':'form-control'}),
            'preco': NumberInput(attrs={'class':'form-control'}),
            'peso': NumberInput(attrs={'class':'form-control'}),
            'linha': TextInput(attrs={'class':'form-control'}),
}