# Register your models here.
from django.contrib import admin
from .models import Posto

@admin.register(Posto)
class PostoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'bandeira', 'endereco', 'avaliacao']
    list_filter = ['bandeira']
    search_fields = ['nome', 'endereco']

