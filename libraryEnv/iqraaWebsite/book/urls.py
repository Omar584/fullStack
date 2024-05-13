from django.urls import path
from . import views


urlpatterns = [
    # path('book' , views.book , name = 'book') ,
    path('' , views.books , name = 'books'),
]