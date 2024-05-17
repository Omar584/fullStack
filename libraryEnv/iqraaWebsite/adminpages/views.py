from django.shortcuts import render , get_object_or_404
from book.models import Book
from userData.models import User

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
    uuser = request.session.get('username')
    if user is not None:
        ud = User.objects.get(pk=user)
        if request.method == 'POST':
            address = request.POST.get('Address')
            phone = request.POST.get('phone')
            ud.address = address
            ud.phoneNumber = phone
            ud.save()
        return render(request , 'pages/admin/profile.html',{'data':ud})
    else:
        return redirect('index')

    

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



