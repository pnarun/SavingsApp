from django import forms
from django.contrib.auth.models import User
from home.models import user_register


# class UserRegisterForm(forms.Form):
#     password = forms.CharField(
#         label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     model = user_register
#     fields = '__all__'
#     # fields = ('username', 'contact', 'first_name',
#     #           'last_name', 'email', 'password')
#     widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'true'}),
#                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#                'contact': forms.TextInput(attrs={'class': 'form-control'}),
#                'email': forms.EmailInput(attrs={'class': 'form-control'})
#                }
