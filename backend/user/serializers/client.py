from rest_framework import serializers
from models.client import Client


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'client', 'seller', 'operation_date')