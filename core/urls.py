from django.urls import path


from core.views import usuario_logado


urlpatterns = [
    path('', usuario_logado, name='index'),
 ]
