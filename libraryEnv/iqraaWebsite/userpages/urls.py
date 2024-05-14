from django.urls import path
from . import views


urlpatterns = [
    path('' , views.userPage , name = 'userPage'),
    path('bookList/' , views.userBooks , name = 'userBooks'),
    path('borrowedBooks/' , views.borrowedbooks , name = 'borrowedBooks'),
    path('changePassword/' , views.changePassword , name = 'changePassword'),
    path('profile/' , views.profile , name = 'profile'),
    path('contact' , views.contact , name = 'contact'),
]