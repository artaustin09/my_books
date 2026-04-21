from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='home'),
    
    path('home/', views.book_list, name='home_alt'),
    
    path('book/<int:id>/', views.detail_book, name='detail_book'),
]