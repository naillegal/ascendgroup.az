from django.db import models
from django.urls import reverse
from shared.urlutils import get_slug

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = get_slug(self.name)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("project:project-detail", kwargs={"pk": self.pk, 'slug': self.slug})


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/')
