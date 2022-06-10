from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from main.views import MyPagination
from .models import Collection, Favorite
from product.models import Product
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, FavoriteSerializer
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
        queryset = self.queryset.filter(name__icontains=q)
        if not queryset.count():
            try:
                queryset = Product.objects.order_by('?')[:5]
            except IndexError:
                return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
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

    def list(self, request):
        queryset = self.queryset
        serializer = FavoriteSerializer(queryset, many=True, context={'request': request})
        if not queryset:
            try:
                queryset = Product.objects.order_by('?')[:5]
                serializer = ProductSerializer(queryset, many=True, context={'request': request})
            except IndexError:
                return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)