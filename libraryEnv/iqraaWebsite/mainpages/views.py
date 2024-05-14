from django.shortcuts import render
from book.models import Book

def index(request):
    return render(request,'pages/main/index.html')

def books(request):
    inventorybooks = Book.objects.all()
    return render(request , 'pages/main/bookList.html' , {'allbooks' : inventorybooks})

def contact(request):
    return render(request,'pages/main/contact.html')

def about(request):
    return render(request,'pages/main/about.html')

def signup(request):
    return render(request,'pages/main/signup.html')


