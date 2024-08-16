from django.urls import path
from .views import books_list,LibraryDetailView
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('books/', books_list, name="books_list"),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(),name='logout')
]