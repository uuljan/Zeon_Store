from .models import Cart
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    """tetyxt"""
    class Meta:
        model = Cart
        fields = '__all__'
