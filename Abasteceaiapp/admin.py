# Register your models here.
from django.contrib import admin
from .models import Posto


@admin.register(Posto)
class PostoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'preco_gasolina', 'preco_etanol', 'preco_diesel', 'atualizado_em')
    list_filter = ('atualizado_em',)
    search_fields = ('nome', 'endereco')
