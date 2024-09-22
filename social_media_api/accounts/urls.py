from django.urls import path,include 
from .views import UserRegistrationView, UserDetailView, UserLoginView, UnfollowUserView, FollowUserView


urlpatterns = [
    path("login/", UserLoginView.as_view(), name='user_login'),
    path("register/", UserRegistrationView.as_view(), name='register'),
    path("profile/<int:pk>/", UserDetailView.as_view(), name='user-detail'),
    path("follow/<int:user_id>/",  FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]