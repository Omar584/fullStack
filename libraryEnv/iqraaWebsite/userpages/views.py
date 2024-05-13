from django.shortcuts import render


def userPage(request):
    return render(request,'pages/user/userPage.html')

def userBooks(request):
    return render(request,'pages/user/bookList.html')

def userContact(request):
    return render(request,'pages/user/contact.html')

def userAbout(request):
    return render(request,'pages/user/about.html')

def userProfile(request):
    return render(request,'pages/user/profile.html')

def borrowedBooks(request):
    return render(request,'pages/user/borrowedBooks.html')

def userChangePassword(request):
    return render(request,'pages/user/changePassword.html')
