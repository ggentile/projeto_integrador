from django.urls import path
from .views import IndexView, MainView, DadosPessoaisView, DadosContatoView, AtualizaEnderecoView, CreateView

urlpatterns = [
    path('', IndexView.as_view(), name='login'),
    path('cadastro', CreateView.as_view(), name='create'),
    path('dashboard/<str:username>', MainView.as_view(), name='dashboard'),
    path('dadospessoais', DadosPessoaisView.as_view(), name='dadospessoais'),
    path('dadoscontato', DadosContatoView.as_view(), name='dadoscontato'),
    path('atualizaendereco', AtualizaEnderecoView.as_view(), name='atualizaendereco'),
]
