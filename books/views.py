from django.views.generic import ListView, DetailView
from django.shortcuts import render
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


    def search_books(request):
        q = request.GET.get('q', '')
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_books.html', {'books': books, 'q': q})


