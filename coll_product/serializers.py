from .models import Coll_product
from rest_framework import serializers


class Coll_productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coll_product
        fields = '__all__'

