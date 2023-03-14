from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Endereco, Pedido, Usuario, Remedio
from .forms import LoginForm, CadastroForm, AtualizaInfoPessoais, AtualizaDadosContato

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


class HistoricalView(FormView):
    template_name = 'historico_pedido.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Pedidos'] = Pedido.objects.order_by('Data_pedido').all()
        return context

class DadosPessoaisView(FormView):
    template_name = 'menu_dados_pessoais.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
class InformacoesPessoaisView(FormView):
    template_name = 'informacoes_pessoais.html'
    form_class = AtualizaInfoPessoais

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao atualizar conta')
        return super(InformacoesPessoaisView, self).form_invalid(form, *args, **kwargs)
    
    def form_valid(self, form, *args, **kwargs):
        atualiza = form.atualiza()
        if atualiza == True:
            messages.success(self.request, 'Atualização feita com sucesso')
            return super(InformacoesPessoaisView, self).form_valid(form, *args, **kwargs)
        else:
            self.form_invalid()

class DadosContatoView(FormView):
    template_name = 'dados_contato.html'
    form_class = AtualizaDadosContato

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao atualizar conta')
        return super(DadosContatoView, self).form_invalid(form, *args, **kwargs)
    
    def form_valid(self, form, *args, **kwargs):
        atualiza = form.atualiza_dados()
        if atualiza == True:
            messages.success(self.request, 'Atualização feita com sucesso')
            return super(DadosContatoView, self).form_valid(form, *args, **kwargs)
        else:
            self.form_invalid()


class AtualizaEnderecoView(FormView):
        template_name = 'dados_contato.html'
        form_class = AtualizaDadosContato

        def get_context_data(self, **kwargs):
            return super().get_context_data(**kwargs)
    
        def form_invalid(self, form, *args, **kwargs):
            messages.error(self.request, 'Erro ao atualizar conta')
            return super(DadosContatoView, self).form_invalid(form, *args, **kwargs)
    
        def form_valid(self, form, *args, **kwargs):
            atualiza = form.atualiza_ender()
            if atualiza == True:
                messages.success(self.request, 'Atualização feita com sucesso')
                return super(DadosContatoView, self).form_valid(form, *args, **kwargs)
            else:
                self.form_invalid()