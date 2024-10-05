from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,CommentViewSet,PostViewSet,CustomUserViewSet,LikeViewSet

router = DefaultRouter()
router.register(r'Posts', PostViewSet, basename='Posts')
router.register(r'Comments', CommentViewSet, basename='Comments')
router.register(r'Category', CategoryViewSet, basename='Categories')
router.register(r'User', CustomUserViewSet, basename='User')
router.register(r'Likes', LikeViewSet, basename='Likes')

urlpatterns = router.urls