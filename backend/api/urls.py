from django.urls import path
from .views import ListMenu, DetailMenu

urlpatterns = [
    path('<int:pk>/', DetailMenu.as_view()),
    path('menu', ListMenu.as_view()),
]