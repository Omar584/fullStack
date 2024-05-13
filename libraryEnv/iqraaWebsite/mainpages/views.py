from django.shortcuts import render

def index(request):
    return render(request,'pages/main/index.html')
