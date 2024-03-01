from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin


# Fazendo ocm que os campos apareçam no admin
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Valores Personalizáveis", {'fields': (
        'imagem_perfil',
        )})
)



UserAdmin.fieldsets = tuple(campos)

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['nome_completo', 'username', 'email']

    def nome_completo(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    nome_completo.short_description = 'Nome completo'


# Register your models here.
