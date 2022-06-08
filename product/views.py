import json

from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from main.views import MyPagination
from .models import Collection, Favorite, RandomProduct
from product.models import Product
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, FavoriteSerializer, RandomProductSerializer
from .serializers import CollectionSerializer

class MyProductPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 1000

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['collection']
    pagination_class = MyProductPagination

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        q = request.query_params.get('q')
        queryset = self.queryset
        queryset = queryset.filter(Q(name__icontains=q) |
                                   Q(description__icontains=q))
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        seria = Product.objects.order_by('?').first()

        if not queryset:
            return Response(json.dumps(seria), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_context(self):
        return {
            'request': self.request
        }
    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)


class CollectionView(ModelViewSet):
    queryset = Collection.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CollectionSerializer
    pagination_class = MyPagination


    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

class FavoriteView(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    pagination_class = MyPagination

from django.db.models.aggregates import Count
from random import randint

class RandomProductView(ModelViewSet):
    queryset = RandomProduct.objects.all()
    serializer_class = RandomProductSerializer

    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)