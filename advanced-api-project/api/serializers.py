from rest_framework import serializers
from .models import Author,Book
import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        current_year = datetime.date.today().year
        if data > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return data


class AuthorSerializer(serializers.ModelSerializer):
    Book = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'Book'] 