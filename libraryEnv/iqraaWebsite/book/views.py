from django.shortcuts import render
from .models import Book




def books(request):
    allbooks = {'products' : Book.objects.all()}
    return render(request , 'pages/main/bookList.html' , allbooks)
