from rest_framework import serializers

from product.serializers import ProductSerializer
from .models import *


class SliderSerializer(serializers.ModelSerializer):
    """Сериализатор Слайдера"""

    class Meta:
        model = Slider
        fields = ('img', 'main_url')


class AdvantageSerializer(serializers.ModelSerializer):
    """Сериализатор Наши преимущества"""

    class Meta:
        model = Advantage
        fields = ('image', 'title_advantage', 'description_advantage')


class BestsellerSerializer(serializers.ModelSerializer):
    """Сериализатор Хиты продаж"""
    obj = ProductSerializer()

    class Meta:
        model = Bestseller
        fields = ('obj', 'bestseller')


class NoveltySerializer(serializers.ModelSerializer):
    """Сериализатор Новинки"""
    item1 = ProductSerializer()

    class Meta:
        model = Novelty
        fields = ('item1', 'novelty')
