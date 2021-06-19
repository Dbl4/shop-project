from django.contrib import admin

from static.products.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity', 'category'), 'image')
    readonly_fields = ('description',)
    ordering = ('-price',)
    search_fields = ('name',)
