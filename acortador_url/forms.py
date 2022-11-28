from django import forms
from .models import  acortador_url
class genericUrl(forms.ModelForm):

    url = forms.URLField(label='url', required=True)
    acor_url = forms.CharField(label='nombre de la url', required=True, max_length=11,
                               widget=(forms.TextInput(attrs={'placeholder': 'Nombre de la url'})))
    class Meta:
        model = acortador_url
        fields = ['url',  'acor_url']