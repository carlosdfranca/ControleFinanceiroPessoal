from django.http.response import HttpResponse as HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForm
from django.contrib import messages

# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class CriarConta(CreateView):
    form_class = CriarContaForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Conta criada com sucesso! Você já pode fazer login.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocorreu um erro durante o registro. Por favor, verifique os dados fornecidos.')
        return super().form_invalid(form)
