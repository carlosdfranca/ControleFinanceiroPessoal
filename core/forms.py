from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']