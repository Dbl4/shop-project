from django.shortcuts import render

from products.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    context = {
        'title': 'GeekShop',
        'h1': 'GeekShop Store',
        'p': 'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {
        'h1': 'GeekShop',
        'footer_title': 'GeekShop',
        'categories': ProductCategory.objects.all()
    }
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)
