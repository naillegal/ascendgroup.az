from django import forms
from .models import Contact
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': _('Ad')}))
    number = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': _('Nömrəniz')}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': _('Mövzu')}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Text...'}))

    class Meta:
        model = Contact
        fields = ['name', 'number', 'subject', 'message']

