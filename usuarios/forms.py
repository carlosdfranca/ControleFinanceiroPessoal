from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'imagem_perfil', 'saldo_inicial']

class TrocarSenhaForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
