from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.fullname
    
class Certificate(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.title

