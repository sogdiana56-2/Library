from django.shortcuts import render
from . import models
from django.views import generic


class AllThingsView(generic.ListView):
    model = models.Products
    template_name = 'waikiki/all.html'
    context_object_name = 'things'


class DressView(generic.ListView):
    model = models.Products
    template_name = 'waikiki/dress.html'
    context_object_name = 'dress'

    def get_queryset(self):
        return models.Products.objects.filter(tags__name='#платья')
    


class ShoesView(generic.ListView):
    model = models.Products
    template_name = 'waikiki/shoes.html'
    context_object_name = 'shoes'

    def get_queryset(self):
        return models.Products.objects.filter(tags__name='#обувь')



class OutwearView(generic.ListView):
    model = models.Products
    template_name = 'waikiki/outwear.html'
    context_object_name = 'outwear'

    def get_queryset(self):
        return models.Products.objects.filter(tags__name='#верхняя одежда')
