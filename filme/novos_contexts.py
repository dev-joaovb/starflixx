from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {'lista_filmes_recentes': lista_filmes, 'filme_destaque': filme_destaque}

def lista_filmes_emAlta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacao')[0:8]
    return {'lista_filmes_emAlta': lista_filmes}
