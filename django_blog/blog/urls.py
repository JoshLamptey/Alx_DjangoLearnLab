from rest_framework.routers import DefaultRouter
from .views import LikeView,CommentViewset,PostViewset,AuthorView
from django.urls import path,include

router = DefaultRouter()
router.register(r'Post', PostViewset, basename='Post' )
router.register(r'Comment', CommentViewset, basename='Comments')
router.register(r'Like', LikeView, basename='Like')
router.register(r'Author', AuthorView , basename='Author')

urlpatterns = router.urls
