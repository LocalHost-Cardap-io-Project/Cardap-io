from rest_framework import serializers
from menu.models import Menu, Categoria, Categoria_Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'autor', 'name', 'img')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'name', 'img', 'desc')

class CategoriaMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria_Menu
        fields = ('id_menu', 'id_categoria')