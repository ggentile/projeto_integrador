from django.db import models
from django import forms
import uuid
from stdimage.models import StdImageField


def get_file_path(instance, filename: str) -> str:
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('data de criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Usuario(Base):
    usuario_id   = models.IntegerField('id', primary_key=True)
    nome = models.CharField('nome', max_length=40)
    cpf = models.CharField('cpf', max_length=11)
    email = models.EmailField('email', max_length=30)
    telefone = models.CharField('telefone', max_length=11)
    password = models.CharField('senha', max_length=200)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __str__(self) -> str:
        return self.nome
    
class Endereco(Base):
    endereco = models.CharField('endereço', max_length=255)
    numero = models.IntegerField('numero')
    bairro = models.CharField('bairro', max_length=70)
    cidade = models.CharField('cidade', max_length=30)
    estado = models.CharField('estado', max_length=2)
    cep = models.CharField('cep', max_length=10)
    complemento = models.CharField('complemento', max_length=60)
    usuario_id = models.ForeignKey('core.Usuario', verbose_name='Usuário', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self) -> str:
        return self.endereco
    

class Remedio(Base):
    nome = models.CharField('remedio', max_length=255)
    descricao = models.TextField('descrição', max_length=200)
    preco = models.DecimalField('preço', max_digits=10, decimal_places=2)
    imagem_remedio = StdImageField('Imagem_remedio', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = 'Remédio'
        verbose_name_plural = 'Remédios'

    def __str__(self) -> str:
        return self.nome

class Pedido(Base):
    STATUS = (
        (1, 'Aprovado'),
        (2, 'Reprovado'),
        (3, 'A caminho'),
        (4, 'Em separação')
    )

    status = models.CharField('Status', max_length=25, choices=STATUS)
    data_pedido = models.DateTimeField('Data_pedido')
    data_pagamento = models.DateTimeField('Data_pagamento')
    data_separacao = models.DateTimeField('Data_separação')
    data_saida = models.DateTimeField('Data_saida')
    usuario_id = models.ForeignKey('core.Usuario', verbose_name='Usuário', on_delete=models.CASCADE)
    remedio_id = models.ForeignKey('core.Remedio', verbose_name='Remédio', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self) -> str:
        return self.status
    
