from rest_framework import serializers
from .models import *

class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = '__all__'

class BestsellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bestseller
        fields = '__all__'

class NoveltieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Noveltie
        fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advantage
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'


