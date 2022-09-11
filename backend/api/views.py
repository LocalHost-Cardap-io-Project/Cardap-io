from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from menu.models import User, Organization, Client, Menu, Categoria
from .serializers import UserSerializer, OrganizationSignupSerializer, ClientSignupSerializer, MenuSerializer

# Create your views here.

class OrganizationSignupView(generics.GenericAPIView):
    serializer_class = OrganizationSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "token" : Token.objects.get(user=user).key,
            "message" : "Organization account created succesfuly."
        })

class ClientSignupView(generics.GenericAPIView):
    serializer_class = ClientSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "token" : Token.objects.get(user=user).key,
            "message" : "Client account created succesfuly."
        })

class ListMenu(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class DetailMenu(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
