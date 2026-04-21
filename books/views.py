from django.shortcuts import render, get_object_or_404
from .models import Book

# Vista para la lista principal de libros
def book_list(request):
    libros = Book.objects.all()
    return render(request, 'books/home.html', {'libros': libros})

# Vista para ver la información de un solo libro
def detail_book(request, id):
    # get_object_or_404 es mejor porque si el libro no existe, da error 404 limpio
    libro = get_object_or_404(Book, id=id)
    return render(request, 'books/detail.html', {'libro': libro})