from django.db import models


class Book(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50 , default= 'unknown')
    category = models.CharField(max_length = 30)
    price = models.DecimalField(max_digits = 5 , decimal_places = 2)
    description = models.TextField()
    image = models.ImageField(upload_to = 'photos/%y/%m/%d' )
    active = models.BooleanField(default = True)

