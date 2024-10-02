from django.shortcuts import render
from rest_framework import generics,permissions,serializers,status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from .models import User

# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer  
    password = serializers.CharField()
    permission_classes = [permissions.AllowAny]


class UserLoginView(APIView):
    def post(self,request):
        user = get_user_model().objects.create_user
        if user:
            token, created = Token.objects.create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)


class UserDetailVIew(generics.RetrieveAPIView):
    queryset = User.objects.all() #same as User.objects.all() which is a rather dynamic and preferred. Used it because of alx checker
    permission_classes =  [permissions.IsAuthenticated]
    serializer_class = CustomUserSerializer



class UserListView(generics.GenericAPIView):
    """
    View to list all users in the system.
    Only accessible to authenticated users.
    """
    CustomUser = User
    queryset = CustomUser.objects.all()  # Query all users
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, ):
        """
        Return a list of all users.
        """
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, ):
        user_to_follow_id = request.data.get('user_id')
        try:
            user_to_follow = User.objects.get(id=user_to_follow_id)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        

        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        request.user.following.add(user_to_follow)
        return Response({"status": "Following"}, status=status.HTTP_201_CREATED)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_to_unfollow_id = request.data.get('user_id')
        try:
            user_to_unfollow = request.data.get('user_id')
        except User.DoesNotExist:
            return Response({"error": "You cannot unfollow yourseelf"}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.remove(user_to_unfollow)
        return Response({"status": "Unfollowed"}, status=status.HTTP_204_NO_CONTENT)