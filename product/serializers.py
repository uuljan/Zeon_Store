from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):

        # instance = "title": "Edited", "price": 199.99 ...
        representation = super().to_representation(instance)
        representation['collection'] = instance.collection.name
        return representation