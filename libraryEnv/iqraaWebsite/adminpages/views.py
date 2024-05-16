from django.shortcuts import render , get_object_or_404
from book.models import Book

def adminHome(request):
    return render(request , 'pages/admin/adminPage.html')

def adminBooks(request):
    if 'search' in request.GET:
        query = request.GET['search']
        inventoryBooks = Book.objects.filter(name__icontains=query)
    else:
        inventoryBooks = Book.objects.all() 

    return render(request , 'pages/admin/bookList.html', {'allbooks':inventoryBooks})

def adminProfile(request):
    return render(request , 'pages/admin/profile.html')

def addBookPage(request):
    return render(request,'pages/admin/addBook.html')

def deleteBookPage(request):
    return render(request, 'pages/admin/deleteBook.html')

def editBookPage(request):
    return render(request , 'pages/admin/editBook.html')

def adminChangePassword(request):
    return render(request , 'pages/admin/changePassword.html')

def adminBookDetails(request , book_id):
    book = get_object_or_404(Book , id = book_id)
    return render(request , 'pages/admin/bookDetails.html' , {'book' : book})



