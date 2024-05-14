from django.shortcuts import render
from .models import Book


def allBooks(request):
    inventorybooks = Book.objects.all() 
    return render(request , 'pages/Books.html' , {'allbooks' : inventorybooks})
