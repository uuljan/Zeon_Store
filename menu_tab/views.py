from rest_framework.viewsets import ModelViewSet

from main.views import MyPagination
from .serializers import *


class OfferView(ModelViewSet):
    """test"""
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)


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


class NewsView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = MyPagination
    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)


class QuestionView(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)


class FooterView(ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer


    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

