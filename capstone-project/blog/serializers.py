from rest_framework import serializers
from .models import CustomUser,Comment,Category,Post,Like
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer



class UserCreateSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username','password', 'date_of_birth', 'created_at']
        read_only_fields = ['created_at']
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr,value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save() 
        return instance



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
     