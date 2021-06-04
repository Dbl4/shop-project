from django.shortcuts import render
from static.products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop',
        'h1': 'GeekShop Store',
        'p': 'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'h1': 'GeekShop',
        'footer_title': 'GeekShop',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
