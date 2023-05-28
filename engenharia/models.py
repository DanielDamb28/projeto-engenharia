from django.db import models

# Create your models here.

class Usuario(models.Model):
    first_name = models.CharField(max_length=60, default=" ")
    last_name = models.CharField(max_length=60, default=" ")
    cpf = models.CharField(max_length=15, default=" ")
    email = models.EmailField(default=" ")
    telefone = models.CharField(max_length=20, default=" ")
    password = models.CharField(max_length=40, default=" ")
