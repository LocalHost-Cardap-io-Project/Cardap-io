from distutils.archive_util import make_zipfile
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="images/cat-bg", null=True, blank=True)
    desc = models.TextField()


class Menu(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="images/menu-bg" ,null=True, blank=True)


class Categoria_Menu(models.Model):
    id_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

# TODO
# Criar a tabela Produto e relacionar com a tabela Categoria. Não se esqueça da normalização

class Produto(models.Model):
    pass

