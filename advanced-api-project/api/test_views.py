from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book,Author 
from django.contrib.auth.models import User 

class BooKAPITests(APITestCase):

    def setUp(self):
        #create the user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        #create an author\
        self.author = Author.objects.create(name='Josh Wood')

        #create a book 
        self.book = Book.objects.create(title='Sample Book', publication_year=2024, author=self.author)


    def test_create_book(self):
        "testing the create method"
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year" : 2024,
            "author" : self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.staus_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, "New Book")


    def test_get_book_list(self):
        #test the Detailview
        url = reverse('book-list')
        response = self.client.get(url, format='jsin')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_book_detail(self):
        #retrieving a single book by ID
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        response = self.client.get(url, foemat='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)


    def test_update_book(self):
        #test updating a book
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-update', kwargs={'pk':self.book.id})
        data = {
            "title": "Updated Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get.id(self.book.id).title, "Updated Book")

    def test_delete_book(self):
        #test the delete book
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-delete', kwargs={'pk': self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_permissions(self):
        #test that unauthorised users can't perform actions
        create_url = reverse('book-create')
        update_url = reverse('book-update', kwargs={'pk': self.book.id})
        delete_url = reverse('book-delete', kwargs={'pk': self.book.id})

        #unauthenticated create attempt
        response = self.client.post(create_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


        #unauthenticated update attempt 
        response = self.client.post(create_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        #unauthenticated delete attempt
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
