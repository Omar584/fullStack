from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminHome , name = 'adminHome'),
    path('adminbooks/',views.adminbooks , name = 'adminbooks') ,
    path('adminprofile',views.adminprofile , name = 'adminprofile')

]
