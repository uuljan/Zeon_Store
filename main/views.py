
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from product.models import Product
from .serializers import *


# Добавила свою пагинацию для "Хиты продаж и Новинки"
class MyPagination(PageNumberPagination):
    page_size = 8
    max_page_size = 1000

class BestsellerView(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BestsellerSerializer
    queryset = Bestseller.objects.all()
    pagination_class = MyPagination

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

class SliderView(ModelViewSet):
    serializer_class = SliderSerializer
    queryset = Slider.objects.all()
    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

class NoveltyView(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = NoveltySerializer
    queryset = Novelty.objects.all()
    pagination_class = MyPagination

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

class CollectionView(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    pagination_class = MyPagination


    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)



class AdvantageView(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = AdvantageSerializer
    queryset = Advantage.objects.all()

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

