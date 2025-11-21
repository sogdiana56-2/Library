from django.urls import path
from . import views

urlpatterns = [
    path('all_things/', views.AllThingsView.as_view(), name='all_things'),
    
    path('dress/', views.DressView.as_view(), name='dress'),
    
    path('shoes/', views.ShoesView.as_view(), name='shoes'),
    
    path('outwear/', views.OutwearView.as_view(), name='outwear'),
]