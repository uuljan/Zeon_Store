from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import *


class CartView(ModelViewSet):
    """View детали корзины"""

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)


class CartInfoView(ModelViewSet):
    """View детали товаров корзины"""

    permission_classes = [IsAuthenticated, ]

    queryset = CartInfo.objects.all()
    serializer_class = CartInfoSerializer

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)
