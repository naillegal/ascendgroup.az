from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=30)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    viewed = models.BooleanField(default=False, verbose_name='Baxdım')
    created = models.DateField(
        auto_now_add=True, verbose_name='Göndərilmə Tarixi')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.subject
