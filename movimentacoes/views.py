from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Movimentacoes
from datetime import datetime


# Create your views here.
class MovimentacoesView(LoginRequiredMixin, ListView):
    model = Movimentacoes
    template_name = 'movimentacoes.html'
    context_object_name = 'page_obj'
    paginate_by = 10

    def get_queryset(self):
        return Movimentacoes.objects.all()


class DespesasView(LoginRequiredMixin, ListView):
    model = Movimentacoes
    template_name = 'despesas.html'
    context_object_name = 'page_obj'
    paginate_by = 10

    def get_queryset(self):
        return Movimentacoes.objects.filter(tipo_movimentacao=2)
    

class ReceitasView(LoginRequiredMixin, ListView):
    model = Movimentacoes
    template_name = 'receitas.html'
    context_object_name = 'page_obj'
    paginate_by = 10

    def get_queryset(self):
        return Movimentacoes.objects.filter(tipo_movimentacao=1)