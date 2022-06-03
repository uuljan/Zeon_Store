from rest_framework import serializers
from .models import *

class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = '__all__'

class BestsellerSerializer(serializers.ModelSerializer):
    collection = serializers.ReadOnlyField()
    class Meta:
        model = Bestseller
        fields = '__all__'



class NoveltySerializer(serializers.ModelSerializer):

    class Meta:
        model = Novelty
        fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advantage
        fields = '__all__'





