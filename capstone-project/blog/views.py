from django.shortcuts import render
from rest_framework import viewsets,filters,status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Post,Comment,Category,CustomUser,Like
from .serializers import CategorySerializer,CommentSerializer,PostSerializer,LikeSerializer,UserSerializer


# Create your views here.

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