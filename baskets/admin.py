from django.contrib import admin

from baskets.models import Basket

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'product',
        'quantity',
        'created_timestamp',
    ]


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('user','product','quantity','created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0