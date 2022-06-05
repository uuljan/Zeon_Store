from rest_framework import serializers
from .models import Offer, About, Image_about

class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = '__all__'




class Image_aboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image_about
        fields = '__all__'

    def create(self, validated_data):
        image_about = Image_about.objects.create(**validated_data)
        return image_about

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        exclude = ('id', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = Image_aboutSerializer(instance.images.all(), many=True).data
        return representation

