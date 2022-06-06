from rest_framework import serializers

from product.serializers import ProductSerializer
from .models import *

class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = '__all__'

class ProductRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRelation
        fields = ('product', 'favorite')
class BestsellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bestseller
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['name'] = BestsellerSerializer(instance.best.all(), many=True).data
    #
    #     return representation



class NoveltySerializer(serializers.ModelSerializer):

    class Meta:
        model = Novelty
        fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advantage
        fields = '__all__'





