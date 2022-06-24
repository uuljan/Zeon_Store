from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from main.views import MyPagination, Pagination12
from .models import Collection, Favorite, Product
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import ProductSerializer, \
    FavoriteSerializer, CollectionSerializer


class ProductViewSet(ModelViewSet):
    """View продукта"""

    queryset = Collection.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['collection']

    def list(self, request):
        '''Другие товары этой коллекции'''
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True,
                                       context={'request': request})
        if not queryset:
            try:
                queryset = Collection.objects.order_by('?')[:5]
                serializer = CollectionSerializer(queryset, many=True,
                                                  context={'request': request})
            except IndexError:
                return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        """Функция поиска товара"""

        q = request.query_params.get('q')
        queryset = self.queryset.filter(name__icontains=q)
        if not queryset.count():
            try:
                queryset = Product.objects.order_by('?')[:5]
            except IndexError:
                return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CollectionSerializer(queryset, many=True,
                                          context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CollectionView(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     GenericViewSet):
    '''View коллекции'''

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = MyPagination


class FavoriteView(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    '''View избранных'''


    serializer_class = FavoriteSerializer
    pagination_class = Pagination12

    def list(self, request):
        queryset = Favorite.objects.all()
        serializer = FavoriteSerializer(queryset, many=True,
                                        context={'request': request})
        if not queryset:
            try:
                queryset = Collection.objects.order_by('?')[:5]
                serializer = CollectionSerializer(queryset, many=True,
                                               context={'request': request})
            except IndexError:
                return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)
