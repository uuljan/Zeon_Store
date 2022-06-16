from django.contrib import admin

from cart.models import Cart, CartItem, CartInfo


class CartItemInline(admin.TabularInline):
    model = CartItem


@admin.register(Cart)
class OrderAdmin(admin.ModelAdmin):
    # pass
    inlines = [CartItemInline]

@admin.register(CartInfo)
class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['cart', 'lines', 'product_quantity', 'cost', 'discount', 'total_cost']

