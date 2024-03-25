from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Movimentacoes
from datetime import datetime, timedelta
from django.db.models import Q
from calendar import monthrange



# Create your views here.
def movimentacoes_view(request):


    if request.method == 'POST':
        current_month = int(request.POST.get('month'))
        current_year = int(request.POST.get('year'))

        action = request.POST.get('action')

        if action == 'prev':
            # Calcula o mês anterior
            current_date = datetime(year=current_year, month=current_month, day=1)
            previous_month_date = current_date - timedelta(days=1)
            current_month = previous_month_date.month
            current_year = previous_month_date.year
        elif action == 'next':
            # Calcula o próximo mês
            current_date = datetime(year=current_year, month=current_month, day=1)
            next_month_date = current_date + timedelta(days=32)
            current_month = next_month_date.month
            current_year = next_month_date.year
            # Aqui eu tenho que fazer como ta fazendo no else abaixo para ver se funciona
            movimentacoes = Movimentacoes.objects.filter(data__range=(start_date, end_date))
            mes_ano_atual = start_date.strftime('%B %Y')
            return render(request, 'movimentacoes.html', {'movimentacoes': movimentacoes, 'mes_ano_atual': mes_ano_atual})
    else:
        now = datetime.now()
        month = now.month
        year = now.year
        days_in_month = monthrange(year, month)[1]
        start_date = datetime(year, month, 1)
        end_date = datetime(year, month, days_in_month)
        movimentacoes = Movimentacoes.objects.filter(data__range=(start_date, end_date))
        mes_ano_atual = start_date.strftime('%B %Y')
        return render(request, 'movimentacoes.html', {'movimentacoes': movimentacoes, 'mes_ano_atual': mes_ano_atual})



class DespesasView(LoginRequiredMixin, TemplateView):
    template_name = 'despesas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        movimentacoes = Movimentacoes.objects.filter(usuario=usuario, tipo_movimentacao=2)
        context['movimentacoes'] = movimentacoes
        return context
    

class ReceitasView(LoginRequiredMixin, TemplateView):
    template_name = 'receitas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        movimentacoes = Movimentacoes.objects.filter(usuario=usuario , tipo_movimentacao=1)
        context['movimentacoes'] = movimentacoes
        return context