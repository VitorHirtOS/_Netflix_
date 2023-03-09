from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISE", "Análise"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)

# criar filmes
class Filme(models.Model):
    thumb = models.ImageField(upload_to='thumb_filmes') # Upload dos filmes nesta pasta criada chamada 'thumb_filmes'
    titulo = models.CharField(max_length=100, null=True)
    descricao = models.TextField(blank=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS) # Dois argumentos o tamanho e a lista que tem o choises, além disso, precisamos criar a lista de categorias
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
    
    
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, null=True)
    video = models.URLField()
 
    def __str__(self):
        return  self.filme.titulo + " - " + self.titulo
    