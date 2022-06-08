from django.contrib import admin

from cart.models import Cart


@admin.register(Cart)
class Cart(admin.ModelAdmin):
    pass