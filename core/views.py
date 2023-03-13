from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Endereco, Pedido, Usuario, Remedio
from .forms import LoginForm, CadastroForm

# Create your views here.
class IndexView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao acessar a conta.\nVerifique login e senha estão corretos')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
    
    def form_valid(self, form, *args, **kwargs):
        valida_login = form.user_login()
        if valida_login is not None:
            messages.success(self.request, 'Login efetuado com sucesso')
            return super(MainView, self).form_valid(form, *args, **kwargs)
        else:
            self.form_invalid()

class CreateView(FormView):
    template_name = 'cadastro.html'
    form_class = CadastroForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form, *args, **kwargs):
        valida_cadastro = form.cadastra_usuario()
        if valida_cadastro == 200:
            messages.success(self.request, 'Cadastro realizado com sucesso')
            return super(IndexView, self).form_valid(form, *args, **kwargs)
        else:
            self.form_invalid(message=valida_cadastro)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, self.valid_cadastro)
        return super(CreateView, self).form_invalid(form, *args, **kwargs)

    
class MainView(FormView):
    template_name = 'tela_inicial.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
