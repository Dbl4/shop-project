from django.urls import path

from static.products.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name = 'index')
]