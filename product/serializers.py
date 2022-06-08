from rest_framework import serializers
from .models import *
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['collection'] = instance.collection.name
        representation['favorite'] = FavoriteSerializer(instance.product.all(), many=True).data

        return representation

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection

        fields = '__all__'

    def create(self, validated_data):
        collection = Collection.objects.create(**validated_data)
        return collection

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('product', 'favorite', )

class RandomProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomProduct
        fields = ('product', 'favorite', )

