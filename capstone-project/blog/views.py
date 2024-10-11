from rest_framework import viewsets,filters,status
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from rest_framework.authentication import authenticate
from rest_framework import generics
from .models import Post,Comment,Category,CustomUser,Like
from .serializers import CategorySerializer,CommentSerializer,PostSerializer,LikeSerializer,UserSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class LoginView(LoginView):
    template_name = 'login.html'
    success_url = 'api/root/'
            


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class PostViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
    login_url = ''
    redirect_field_name = 'api/roots/Posts'

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author','categories', 'published_date']

    def get(self, request, *args, **kwargs):
        #fetch the filtered queryset
        queryset = self.filter_queryset(self.get_queryset())

        #paginate the request
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        #if no data is paginated return the full response
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer