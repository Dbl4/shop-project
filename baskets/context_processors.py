from baskets.models import Basket


def baskets(request):
    print('ПРИВЕТ из контекстного процессора')
    baskets = []

    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user)

    return {
        'baskets': baskets,
    }