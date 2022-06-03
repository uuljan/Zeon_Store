from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from main.views import MyPagination
from .models import Collection
from product.models import Product
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
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

