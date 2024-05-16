from django.db import models
from book.models import Book


class User(models.Model):
    username = models.CharField(primary_key = True,max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    isAdmin = models.BooleanField(default = False)
    userImage = models.ImageField(upload_to = 'userphotos/%y%m%d',default = 'userphotos/240515/profile1.jpg')
    address = models.CharField(max_length = 50)
    phoneNumber = models.CharField(max_length = 11)
    books = models.ManyToManyField(Book,null = True)
    def __str__(self):
        return self.username
    

