from django.contrib import admin
from .models import Movimentacoes

# Register your models here.
@admin.register(Movimentacoes)
class Movimentacoes(admin.ModelAdmin):
    search_fields = ['usuario']
    list_display = ['usuario', 'carteira', 'tipo', 'valor']