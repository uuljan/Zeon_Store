from django.contrib import admin
from .models import Order, OrderItem, OrderInfo


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email',
                    'number', 'country', 'city', 'order_status',
                    'created']
    list_filter = ['order_status', 'created']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'order_cost',
                    'total_cost']


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['order', 'lines', 'product_quantity', 'cost',
                    'discount', 'total_cost']
