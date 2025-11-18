from django.urls import path
from .views import BookListView, BookDetailView, search_books

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='book'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book_detail'),
    path('search/', search_books, name='search_books'),
]
