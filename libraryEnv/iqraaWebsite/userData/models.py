from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(primary_key = True,max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    isAdmin = models.BooleanField(default = False)
    userImage = models.ImageField('userphotos/%y%m%d')
    address = models.CharField(max_length = 50)
    phoneNumber = models.CharField(max_length = 11)