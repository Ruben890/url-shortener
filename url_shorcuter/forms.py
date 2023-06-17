from django import forms
from .models import  Acortador_url
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class genericUrl(forms.ModelForm):

    url = forms.URLField(label='url', required=True,
                         widget=forms.TextInput(attrs={'placeholder': 'url', 'class':'form-control'}))
    acor_url = forms.CharField(label='nombre de la url', required=True, max_length=18,
                               widget=(forms.TextInput(attrs={'placeholder': 'Nombre de la url', 'class':'form-control'})))
    class Meta:
        model = Acortador_url
        fields = ['url',  'acor_url']
        




class UserRegister(UserCreationForm):
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(label="Username", required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))  # Update this line
    password1 = forms.CharField(label='Password', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))