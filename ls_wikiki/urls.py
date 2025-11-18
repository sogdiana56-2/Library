from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Привет! Это главная страница.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),  # <-- вот корень сайта
]
