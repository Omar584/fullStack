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
            if 'image' in request.FILES:
                image = request.FILES['image']
                ud.userImage = image
            if address is not None:
                ud.address = address
            if phone is not None:
                ud.phoneNumber = phone
            ud.save()
        return render(request , 'pages/user/profile.html',{'data':ud})
    else:
        return redirect('index')



def userChangePassword(request):
    return render(request , 'pages/user/changePassword.html')




def borrowedbooks(request):

    username = request.session.get('username')
    if username:
        user = get_object_or_404(User,pk = username)
        books = user.books.all()
        print("Books associated with user:", books)  
        return render(request , 'pages/user/borrowedBooks.html',{'books':books})
    else:
        return redirect('index')



def userBookDetails(request , book_id):
    book = get_object_or_404(Book , id = book_id)
    user = request.session.get('username')
    if user:
        if request.method == 'POST':
            userID = request.POST.get('id')
            userDetails = User.objects.get(pk=user)
            userDetails.books.add(book)
            
    return render(request , 'pages/user/bookDetails.html' , {'book' : book})
