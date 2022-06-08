from rest_framework import serializers
from .models import MyCallback

class MyCallbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyCallback
        fields = '__all__'

