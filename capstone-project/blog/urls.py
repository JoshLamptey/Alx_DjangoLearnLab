from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import CategoryViewSet,CommentViewSet,PostViewSet,LoginView,CustomUserViewSet,LikeViewSet,RegisterView


#using DRF in built default router to create endpoints for the views 
router = DefaultRouter()
router.register(r'Posts', PostViewSet, basename='Posts')
router.register(r'Comments', CommentViewSet, basename='Comments')
router.register(r'Category', CategoryViewSet, basename='Categories')
router.register(r'User', CustomUserViewSet, basename='User')
router.register(r'Likes', LikeViewSet, basename='Likes')


urlpatterns = [
    path('api/root/', include(router.urls)),
    #separate endpoints for the login and register views
    path('', LoginView.as_view(next_page='api/root/'), name='Login' ),
    path('api/register/', RegisterView.as_view(), name='Register')
]