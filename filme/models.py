from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

#Criar o filme
LISTA_CATEGORIAS = (
    ('ACAO', 'Ação'),
    ('COMEDIA', 'Comédia'),
    ('DRAMA', 'Drama'),
    ('ROMANCE', 'Romance'),
    ('DOCUMENTARIO', 'Documentário'),
    ('SUSPENSE', 'Suspense'),
    ('TERROR', 'Terror'),
    ('FICCAO_CIENTIFICA', 'Ficção Científica'),

)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    visualizacao = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

#Criar os episodios
class Episodio(models.Model):
    filme = models.ForeignKey('Filme', related_name= 'episodios', on_delete= models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.titulo + ' - ' + self.filme.titulo

#Criar usuarios
class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('Filme')