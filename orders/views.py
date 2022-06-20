from rest_framework.viewsets import ModelViewSet

from .serializers import *


class OrderView(ModelViewSet):
    """View заказа"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)


class OrderItemView(ModelViewSet):
    """View детали заказа"""

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)


class OrderInfoView(ModelViewSet):
    """View детали товаров заказа"""

    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializer

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)
