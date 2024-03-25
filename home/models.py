from django.db import models

# Create your models here.

class Slider(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class SlideContent(models.Model):
    slider = models.ForeignKey(Slider, related_name='slide_contents', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')

class VideoSlider(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='media/videos/')

    def __str__(self):
        return self.title

class Statistic(models.Model):
    members = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    projects = models.IntegerField(default=0)

