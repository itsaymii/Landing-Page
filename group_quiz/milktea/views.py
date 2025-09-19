from django.shortcuts import render
from .models import Product

def landing_page(request):
    products = Product.objects.all()[:5]
    return render(request, 'home.html', {'products': products})
