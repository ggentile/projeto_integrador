from django import forms
from django.core.mail.message import EmailMessage
from .models import Usuario, Endereco


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
        