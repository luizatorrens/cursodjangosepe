from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=40)

    def __str__(self):
        return self.descricao
    
class TipoAtuação(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural= 'Tipos de Atuação'
    
class Pais(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural= 'Países'

class Produtora(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.pais})"
    
class Membro(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    sinopse = models.TextField()
    classificacao = models.IntegerField()
    duracao = models.TimeField()
    produtora = models.ForeignKey(Produtora, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.titulo} ({self.ano})"