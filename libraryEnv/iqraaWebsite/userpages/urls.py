from django.urls import path
from . import views

urlpatterns=[
    path('',views.userPage,name='userPage'),
    path('books/',views.userBooks , name = 'books'),
    path('contact/' , views.userContact , name = 'contact') ,
    path('about/' , views.userAbout , name = 'about') ,
    path('profile/' , views.userProfile , name = 'profile') ,
    path('changePassword/' , views.userChangePassword , name = 'changePassword')
]

