from distutils.archive_util import make_zipfile
from operator import mod
from tkinter import CASCADE
from unicodedata import category
from xml.etree.ElementInclude import default_loader
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

# Create your models here.

class User(AbstractUser):
    is_organization = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Organization(models.Model):
    user = models.OneToOneField(User, related_name='organization', on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    RESTAURANTE = 1
    BEBIDAS = 2
    LANCHONETE = 3
    PADARIA = 4
    CONFEITARIA = 5
    OUTRO = 6
    ORGANIZATION_TYPE_CHOICES = (
      (RESTAURANTE, 'retaurante'),
      (BEBIDAS, 'bebidas'),
      (LANCHONETE, 'lanchonete'),
      (PADARIA, 'padaria'),
      (CONFEITARIA, 'confeitaria'),
      (OUTRO, 'outro'),
    )

    organization_type = models.PositiveSmallIntegerField(choices=ORGANIZATION_TYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Client(models.Model):
    user = models.OneToOneField(User, related_name='client', on_delete=models.CASCADE)
    estado_sg = models.CharField(max_length=2, blank=True, null=True)
    cidade_sg = models.CharField(max_length=2, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    rua = models.CharField(max_length=50, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)



    def __str__(self):
        return self.user.username

class Menu(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="images/menu-bg", null=True, blank=True)

    def __str__(self):
        return self.name

class Categoria(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="images/cat-bg", null=True, blank=True)
    description = models.TextField()

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# TODO
# Criar a tabela Produto e relacionar com a tabela Categoria. Não se esqueça da normalização

class Produto(models.Model):
    name = models.CharField(max_length=50, null=False)
    weight_in_grams = models.FloatField(null=False)
    price = models.FloatField(null=False)
    short_name = models.CharField(max_length=10, null=False)
    image = models.ImageField(upload_to='images/product', null=False, blank=True)
    description = models.TextField(null=False)

    category = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name
