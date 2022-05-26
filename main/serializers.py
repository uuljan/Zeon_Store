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