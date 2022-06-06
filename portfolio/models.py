from django.db import models


# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=40)
    titulo = models.CharField(max_length=70)
    descricao = models.TextField(max_length=250)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor}: {self.titulo}"


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=40)
    pontuacao = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome}: {self.pontuacao}"


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    linkedin = models.URLField(blank=True, default='')

    def __str__(self):
        return f"{self.nome}"


class Projeto(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.TextField(max_length=400)
    imagem = models.ImageField(upload_to="pictures/")

    def __str__(self):
        return f"{self.titulo}"


class Cadeira(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField(default=1)
    anoLetivo = models.CharField(max_length=10)
    semestre = models.IntegerField(default=1)
    ects = models.IntegerField(default=1)
    professor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, default="")
    rank = models.IntegerField(default=1)
    descricao = models.TextField(max_length=500)
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nome}"


class Picture(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pictures/', blank=True)
