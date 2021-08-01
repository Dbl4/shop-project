from django.contrib import admin

from users.models import User, ShopUserProfile
from baskets.admin import BasketAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdmin,)


admin.site.register(ShopUserProfile)
