from django.db import models


class Atestado(models.Model):
    matricula = models.IntegerField('Matricula')
    nome = models.CharField('Nome', max_length=100)
    doc_forma_envio = models.CharField('Documento enviado por', max_length=35)
    doc_data_recebido = models.DateField('Data de recebimento do documento')
    data_inicio = models.DateField('Data início de afastamento')
    data_fim = models.DateField('Data Fim de afastamento')
    cid_principal = models.CharField('CID Principal', max_length=4)
    cid_secundario = models.CharField('CID Secundário', max_length=4)
    cid_terceario = models.CharField('CID Terceário', max_length=4)


class Producao(models.Model):
    matricula = models.IntegerField('Matricula')
    nome = models.CharField('Nome', max_length=50)
    data = models.DateField('Data')


class PessoaCid(models.Model):
    matricula = models.IntegerField('Matricula')
    datainicial = models.DateField('Data Inicial')
    datafinal = models.DateField('Data Final')
    dias = models.IntegerField('Dias')
    codigo = models.IntegerField('Código')
    afastamento = models.CharField('Afastamento', max_length=50)
    cadastro = models.CharField('Cadastro', max_length=50)
    cid = models.CharField('CID', max_length=20)
    nome = models.CharField('Nome', max_length=50)
    sexo = models.CharField('Sexo', max_length=15)
    idade = models.IntegerField('Idade')
    vinculo = models.CharField('Vinculo', max_length=30)
    comarca = models.CharField('Comarca', max_length=50)
    centroCusto = models.CharField('Centro de Custo', max_length=50)
    apoioDiretoIndireto = models.CharField('Grau', max_length=50)
    area = models.CharField('Area', max_length=50)
    areasub = models.CharField('Sub Área', max_length=50)
    maxlotaexer = models.CharField('Lotação', max_length=50)
