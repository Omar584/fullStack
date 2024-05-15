from django.shortcuts import render
from book.models import Book

def userPage(request):
    return render(request , 'pages/user/userPage.html')

def userBooks(request):
    if 'search' in request.GET:
        query = request.GET['search']
        inventoryBooks = Book.objects.filter(name__icontains=query)
    else:
        inventoryBooks = Book.objects.all() 
        
    return render(request , 'pages/user/bookList.html' , {'books' : inventoryBooks})

def userAbout(request):
    return render(request , 'pages/user/about.html')

def userContact(request):
    return render(request , 'pages/user/contact.html')

def userProfile(request):
    return render(request , 'pages/user/profile.html')

def userChangePassword(request):
    return render(request , 'pages/user/changePassword.html')

def borrowedbooks(request):
    return render(request , 'pages/user/borrowedBooks.html')
