from django.db import models

class Computador(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    peso = models.DecimalField(max_digits=4, decimal_places=2)
    linha = models.CharField(max_length=20)