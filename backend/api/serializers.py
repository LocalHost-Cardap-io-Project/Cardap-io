from rest_framework import serializers
from menu.models import User, Organization, Client, Menu, Categoria

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_client')

class OrganizationSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email','password', 'password2')
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
    
    def save(self, **kwargs):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"error":"password does not match"})
        user.set_password(password)
        user.is_organization = True
        user.save()
        Organization.objects.create(user=user)

        return user

class ClientSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email','password', 'password2')
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def save(self, **kwargs):
        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"error":"password does not match"})
        user.set_password(password)
        user.is_client = True
        user.save()
        Client.objects.create(user=user)

        return user

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'organization', 'name', 'img')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'img', 'desc')

