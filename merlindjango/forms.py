from django import forms
from django.contrib.auth.models import User
from .models import GSMModels


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


class ModelForm(forms.ModelForm):

    class Meta:
        model = GSMModels
        fields = ['id_modelo', 'name', 'organism', 'publication', 'year', 'file', 'is_public']
