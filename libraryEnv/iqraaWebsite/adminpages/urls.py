from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminHome , name = 'adminHome'),
    path('adminbooks/',views.adminBooks , name = 'adminBooks') ,
    path('adminprofile/',views.adminProfile , name = 'adminProfile') ,
    path('addbook/' ,views.addBookPage , name ='addBookPage') ,
    path('deletebook/' , views.deleteBookPage , name = 'deleteBookPage'),
    path('editbook/',views.editBookPage , name = 'editBookPage' ) ,
    path('changepassword/' , views.adminChangePassword , name = 'adminChangePassword') ,
    path('bookDetils/<int:book_id>/' , views.adminBookDetails , name = 'adminBookDetails')
]
