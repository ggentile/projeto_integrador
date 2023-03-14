from django import forms
from django.core.mail.message import EmailMessage
from .models import Usuario, Endereco
import requests


attribs = {
    'is_required': True
}

class LoginForm(forms.Form):
    user = forms.EmailField(label='email', max_length=50, required=True)
    password = forms.PasswordInput(attrs=attribs)

    def valida_usuario(self):
        usuario = Usuario.objects.get(name=self.user, password=self.password)
        return usuario

    def user_login(self):
        if self.user is not None:
            check_user = self.valida_usuario()
            if check_user is None:
                return False
            else:
                return self.user

class CadastroForm(forms.Form):

    correcoes = []

    nome  = forms.CharField(label='nome', max_length=100, required=True)
    sobrenome = forms.CharField(label='sobrenome', max_length=100, required=True)
    cpf = forms.CharField(label='cpf', max_length=11, required=True)
    data_nascimento = forms.DateField(label='Data Nascimento', required=True)
    endereco = forms.CharField(label='endereço', max_length=100, required=True)
    numero = forms.IntegerField(label='numero', required=True)
    bairro = forms.CharField(label='Bairro', max_length=40, required=True)
    cidade = forms.CharField(label='cidade', max_length=30, required=True)
    estado = forms.CharField(label='Estado', max_length=2, required=True)
    cep = forms.CharField(label='Cep', max_length=8, required=True)
    complemento = forms.CharField(label='Complemento', max_length=100)
    email = forms.EmailField(label='email', required=True)
    password = forms.PasswordInput(attrs=attribs)
    
    cadastro = {
        'nome': nome,
        'sobrenome': sobrenome,
        'cpf': cpf,
        'data_nascimento': data_nascimento,
        'endereco': endereco,
        'numero': numero,
        'bairro': bairro,
        'cidade': cidade,
        'estado': estado,
        'cep': cep,
        'complemento': complemento,
        'email': email,
        'password': password
    }


    def valida_dados(self) -> bool:     
        for k, v in self.cadastro:
            if v is not None:
                pass
            else:
                self.correcoes.append(k)

        if self.correcoes != []:
            return False
        else:
            return True

    def cadastra_usuario(self):
        message = []
        valida = self.valida_dados()
        if valida == True:
            Usuario.objects.create(nome=self.nome, cpf=self.cpf, email=self.email, password=self.password)
            Endereco.objects.create(endereco=self.endereco, numero=self.numero, bairro=self.bairro, cidade=self.cidade, estado=self.estado, cep=self.cep, complemento=self.complemento)
            res = 200
            return res
        else:
            for values in self.correcoes:
                m = f'Preencher {values} para prosseguir com cadastro'

                message.append(m)
            return message
        
class AtualizaInfoPessoais(forms.Form):

    nome_completo = forms.CharField(label='nome_completo', max_length=100)
    cpf_cliente = forms.CharField(label='cpf_client', max_length=11)

    def atualiza(self):
        cliente = Usuario.objects.get(nome=requests.session['nome'], cpf=requests.session['cpf'])

        cliente.nome = self.nome_completo
        cliente.cpf = self.cpf_cliente

        cliente.save()
        return True

class AtualizaDadosContato(forms.Form):
    email_novo = forms.EmailField(label='email', max_length=100, required=True)
    telefone_novo = forms.CharField(label='telefone', max_length=11, required=True)


    def atualiza_dados(self):
        cliente = Usuario.objects.get(nome=requests.session['nome'], cpf=requests.session['cpf'])

        cliente.email = self.email_novo
        cliente.telefone = self.telefone_novo

        cliente.save()

        return True
    
class AtualizaEndereco(forms.Form):
    endereco_novo = forms.CharField(label='endereço', max_length=100, required=True)
    numero_novo = forms.IntegerField(label='numero', required=True)
    complemento_novo = forms.CharField(label='Complemento', max_length=100)
    bairro_novo = forms.CharField(label='Bairro', max_length=40, required=True)
    cidade_nova =  forms.CharField(label='cidade', max_length=30, required=True)
    estado_novo = forms.CharField(label='Estado', max_length=2, required=True)
    cep_novo = forms.CharField(label='Cep', max_length=8, required=True)
 

    def atualiza_ender(self):
        addr = Endereco.objects.get(endereco=requests.session['endereco'], numero=requests.session['numero'], usuario_id=requests.session['usuario_id'])

        addr.endereco = self.endereco_novo
        addr.numero = self.numero_novo
        addr.bairro = self.bairro_novo
        addr.cidade = self.cidade_nova
        addr.estado = self.estado_novo
        addr.cep = self.cep_novo
        addr.complemento = self.complemento_novo

        addr.save()
        
        return True