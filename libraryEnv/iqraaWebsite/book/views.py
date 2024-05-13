from django.shortcuts import render
from .models import Book




def books(request):
    books = Book.objects.all() 
    return render(request , 'pages/main/bookList.html' , {'books' : books})
