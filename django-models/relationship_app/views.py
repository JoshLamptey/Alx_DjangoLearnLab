from django.shortcuts import render,redirect
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import user_passes_test

#create your views here
def books_list(request):
    book_list = Book.objects.all()
    context = {
        'book_list' : book_list,
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'