from django.shortcuts import render


def userPage(request):
    return render(request,'pages/user/userPage.html' , name = 'userPage'),
