from .forms import ContactForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contact') + '?success=true')
        else:
            return HttpResponseRedirect(reverse('contact') + '?success=false')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

