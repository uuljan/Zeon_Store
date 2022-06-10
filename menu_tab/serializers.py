from rest_framework import serializers
from .models import *

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

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = ImageQuestionSerializer(instance.image.all(), many=True).data
        representation['reply'] = ReplySerializer(instance.replies.all(), many=True).data
        return representation

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('reply', )

class ImageQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageQuestion
        fields = ('image', )

class FooterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Footer
        fields = '__all__'

