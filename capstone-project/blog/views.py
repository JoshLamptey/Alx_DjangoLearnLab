from django.shortcuts import render
from rest_framework import viewsets,filters,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.authentication import authenticate
from rest_framework.pagination import PageNumberPagination
from .models import Post,Comment,Category,CustomUser,Like
from .serializers import CategorySerializer,CommentSerializer,PostSerializer,LikeSerializer,UserSerializer


# Create your views here.

class LoginView(APIView):
    def post (self, request, format=None):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                response = {
                    'message' : "Login successful",
                    'user' : user
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
            


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class PostViewSet(viewsets.ModelViewSet):
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