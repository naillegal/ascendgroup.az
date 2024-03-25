from .models import SlideContent, Slider
from modeltranslation.translator import TranslationOptions, register

@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title',)  


@register(SlideContent)
class SlideContentTranslationOptions(TranslationOptions):
    fields = ('title',)  
