from django.shortcuts import render
from .models import Book


def books(request):
    inventorybooks = Book.objects.all() 
    return render(request , 'pages/main/bookList.html' , {'allbooks' : inventorybooks})
