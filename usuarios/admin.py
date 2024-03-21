from django.contrib import admin
from .models import Usuario, Carteira, Categoria, CartaoCredito
from django.contrib.auth.admin import UserAdmin


# Fazendo ocm que os campos apareçam no admin
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Valores Personalizáveis", {'fields': (
        'imagem_perfil',
        )})
)



UserAdmin.fieldsets = tuple(campos)


# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['nome_completo', 'username', 'email']

    def nome_completo(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    nome_completo.short_description = 'Nome completo'


@admin.register(Carteira)
class BancoAdmin(admin.ModelAdmin):
    search_fields = ['usuario']
    list_display = ['usuario', 'descricao', 'instituicao', 'tipo_conta', 'saldo_inicial']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['usuario']
    list_display = ['usuario', 'tipo_transacao', 'nome', 'cor']


@admin.register(CartaoCredito)
class CartaoCreditoAdmin(admin.ModelAdmin):
    search_fields = ['usuario']
    list_display = ['usuario', 'descricao', 'carteira', 'bandeira']