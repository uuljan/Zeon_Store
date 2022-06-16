from rest_framework.viewsets import ModelViewSet

from callback_form.models import MyCallback
from callback_form.serializers import MyCallbackSerializer


class MyCallbackView(ModelViewSet):
    """View Обратный звонок"""
    queryset = MyCallback.objects.all()
    serializer_class = MyCallbackSerializer

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)
