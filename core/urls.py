from django.urls import path


from core.views import usuario_logado, submit_login, logout_user


urlpatterns = [
    path('', usuario_logado, name='index'),
    path('submit', submit_login, name='index'),
    path('logout', logout_user, name='index'),
 ]
