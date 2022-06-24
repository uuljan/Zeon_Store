from django.contrib import admin

from cart.models import Cart, CartInfo


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity',
                    'cart_cost', 'total_cart_cost']


@admin.register(CartInfo)
class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['cart', 'lines', 'product_quantity',
                    'cost', 'discount', 'total_cost']
