from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from .serializers import *


class MyPagination(PageNumberPagination):
    """Кастомный класс для пагинации в 8 страниц"""

    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 1000


class Pagination12(PageNumberPagination):
    """Кастомный класс для пагинации в 12 страниц"""

    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000


class SliderView(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 GenericViewSet):
    """View Слайдера"""

    serializer_class = SliderSerializer
    queryset = Slider.objects.all()


class AdvantageView(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    GenericViewSet):
    """View Наши преимущества"""

    serializer_class = AdvantageSerializer
    queryset = Advantage.objects.all()


class BestsellerView(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):
    """View Хиты продаж"""

    serializer_class = BestsellerSerializer
    queryset = Bestseller.objects.all()
    pagination_class = MyPagination


class NoveltyView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    """View Новинки"""

    serializer_class = NoveltySerializer
    queryset = Novelty.objects.all()
    pagination_class = MyPagination
