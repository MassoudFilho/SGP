from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Atestado, Producao

from .forms import AtestadoModelForm, ProducaoModelForm


# @login_required: Obriga o usuário a logar em Admin.
@login_required
def home_saude(request):
    return render(request, 'home_saude.html')


# @login_required: Obriga o usuário a logar em Admin.
@login_required
def atestado(request):
    # se o usuário enviou um POST para gente.
    if str(request.method) == 'POST':
        # se tem imagem usar também request.FILES: (request.POST, request.FILES)
        form = AtestadoModelForm(request.POST)
        if form.is_valid():  # o form está válido então

            prod = form.save()  # salva!!!

            messages.success(request, 'Produto salvo com sucesso.')
        else:
            messages.error(request, 'Erro ao salvar produção.')
    else:
        form = AtestadoModelForm()
    context = {
        'form': form
    }
    return render(request, 'atestado.html', context)


# @login_required: Obriga o usuário a logar em Admin.
@login_required
def producao(request):
    #  Verificar se o usuário está logado no Admin.
    # AnonymousUser é a denominação usada quando não está logado.
    if str(request.user) != 'AnonymousUser':
        # se o usuário enviou um POST para gente.
        if str(request.method) == 'POST':
            # Verificanco o método que foi enviado.
            # Se tem imagem usar também request.FILES: (request.POST, request.FILES)
            form = ProducaoModelForm(request.POST)
            # se o formulário é válido.
            if form.is_valid():
                # salvar os dados.
                prod = form.save()
                # Mostrar a mensagem.
                messages.success(request, 'Produto salvo com sucesso.')
            else:
                # Se houve algum erro (formulário não é válido).
                messages.error(request, 'Erro ao salvar produção.')
        else:
            form = ProducaoModelForm()
        context = {
            'form': form
        }
        return render(request, 'producao.html', context)
    else:
        return HttpResponse('Você precisa estar logado')


# @login_required: Obriga o usuário a logar em Admin.
@login_required
def mostraproducao(request):
    context = {
        'producao': Producao.objects.all()
    }
    return render(request, 'mostraproducao.html', context)
