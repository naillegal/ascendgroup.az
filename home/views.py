from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import Slider, VideoSlider, Statistic

def home(request):
    try:
        slider1 = Slider.objects.get(title='first_slider')
        slide_contents1 = slider1.slide_contents.all()
    except ObjectDoesNotExist:
        slider1 = None
        slide_contents1 = []

    try:
        slider2 = Slider.objects.get(title='partners_slider')
        slide_contents2 = slider2.slide_contents.all()
    except ObjectDoesNotExist:
        slider2 = None
        slide_contents2 = []

    try:
        videos = VideoSlider.objects.all()
    except ObjectDoesNotExist:
        videos = None

    try:
        statistics = Statistic.objects.all()
    except ObjectDoesNotExist:
        statistics = None

    return render(request, 'home.html', {'slider1': slider1, 'slide_contents1': slide_contents1, 'slider2': slider2, 'slide_contents2': slide_contents2, 'videos': videos, 'statistics': statistics})
