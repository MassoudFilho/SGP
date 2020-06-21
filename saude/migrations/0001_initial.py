# Generated by Django 3.0.6 on 2020-05-25 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaudeDocumentoAfastamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField(verbose_name='Matricula')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('doc_forma_envio', models.CharField(max_length=35, verbose_name='Documento enviado por')),
                ('doc_data_recebido', models.DateField(verbose_name='Data de recebimento do documento')),
                ('data_inicio', models.DateField(verbose_name='Data início de afastamento')),
                ('data_fim', models.DateField(verbose_name='Data Fim de afastamento')),
                ('cid_principal', models.CharField(max_length=4, verbose_name='CID Principal')),
                ('cid_secundario', models.CharField(max_length=4, verbose_name='CID Secundário')),
                ('cid_terceario', models.CharField(max_length=4, verbose_name='CID Terceário')),
            ],
        ),
    ]