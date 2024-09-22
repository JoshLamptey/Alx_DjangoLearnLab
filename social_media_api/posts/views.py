from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment,Like
from .serializer import PostSerializer, CommentSerializer,LikeSerializer
from notifications.models import Notification
from rest_framework.decorators import action, api_view
from django.shortcuts import get_object_or_404
from django.http import JsonResponse



# Create your views here.

@api_view(['POST'])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        return JsonResponse({'message': 'You have already liked this post'})
    

    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb='liked',
        target=post
    )

    return JsonResponse({'message': ' Post liked successfully.'})
#creating viewsets to handle CRUD operations

@api_view(['POST'])
def unlike_post(request, pk):
    pass






class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    
    def get_queryset(self):
        return Post.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        following= user.following.all()

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = []
