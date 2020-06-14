from django.urls import path

from saude.views import home_saude, atestado, producao, mostraproducao


urlpatterns = [
    path('saude/', home_saude, name='home_saude'),
    path('saude/atestado/', atestado, name='atestado'),
    path('saude/producao/', producao, name='producao'),
    path('saude/mostraproducao/', mostraproducao, name='mostraproducao'),
]
