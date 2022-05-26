from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Bestseller
from .serializers import BestsellerSerializer

# class Slider(ModelViewSet):

class PaginationBestseller(PageNumberPagination):
    page_size = 8
    max_page_size = 1000

class BestsellerView(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BestsellerSerializer
    queryset = Bestseller.objects.all()
    pagination_class = PaginationBestseller

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)