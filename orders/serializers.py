from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор заказа"""
    class Meta:
        model = Order
        fields = ('user', 'first_name', 'last_name', 'email',
                  'number', 'country', 'city', 'order_status',
                  'created')


class OrderItemSerializer(serializers.ModelSerializer):
    """Сериализатор детали заказа"""

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderInfoSerializer(serializers.ModelSerializer):
    """Сериализатор детали товаров заказа"""

    class Meta:
        model = OrderInfo
        fields = '__all__'
