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
    product = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Favorite
        fields = ['favorite', 'product', 'quantity']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['quantity'] = len(Favorite.objects.all())

        return representation

