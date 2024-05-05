from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="Enter Book ID")  # AutoField for automatic primary key generation
    title = serializers.CharField(label="Enter Book Title")
    author = serializers.CharField(label="Enter Author Names")

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance
