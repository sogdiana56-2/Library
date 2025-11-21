from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views import generic

class CategoryView(generic.ListView):
    model = Product
    template_name = 'store/category_products.html'
    context_object_name = 'products'

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'store/categories.html'
    context_object_name = 'categories'

class ProductListView(generic.ListView):
    model = Product
    template_name = 'store/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['id'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context