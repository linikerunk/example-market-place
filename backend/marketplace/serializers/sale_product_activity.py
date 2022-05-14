from rest_framework import serializers
from marketplace.models.product_activity import ProductActivity
from marketplace.models.sale import Sale
from marketplace.models.sale_product_activity import SaleProductActivity


class SaleProductActivitySerializer(serializers.ModelSerializer):
    sales = serializers.SlugRelatedField(
        queryset=Sale.objects.all(),
        slug_field='sales',
        required=False
    )
    product_activity = serializers.SlugRelatedField(
        queryset=ProductActivity.objects.all(),
        slug_field='product_activity',
        required=False
    )
    quantity = serializers.CharField(allow_blank=False, required=True)

    class Meta:
        model = SaleProductActivity
        fields = ('id', 'sales', 'product_activity', 'quantity')
