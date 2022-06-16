from rest_framework import serializers
from .models import MyCallback

class MyCallbackSerializer(serializers.ModelSerializer):
    """Сериализатор Обратный звонок"""

    class Meta:
        model = MyCallback
        fields = '__all__'

