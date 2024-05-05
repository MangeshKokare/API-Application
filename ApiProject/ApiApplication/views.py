from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer  # Import the BookSerializer from your serializers.py file

class BookApiView(APIView):
    serializer_class = BookSerializer  # Use serializer_class instead of serializers_class

    def get(self, request):
        all_books = Book.objects.all()
        serializer = self.serializer_class(all_books, many=True)
        return Response({"Message": "List of Books", "Book List": serializer.data})
    
    def post(self, request):
        print("request data is :", request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            new_book = serializer.save()  # Save the validated data to create a new book instance
            return Response({"Message": "New Book created", "Book": {
                "id": new_book.id,
                "title": new_book.title,
                "author": new_book.author
            }})
        else:
            return Response(serializer.errors, status=400)  # Return validation errors if data is invalid
