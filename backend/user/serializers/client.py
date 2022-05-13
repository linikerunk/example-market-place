from rest_framework import serializers
from user.models.client import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'client', 'seller', 'operation_date')