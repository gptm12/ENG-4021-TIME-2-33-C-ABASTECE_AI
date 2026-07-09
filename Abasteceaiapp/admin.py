# Register your models here.
from django.contrib import admin
from .models import Posto, TipoCombustivel, Preco, Comodidade, Conta


@admin.register(Posto)
class PostoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'preco_gasolina', 'preco_etanol', 'preco_diesel', 'atualizado_em')
    list_filter = ('atualizado_em',)
    search_fields = ('nome', 'endereco')

@admin.register(TipoCombustivel)
class TipoCombustivelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao')
    search_fields = ('titulo',)

@admin.register(Preco)
class PrecoAdmin(admin.ModelAdmin):
    list_display = ('posto', 'tipo_combustivel', 'valor', 'atualizado_em')
    list_filter = ('atualizado_em',)
    search_fields = ('posto__nome', 'tipo_combustivel__titulo')

@admin.register(Comodidade)
class ComodidadeAdmin(admin.ModelAdmin):
    list_display = ('posto', 'tipo', 'nome')
    list_filter = ('tipo',)
    search_fields = ('posto__nome', 'nome')

@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'email', 'senha')
    search_fields = ('usuario', 'email')
