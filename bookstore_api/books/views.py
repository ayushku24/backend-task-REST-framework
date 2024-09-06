from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from bookstore_api.authentication import AuthorTokenAuthentication

class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthorTokenAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price', 'publication_date']
    search_fields = ['title', 'author__name']
    ordering_fields = ['price', 'publication_date']

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]