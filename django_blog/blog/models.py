from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Author(models.Model):
    author = models.CharField(max_length=25, blank=False)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# Comment model definition
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


class Like(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_post')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='liker')