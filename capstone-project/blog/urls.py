from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import CategoryViewSet,CommentViewSet,PostViewSet,LoginView,CustomUserViewSet,LikeViewSet

router = DefaultRouter()
router.register(r'Posts', PostViewSet, basename='Posts')
router.register(r'Comments', CommentViewSet, basename='Comments')
router.register(r'Category', CategoryViewSet, basename='Categories')
router.register(r'User', CustomUserViewSet, basename='User')
router.register(r'Likes', LikeViewSet, basename='Likes')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/LoginView/', LoginView.as_view(), name='Login')
]