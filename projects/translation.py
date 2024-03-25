from .models import Project
from modeltranslation.translator import TranslationOptions, register


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
