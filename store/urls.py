from django.urls import path
from . import views

urlpatterns = [
    path('categories/<int:id>/', views.CategoryView.as_view(), name='category_products'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('products/', views.ProductListView.as_view(), name='products'),
]   