from django.db import models

# Create your models here.


class Laminate(models.Model):
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name
