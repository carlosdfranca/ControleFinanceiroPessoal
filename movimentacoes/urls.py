from django.urls import path
from .views import movimentacoes_view, ReceitasView, DespesasView

urlpatterns = [
    path('', movimentacoes_view, name='movimentacoes'),
    path('despesas/', DespesasView.as_view(), name='despesas'),
    path('receitas/', ReceitasView.as_view(), name='receitas'),
]