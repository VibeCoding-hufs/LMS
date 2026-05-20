from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserRegisterSerializer(user).data, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            login_id = serializer.validated_data['login_id']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(login_id=login_id)
                if check_password(password, user.password):
                    return Response({'message': 'Login successful'}, status=200)
                return Response({'message': 'Invalid credentials'}, status=401)
            except User.DoesNotExist:
                return Response({'message': 'Invalid credentials'}, status=401)
        return Response(serializer.errors, status=400)