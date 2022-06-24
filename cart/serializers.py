from rest_framework import serializers

from product.serializers import ProductSerializer
from .models import *


class CartSerializer(serializers.ModelSerializer):
    """Сериализатор детали корзины"""

    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = ('user', 'product', 'quantity', 'cart_cost', 'total_cart_cost')


class CartInfoSerializer(serializers.ModelSerializer):
    """Сериализатор детали товаров корзины"""

    class Meta:
        model = CartInfo
        fields = ('cart', 'lines', 'product_quantity', 'cost', 'discount', 'total_cost')
