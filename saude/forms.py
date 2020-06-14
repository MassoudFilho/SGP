from django import forms

from .models import Atestado, Producao


class AtestadoModelForm(forms.ModelForm):
    class Meta:
        model = Atestado  # o Formulário usa o modelo Atestado.
        fields = ['matricula', 'nome', 'doc_forma_envio', 'doc_data_recebido', 'data_inicio', 'data_fim',
                    'cid_principal', 'cid_secundario', 'cid_terceario']


class ProducaoModelForm(forms.ModelForm):
    class Meta:
        model = Producao  # o Formulário utiliza o modelo Producao.
        fields = ['matricula', 'nome', 'data']
