from rest_framework import serializers
from .models import *


class OfferSerializer(serializers.ModelSerializer):
    """Сериализатор Публичная оферта"""

    class Meta:
        model = Offer
        fields = ('title', 'description')


class Image_aboutSerializer(serializers.ModelSerializer):
    """Сериализатор О нас для картинок"""

    class Meta:
        model = Image_about
        fields = ("image",)


class AboutSerializer(serializers.ModelSerializer):
    """Сериализатор О нас"""

    class Meta:
        model = About
        fields = ('title', "description")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = Image_aboutSerializer(instance.images.all(),
                                                         many=True).data
        return representation


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор Новости"""

    class Meta:
        model = News
        fields = ('image', 'title', 'description')


class ImageQuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для Вопрос/Ответ"""

    class Meta:
        model = ImageQuestion
        fields = ('image',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['help'] = QuestionSerializer(instance.questions.all(),
                                                    many=True).data
        return representation


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для Вопрос/Ответ"""

    class Meta:
        model = Question
        fields = ('question', 'reply')


class FooterOneSerializer(serializers.ModelSerializer):
    """Сериализатор для Футер1"""

    class Meta:
        model = Footer1
        fields = ('header_logo', 'footer_logo', 'text', 'header_contact')


class FooterTwoSerializer(serializers.ModelSerializer):
    """Сериализатор для Футер2"""

    class Meta:
        model = Footer2
        fields = ('contact_number', 'mail', 'instagram',
                  'telegram', 'whatsapp')
