from django.shortcuts import render

def adminHome(request):
    return render(request , 'pages/admin/adminPage.html')

def adminbooks(request):
    return render(request , 'pages/admin/bookList.html')

def adminprofile(request):
    return render(request , 'pages/admin/profile.html')



