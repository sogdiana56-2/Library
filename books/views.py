from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book.html'
    context_object_name = 'books'
    paginate_by = 10
    queryset = Book.objects.filter(is_published=True)

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


