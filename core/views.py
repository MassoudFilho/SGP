from django.shortcuts import render


# Função usada para identificar se o usuário está logado no Admin.
def usuario_logado(request):
    # Verificar se o usuário está logado no Admin.
    # O usuário está logado no Admin se request.user é diferente de AnonymousUser.
    if str(request.user) != 'AnonymousUser':
        return render(request, 'index.html', {'logado': f"{request.user} logado no Admin!"})

    # Usuário não está logado no Admin se request.user é igual a AnonymousUser.
    else:
        return render(request, 'index.html', {'logado': 'Você não esta logado no Admin'})
