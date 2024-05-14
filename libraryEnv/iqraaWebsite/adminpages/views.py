from django.shortcuts import render

def adminHome(request):
    return render(request , 'pages/admin/adminPage.html')

def adminBooks(request):
    return render(request , 'pages/admin/bookList.html')

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



