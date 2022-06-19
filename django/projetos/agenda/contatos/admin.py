from django.contrib import admin
from . models import Categoria, Contato
# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone', 'email',
                    'data_criacao', 'categoria',)
    list_display_links = ('nome', 'sobrenome')
    # list_filter = ('nome', 'sobrenome')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
