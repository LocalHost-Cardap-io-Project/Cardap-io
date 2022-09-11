from django.urls import path
from .views import ListMenu, DetailMenu, OrganizationSignupView, ClientSignupView

urlpatterns = [
    path('signup/organization/', OrganizationSignupView.as_view()),
    path('signup/client/', ClientSignupView.as_view()),
    path('menu/<int:pk>/', DetailMenu.as_view()),
    path('menu', ListMenu.as_view()),
]