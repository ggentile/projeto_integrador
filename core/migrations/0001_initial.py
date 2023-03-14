# Generated by Django 4.1.7 on 2023-03-14 02:09

import core.models
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remedio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=255, verbose_name='remedio')),
                ('descricao', models.TextField(max_length=200, verbose_name='descrição')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='preço')),
                ('imagem_remedio', stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem_remedio')),
            ],
            options={
                'verbose_name': 'Remédio',
                'verbose_name_plural': 'Remédios',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('criados', models.DateField(auto_now_add=True, verbose_name='data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('usuario_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('nome', models.CharField(max_length=40, verbose_name='nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='cpf')),
                ('email', models.EmailField(max_length=30, verbose_name='email')),
                ('telefone', models.CharField(max_length=11, verbose_name='telefone')),
                ('password', models.CharField(max_length=200, verbose_name='senha')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('status', models.CharField(choices=[(1, 'Aprovado'), (2, 'Reprovado'), (3, 'A caminho'), (4, 'Em separação')], max_length=25, verbose_name='Status')),
                ('data_pedido', models.DateTimeField(verbose_name='Data_pedido')),
                ('data_pagamento', models.DateTimeField(verbose_name='Data_pagamento')),
                ('data_separacao', models.DateTimeField(verbose_name='Data_separação')),
                ('data_saida', models.DateTimeField(verbose_name='Data_saida')),
                ('remedio_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.remedio', verbose_name='Remédio')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario', verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('endereco', models.CharField(max_length=255, verbose_name='endereço')),
                ('numero', models.IntegerField(verbose_name='numero')),
                ('bairro', models.CharField(max_length=70, verbose_name='bairro')),
                ('cidade', models.CharField(max_length=30, verbose_name='cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='estado')),
                ('cep', models.CharField(max_length=10, verbose_name='cep')),
                ('complemento', models.CharField(max_length=60, verbose_name='complemento')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario', verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
    ]
