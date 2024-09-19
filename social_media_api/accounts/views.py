from django.shortcuts import render
from rest_framework import generics,permissions,serializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from .models import User

# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer  
    password = serializer.Charfield(max_length=10, blank=False)
    permission_classes = [permissions.AllowAny]





class UserLoginView(APIView):
    def post(self,request):
        user = get_user_model().objects.create_user
        if user:
            token, created = Token.objects.create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)



class UserListView(generics.GenericAPIView):
    """
    View to list all users in the system.
    Only accessible to authenticated users.
    """
    queryset = User.objects.all()  # Query all users
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)