from django.urls import path
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='accounts/login.html'),  # View que o Django disponibiliza.
          name='login'),
]


"""
urlpatterns = [
    path('entrar/',
         LoginView.as_view(template_name='accounts/login.html'),  # View que o Django disponibiliza.
          name='login'),
]
"""