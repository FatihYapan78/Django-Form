from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adınız", widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Kullanıcı Adı"
        }))
    password = forms.CharField(label="Şifreniz",widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':"Şifreniz"
        }))
    
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Kullanıcı Adınız", widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Kullanıcı Adı"
        }))
    first_name = forms.CharField(label="Adınız", widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"Ad"
        }))
    last_name = forms.CharField(label="SoyAdınız", widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':"SoyAd"
        }))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':"Email"
        }))
    password1 = forms.CharField(label="Şifre",widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':"Şifre"
        }))
    password2 = forms.CharField(label="Şifre Tekrar",widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':"Şifre Tekrar"
        }))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']