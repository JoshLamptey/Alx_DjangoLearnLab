from django.urls import path  
from django.contrib import admin  
from .views import register  
from django.contrib.auth import views as auth_views
from . import views 
  

urlpatterns = [  
    path("/login", views.login,  name='login'),
    path("login_user/", auth_views.LoginView.as_view(template_name='templates/login.html'), name='login'),
    path("/logout", auth_views.LogoutView.as_view(template_name='templates/logout.html'), name='logout'),
    path("/profile",views.profile, name = 'profile' ),
    path("admin/", admin.site.urls),  
    path("register", register, name = 'register')
]