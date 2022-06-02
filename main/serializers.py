from rest_framework import serializers
from .models import *

class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = '__all__'

class BestsellerSerializer(serializers.ModelSerializer):
    collection = serializers.ReadOnlyField(source='author.name')
    class Meta:
        model = Bestseller
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['image'] = instance.title


class NoveltySerializer(serializers.ModelSerializer):

    class Meta:
        model = Novelty
        fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advantage
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'

    def create(self, validated_data):
        collection = Collection.objects.create(**validated_data)
        return collection


