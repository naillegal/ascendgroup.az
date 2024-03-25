from .models import Employee
from modeltranslation.translator import TranslationOptions,register

@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('job',)