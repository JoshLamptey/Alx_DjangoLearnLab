from django.shortcuts import render,redirect
from typing import Any
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.db import transaction
from .models import Book,Library

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    response = "\n".join([f"Title: {book.title}, Author: {book.author}" for book in books])

    return HttpResponse(response, content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'templates/relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.book_set.all() 
        return context
    