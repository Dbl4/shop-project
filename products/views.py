from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title':
        'GeekShop',
        'h1':
        'GeekShop Store',
        'p':
        'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'h1':
        'GeekShop',
        'products': [{
            "name": "Худи черного цвета с монограммами adidas Originals",
            "price": "6 090,00",
            "description":
            "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни",
            "path": "vendor/img/products/Adidas-hoodie.png"
        }, {
            "name":
            "Синяя куртка The North Face",
            "price":
            "23 725,00",
            "description":
            "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
            "path":
            "vendor/img/products/Blue-jacket-The-North-Face.png"
        }, {
            "name":
            "Коричневый спортивный oversized-топ ASOS DESIGN",
            "price":
            "3 390,00",
            "description":
            "Материал с плюшевой текстурой. Удобный и мягкий.",
            "path":
            "vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png"
        }, {
            "name":
            "Черный рюкзак Nike Heritage",
            "price":
            "2 340,00",
            "description":
            "Плотная ткань. Легкий материал.",
            "path":
            "vendor/img/products/Black-Nike-Heritage-backpack.png"
        }, {
            "name":
            "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
            "price": "13 590,00",
            "description": "Гладкий кожаный верх. Натуральный материал.",
            "path": "vendor/img/products/Black-Dr-Martens-shoes.png"
        }, {
            "name":
            "Темно-синие широкие строгие брюки ASOS DESIGN",
            "price":
            "2 890,00",
            "description":
            "Легкая эластичная ткань сирсакер Фактурная ткань.",
            "path":
            "vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png"
        }],
        'footer_title':
        'GeekShop'
    }
    return render(request, 'products/products.html', context)
