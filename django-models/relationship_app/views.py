from django.shortcuts import render,redirect
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import user_passes_test

#create your views here
def list_books(request):
    book_list = Book.objects.all()
    context = {
        'list_books' : list_books,
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_books')
        else:
            return render(request,'login.html', {'error': 'Invalid credentials.'})


    else:
        return render(request, 'relationship_app/login.html')
    


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'relationship_app/register.html', context)

#break-off point. I'll continue tomorrow