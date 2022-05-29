from django.db import models


# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=40)
    titulo = models.CharField(max_length=70)
    descricao = models.CharField(max_length=250)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor}: {self.titulo}"


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=40)
    pontuacao = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome}: {self.pontuacao}"
