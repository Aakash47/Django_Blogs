from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('<slug:slug>/', views.blogpost.as_view(), name='Blogpost')
    
]