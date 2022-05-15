from rest_framework import serializers
from marketplace.models.sale_product_activity import SaleProductActivity
from marketplace.serializers.sale import SaleSerializer
from marketplace.serializers.product_activity import ProductActivitySerializer


class SaleProductActivitySerializer(serializers.ModelSerializer):
    sale = SaleSerializer(required=True)
    product_activity = ProductActivitySerializer(required=True)
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = SaleProductActivity
        fields = ('id', 'sale', 'product_activity', 'quantity')
