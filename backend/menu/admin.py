from django.contrib import admin
from .models import Menu, Categoria, Categoria_Menu

# Register your models here.

admin.site.register(Menu)
admin.site.register(Categoria)
admin.site.register(Categoria_Menu)
