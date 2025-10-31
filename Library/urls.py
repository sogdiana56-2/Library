from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('time/', views.time_message, name='time'),
    path('quote/', views.random_quote, name='CC'),
]
