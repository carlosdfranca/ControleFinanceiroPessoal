from django.shortcuts import render
from django.views.generic import UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuario
from .forms import UsuarioForm, TrocarSenhaForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash

# Create your views here.
class PerfilView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return self.request.path
    
    def form_valid(self, form):
        messages.success(self.request, 'Alterações salvas com sucesso!')
        return super().form_valid(form)
    
    
class PasswordChangeView(FormView):
    template_name = 'perfil.html'
    form_class = TrocarSenhaForm

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)  # Atualiza a sessão do usuário para evitar logout
        messages.success(self.request, 'Senha Alterada!')
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


