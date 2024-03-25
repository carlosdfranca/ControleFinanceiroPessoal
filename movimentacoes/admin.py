from django.contrib import admin
from .models import Movimentacoes

# Register your models here.
@admin.register(Movimentacoes)
class MovimentacoesAdmin(admin.ModelAdmin):
    search_fields = ['usuario']
    list_display = ['usuario', 'carteira', 'tipo_movimentacao', 'valor']