from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Book
        fields = ['id','title','author','publish_date','created_at','cover_image']