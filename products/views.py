from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from products.models import Product, ProductCategory


class IndexTemplateView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop'
        context['h1'] = 'GeekShop Store'
        context['p'] = 'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
        return context


class ProductsListView(ListView):
    paginate_by = 3
    model = Product
    template_name = 'products/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['h1'] = 'GeekShop'
        context['footer_title'] = 'GeekShop'
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset