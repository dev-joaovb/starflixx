#url - view - template

"""
URL configuration for starflix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, reverse_lazy
from django.urls import include
from .views import Homepage, HomeFilmes, DetalhesFilme, PesquisaFilme, PaginaPerfil, CriarConta
from django.contrib.auth import views as auth_views

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homepage_filmes'),# Acessar o filmes
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name='detalhesFilme'), # Detalhe Filme
    path('pesquisa/', PesquisaFilme.as_view(), name= 'pesquisaFilme'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarPerfil/<int:pk>', PaginaPerfil.as_view(), name='editarPerfil'),
    path('criarConta/', CriarConta.as_view(), name='criarConta'),
    path('mudarSenha/', auth_views.PasswordChangeView.as_view(template_name='editarPerfil.html', success_url=reverse_lazy('filme:homepage_filmes')),name='mudarSenha'),
]
