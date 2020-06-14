from django.contrib import admin

from .models import Atestado, Producao, PessoaCid


# Existem duas formas de registrar Atestado no admin:
# admin.site.register(Atestado, AtestadoAdmin)
# Através de decorator: @admin.register(Atestado)


@admin.register(Atestado)
class AtestadoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'doc_forma_envio', 'doc_data_recebido', 'data_inicio', 'data_fim',
                    'cid_principal', 'cid_secundario', 'cid_terceario')


@admin.register(Producao)
class ProducaoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'data')


admin.site.register(PessoaCid)
