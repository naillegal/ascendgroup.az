from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'number', 'subject', 'message', 'created']
    list_display = ['name', 'number', 'viewed', 'created']