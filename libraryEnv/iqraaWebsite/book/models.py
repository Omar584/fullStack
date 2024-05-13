from django.db import models


class Book(models.Model):
    name = models.CharField(max_length = 50)
    id = models.IntegerField(primary_key = True)
    category = models.CharField(max_length = 30)
    price = models.DecimalField(max_digits = 5 , decimal_places = 2)
    description = models.TextField()
    image = models.ImageField(upload_to = 'photos/%y/%m/%d' )
    active = models.BooleanField(default = True)

