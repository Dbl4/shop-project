from django.shortcuts import render


# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
        'h1': 'GeekShop Store',
        'p': 'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
    }
    return render(request, 'products/index.html', context)


def products(request):
    return render(request, 'products/products.html')
