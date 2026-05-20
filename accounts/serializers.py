from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['login_id', 'password', 'name', 'email', 'role', 'dept']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['login_id', 'password']