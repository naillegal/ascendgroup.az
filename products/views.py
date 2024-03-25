from django.shortcuts import render
from .models import Laminate, Product
from django.core.exceptions import ObjectDoesNotExist


def products(request):
    try:
        laminates = Laminate.objects.all()
    except ObjectDoesNotExist:
        laminates = []

    try:
        our_products = Product.objects.all()
    except ObjectDoesNotExist:
        our_products = []

    return render(request, 'products.html', {'laminates': laminates, 'our_products': our_products})
