from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Movimentacoes



# Create your views here.
class MovimentacoesView(LoginRequiredMixin, TemplateView):
    template_name = 'movimentacoes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        movimentacoes = Movimentacoes.objects.filter(usuario=usuario)
        context['movimentacoes'] = movimentacoes
        return context


class DespesasView(LoginRequiredMixin, TemplateView):
    template_name = 'despesas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        movimentacoes = Movimentacoes.objects.filter(usuario=usuario, tipo=2)
        context['movimentacoes'] = movimentacoes
        return context
    

class ReceitasView(LoginRequiredMixin, TemplateView):
    template_name = 'receitas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        movimentacoes = Movimentacoes.objects.filter(usuario=usuario , tipo=1)
        context['movimentacoes'] = movimentacoes
        return context