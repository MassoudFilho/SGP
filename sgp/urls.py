from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('sgp/', include('saude.urls')),
    path('contas/', include('django.contrib.auth.urls')),
]


"""
Alterar Textos no ADMIN.
"""
# Cabeçalho do site.
admin.site.site_header = 'Secretaria de Gestão de Pessoas do TJPA'
# Título da página.
admin.site.site_title = 'SGP'
# Título da página índice.
admin.site.index_title = 'Sistema de Gerenciamento'
