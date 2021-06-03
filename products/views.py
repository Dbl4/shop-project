import os
import json

from django.shortcuts import render

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.


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
        'footer_title': 'GeekShop'
    }
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context['products'] = json.load(open(file_path, encoding = 'utf-8'))
    return render(request, 'products/products.html', context)
