from rest_framework import serializers
from .models import CustomUser,Comment,Category,Post,Like
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'date_of_birth']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date', 'author', 'categories']
     

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'content', 'created_at', 'updated_at']
     
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['posts', 'author']
     