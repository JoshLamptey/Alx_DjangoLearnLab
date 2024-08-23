from django.forms import ModelForm
from .models import Book
from django import forms

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]
    


class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)