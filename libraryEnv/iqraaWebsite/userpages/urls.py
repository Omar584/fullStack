from django.urls import path
from . import views


urlpatterns = [
    path('' , views.userPage , name = 'userPage'),
    path('bookList/' , views.userBooks , name = 'userBooks'),
    path('borrowedBooks/' , views.borrowedbooks , name = 'borrowedBooks'),
    path('changePassword/' , views.userChangePassword , name = 'userChangePassword'),
    path('profile/' , views.userProfile , name = 'userProfile'),
    path('contact' , views.userContact , name = 'userContact'),
]