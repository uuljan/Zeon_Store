from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import *


class CartView(ModelViewSet):
    """View детали корзины"""

    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartInfoView(ModelViewSet):
    """View детали товаров корзины"""

    permission_classes = [IsAuthenticated, ]

    queryset = CartInfo.objects.all()
    serializer_class = CartInfoSerializer
