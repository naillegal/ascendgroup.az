from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Employee,Certificate


def about(request):
    try:
        employees = Employee.objects.all()
    except ObjectDoesNotExist:
        employees = []
    try:
        certificates = Certificate.objects.all()
    except ObjectDoesNotExist:
        certificates = []

    return render(request, 'about.html', {'employees': employees, 'certificates': certificates})
