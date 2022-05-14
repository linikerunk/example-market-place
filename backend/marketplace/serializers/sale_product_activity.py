from rest_framework import serializers
from marketplace.models.product_activity import ProductActivity
from marketplace.models.sale import Sale
from marketplace.models.sale_product_activity import SaleProductActivity


class SaleProductActivitySerializer(serializers.ModelSerializer):
    sale = serializers.PrimaryKeyRelatedField(
        queryset=Sale.objects.all(),
        required=False
    )
    product_activity = serializers.PrimaryKeyRelatedField(
        queryset=ProductActivity.objects.all(),
        required=False
    )
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = SaleProductActivity
        fields = ('id', 'sale', 'product_activity', 'quantity')
