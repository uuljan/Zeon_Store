from rest_framework import serializers
from .models import *


class ImageProductSerializer(serializers.ModelSerializer):
    """Сериализатор цвет и фото цвета"""

    class Meta:
        model = ImageProduct
        fields = ('image', 'color')


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор Продукта"""

    color_image = ImageProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('collection', 'name', 'vendor', 'price',
                  'price_with_discount', 'discount', 'description',
                  'size_range', 'structure', 'line', 'fabric', 'color_image')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['favorite'] = FavoriteSerializer(instance.product.all(),
                                                        many=True).data
        representation['color_image'] = ImageProductSerializer(
                                        instance.image_color.all(),
                                        many=True).data

        return representation


class CollectionSerializer(serializers.ModelSerializer):
    """Сериализатор Коллекции"""

    class Meta:
        model = Collection
        fields = ('name',)


class FavoriteSerializer(serializers.ModelSerializer):
    """Сериализатор Избранное"""

    class Meta:
        model = Favorite
        fields = ['favorite', 'quantity', 'product']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['quantity'] = len(Favorite.objects.all())
        representation['product'] = ProductSerializer().data
        representation['author'] = instance.user.email
        return representation
