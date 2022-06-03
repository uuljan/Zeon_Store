from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ('bestseller', 'novelty', )

    def to_representation(self, instance):

        # instance = "title": "Edited", "price": 199.99 ...
        representation = super().to_representation(instance)
        representation['collection'] = instance.collection.name
        return representation


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection

        fields = '__all__'

    def create(self, validated_data):
        collection = Collection.objects.create(**validated_data)
        return collection
