from django.shortcuts import render , get_object_or_404,redirect
from book.models import Book
from userData.models import User

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
    user = request.session.get('username')
    if user is not None:
        ud = User.objects.get(pk=user)
        if request.method == 'POST':
            address = request.POST.get('Address')
            phone = request.POST.get('phone')
            if 'addimage' in request.FILES:
                image = request.FILES['addimage']
                ud.userImage = image
            if address is not None:
                ud.address = address
            if phone is not None:
                ud.phoneNumber = phone
            if image is not None:
                ud.userImage = image
            ud.save()
        return render(request , 'pages/user/profile.html',{'data':ud})
    else:
        return redirect('index')

def userChangePassword(request):
    return render(request , 'pages/user/changePassword.html')

def borrowedbooks(request):
    return render(request , 'pages/user/borrowedBooks.html')

def userBookDetails(request , book_id):
    book = get_object_or_404(Book , id = book_id)
    return render(request , 'pages/user/bookDetails.html' , {'book' : book})
