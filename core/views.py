from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Função usada para identificar se o usuário está logado no Admin.
def usuario_logado(request):
    # Verificar se o usuário está logado no Admin.
    # O usuário está logado no Admin se request.user é diferente de AnonymousUser.
    if str(request.user) != 'AnonymousUser':
        return render(request, 'index.html', {'logado': f"{request.user} logado no Admin!"})

    # Usuário não está logado no Admin se request.user é igual a AnonymousUser.
    else:
        return render(request, 'index.html', {'logado': 'Você não esta logado no Admin'})


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválida')
    return redirect('/')


def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/')
