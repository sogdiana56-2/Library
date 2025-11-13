from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]
urlpatterns = [
    path('users/', include('users.urls')),
    path('captcha/', include('captcha.urls')),
]

