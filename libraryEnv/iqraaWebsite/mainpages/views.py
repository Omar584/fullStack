from django.shortcuts import render


def index(request):
    return render(request,'pages/main/index.html')

def contact(request):
    return render(request,'pages/main/contact.html')

def about(request):
    return render(request,'pages/main/about.html')

def signup(request):
    return render(request,'pages/main/signup.html')


