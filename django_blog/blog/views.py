from .models import Post,Comment,Like,Author
from rest_framework import viewsets
from .serializers import CommentSerializer,PostSerializer,LikeSerializer,AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LikeView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer