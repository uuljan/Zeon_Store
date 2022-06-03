from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from main.models import Collection
from product.models import Product
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        return {
            'request': self.request
        }
    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)