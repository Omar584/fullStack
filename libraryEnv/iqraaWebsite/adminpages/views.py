from django.shortcuts import render


def adminPage(request):
    return render(request,'pages/admin/adminPage.html'),

