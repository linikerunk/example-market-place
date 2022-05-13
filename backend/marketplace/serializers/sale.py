from rest_framework import serializers
from marketplace.models.sale import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'client', 'seller', 'operation_date')
