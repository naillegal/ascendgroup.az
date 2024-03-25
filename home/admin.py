from django.utils.html import format_html
from django.contrib import admin
from .models import Slider, SlideContent, VideoSlider, Statistic
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
class SlideContentInline(TranslationTabularInline):
    model = SlideContent
    extra = 1
    readonly_fields = ['image_preview']
    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.image.url)
        else:
            return None

    image_preview.short_description = 'Image Preview'

class SliderAdmin(TranslationAdmin):
    inlines = [SlideContentInline]

admin.site.register(Slider, SliderAdmin)
admin.site.register(VideoSlider)
admin.site.register(Statistic)

