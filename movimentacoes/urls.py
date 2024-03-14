from django.urls import path
from .views import MovimentacoesView, ReceitasView, DespesasView

urlpatterns = [
    path('/', MovimentacoesView.as_view(), name='movimentacoes'),
    path('/despesas/', DespesasView.as_view(), name='despesas'),
    path('/receitas/', ReceitasView.as_view(), name='receitas'),
]