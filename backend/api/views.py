from rest_framework import generics
from menu.models import Menu, Categoria, Categoria_Menu
from .serializers import MenuSerializer

# Create your views here.

class ListMenu(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class DetailMenu(generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
