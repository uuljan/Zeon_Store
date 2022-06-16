from rest_framework import serializers

from product.serializers import ProductSerializer
from .models import *


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'



class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ('cart', 'product', 'quantity')




class CartInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartInfo
        fields = '__all__'
