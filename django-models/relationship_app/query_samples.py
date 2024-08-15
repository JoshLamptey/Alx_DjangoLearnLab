from relationship_app.models import Book, Librarian, Library, Author


author = Author.objects.get(name="Author Name")

Book.objects.filter(author=author)