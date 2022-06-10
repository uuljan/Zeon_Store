from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    # raw_id_fields = ['cart']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'number', 'country', 'city', 'order_status',
                    'created']
    list_filter = ['order_status', 'created']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'cart',
                    'line', 'product_quantity', 'cost', 'discount', 'total_cost']


admin.site.register(OrderItem, OrderItemAdmin)
