from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
#Custom User Manager since i am using Abstract User
class CustomUserManager(BaseUserManager):
    def create_user(self, email,username, password=None, **extra_fields):
        if not email:
            raise ValueError('The email Field is not set please')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(self, email, password, **extra_fields)

#User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username'
    ]
#model for the categories
class Category(models.Model):
    category = models.CharField(max_length=30)

# Post model
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='+' )
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='post')

#comment feature model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='commenter')
    content =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

#Like feature model    
class Like(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_posts')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='liker')


