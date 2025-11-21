from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Film
from .forms import FilmForm

class RegisterView(FormView):
    template_name = 'CineBoard/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('film_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class LoginUserView(LoginView):
    template_name = 'CineBoard/login.html'

class FilmListView(ListView):
    model = Film
    template_name = 'CineBoard/film_list.html'
    context_object_name = 'films'

    def get_queryset(self):
        qs = Film.objects.all()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(title__icontains=q)
        genre = self.request.GET.get("genre")
        if genre:
            qs = qs.filter(genre=genre)
        return qs

class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'CineBoard/film_form.html'
    success_url = reverse_lazy('film_list')

class FilmUpdateView(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'CineBoard/film_form.html'
    success_url = reverse_lazy('film_list')

class FilmDeleteView(DeleteView):
    model = Film
    template_name = 'CineBoard/film_confirm_delete.html'
    success_url = reverse_lazy('film_list')
