from rest_framework import serializers

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

    class Meta:
        model = Bestseller
        fields = '__all__'


class NoveltySerializer(serializers.ModelSerializer):
    """Сериализатор Новинки"""

    class Meta:
        model = Novelty
        fields = '__all__'



