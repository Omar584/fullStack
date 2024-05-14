from django.shortcuts import render
from book.models import Book

def userPage(request):
    return render(request , 'pages/user/userPage.html')

def userBooks(request):
    inventoryBooks = Book.objects.all()
    return render(request , 'pages/user/bookList.html' , {'books' : inventoryBooks})

def about(request):
    return render(request , 'pages/user/about.html')

def contact(request):
    return render(request , 'pages/user/contact.html')

def profile(request):
    return render(request , 'pages/user/profile.html')

def changePassword(request):
    return render(request , 'pages/user/contact.html')

def borrowedbooks(request):
    return render(request , 'pages/user/borrowedBooks.html')
