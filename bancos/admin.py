from django.contrib import admin
from .models import DadosInstitucionais

# Register your models here.
@admin.register(DadosInstitucionais)
class DadosInstitucionaisAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['nome', 'categoria',]