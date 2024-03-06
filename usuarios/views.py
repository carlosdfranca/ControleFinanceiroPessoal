from django.shortcuts import render
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuario
from .forms import UsuarioForm
from django.contrib import messages

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
        
        usuario = form.save(commit=False)
        if 'nova_imagem_perfil' in self.request.FILES:
            usuario.imagem_perfil = self.request.FILES['nova_imagem_perfil']
        usuario.save()

        messages.success(self.request, 'Alterações salvas com sucesso!')
        return super().form_valid(form)

