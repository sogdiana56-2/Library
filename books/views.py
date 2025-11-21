from django.shortcuts import render, get_object_or_404
from . import models
from django.db.models import Avg
from django.views import generic


class SearchView(generic.View):
    def get(self, request):
        query = self.request.GET.get('s', '')
        if query:
            book = models.Book.objects.filter(title__icontains=query)
        else:
            book = models.Book.objects.none()
        context = {
                'book': book,
                's': query
            }
        return render(request, 'books/book.html', context)


class BookListView(generic.ListView):
    template_name = 'books/book.html'
    model = models.Book
    context_object_name = 'book'
    ordering = ['-id']



class BookDetailView(generic.DetailView):
    template_name = 'books/book_detail.html'
    model = models.Book
    pk_url_kwarg = 'id'
    context_object_name = 'book_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.get_object()
        average_rating = models.Reviews.objects.filter(choice_book=book_id).aggregate(Avg('mark'))['mark__avg']
        context['average_rating'] = round(average_rating, 1)
        return context