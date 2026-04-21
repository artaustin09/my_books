# books/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Cambia el string vacío '' por 'home/'
    path('home/', views.home, name='home'), 
    path('detail_book/<int:id>/', views.detail_book, name='detail_book'),
]