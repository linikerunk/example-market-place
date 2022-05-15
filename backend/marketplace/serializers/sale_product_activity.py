from rest_framework import serializers
from marketplace.models.sale import Sale
from marketplace.models.product_activity import ProductActivity
from marketplace.models.sale_product_activity import SaleProductActivity
from .sale import SaleSerializer
from marketplace.serializers.product_activity import ProductActivitySerializer
from marketplace.services.sale_product_activity import SaleProductActivityService


class SaleProductActivitySerializer(serializers.ModelSerializer):
    sale = SaleSerializer(required=True)
    product_activity = ProductActivitySerializer(required=True)

    def to_internal_value(self, data, *args, **kwargs):
        data = SaleProductActivityService(
            operation_date=self.initial_data['sale']['operation_date'],
            commission=self.initial_data['product_activity']['commission']
        ).verify_commission_time()


    def create(self, validated_data):
        sale = Sale.objects.get(
            pk=self.initial_data['sale']['id']
        )
        product_activity = ProductActivity.objects.get(
            pk=self.initial_data['product_activity']['pk']
        )
        sale_product_activity = SaleProductActivity.objects.create(
            sale=sale,
            product_activity=product_activity
        )
        
        return sale_product_activity

    class Meta:
        model = SaleProductActivity
        fields = ('pk', 'sale', 'product_activity')
