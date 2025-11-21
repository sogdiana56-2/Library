from django.urls import path
from .views import FilmListView, FilmCreateView, FilmUpdateView, FilmDeleteView, RegisterView, LoginUserView

urlpatterns = [
    path('film_list/', FilmListView.as_view(), name='film_list'),
    path('film/create/', FilmCreateView.as_view(), name='film_create'),
    path('film/<int:pk>/update/', FilmUpdateView.as_view(), name='film_update'),
    path('film/<int:pk>/delete/', FilmDeleteView.as_view(), name='film_delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
]
