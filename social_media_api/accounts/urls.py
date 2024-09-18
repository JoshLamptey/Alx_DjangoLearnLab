from django.urls import path,include 
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    path("/login", UserLoginView.as_view(), name='user_login'),
    path("/register", UserRegistrationView.as_view(), name='register'),
    path("api/accounts/", include('accounts.urls'))
]