from django.contrib import admin
from .models import Menu, Categoria, User, Organization, Client

# Register your models here.

admin.site.register(Menu)
admin.site.register(Categoria)
admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Client)
