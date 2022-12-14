from django.urls import path
from .views import (    
    ListMenu,
    DetailMenu,
    OrganizationSignupView,
    ClientSignupView,
    CustomAuthToken,
    LogoutView,
    ClientOnlyView,
    OrganizationOnlyView
)


urlpatterns = [
    path('signup/organization/', OrganizationSignupView.as_view()),
    path('signup/client/', ClientSignupView.as_view()),
    path('login/', CustomAuthToken.as_view()),
    path('logout/', LogoutView.as_view()),
    path('client/dashboard/', ClientOnlyView.as_view()),
    path('organization/dashboard/', OrganizationOnlyView.as_view())

    
    # path('menu/<int:pk>/', DetailMenu.as_view()),
    # path('menu', ListMenu.as_view()),
]