from rest_framework.viewsets import ModelViewSet

from .models import About
from .serializers import AboutSerializer


class AboutView(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)
