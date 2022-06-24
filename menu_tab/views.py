from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from main.views import MyPagination
from .serializers import *


class OfferView(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                GenericViewSet):
    """View для Публичная оферта"""

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class AboutView(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                GenericViewSet):
    """View для О нас"""

    queryset = About.objects.all()
    serializer_class = AboutSerializer


class NewsView(ModelViewSet):
    """ View Новости"""

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = MyPagination


class ImageQuestionView(ModelViewSet):
    """View для Помощь"""

    queryset = ImageQuestion.objects.all()
    serializer_class = ImageQuestionSerializer
    query = Question.objects.all()


class FooterOneView(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    GenericViewSet):
    """View для Футера"""

    queryset = Footer1.objects.all()
    serializer_class = FooterOneSerializer


class FooterTwoView(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    GenericViewSet):
    """View для Футера"""

    queryset = Footer2.objects.all()
    serializer_class = FooterOneSerializer
