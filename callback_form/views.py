from rest_framework.viewsets import ModelViewSet

from callback_form.models import MyCallback
from callback_form.serializers import MyCallbackSerializer


class MyCallbackView(ModelViewSet):
    """View Обратный звонок"""

    queryset = MyCallback.objects.all()
    serializer_class = MyCallbackSerializer
