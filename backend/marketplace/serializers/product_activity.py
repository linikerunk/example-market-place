from rest_framework import serializers
from marketplace.services.product_activity import ProductActivityService
from marketplace.models.product_activity import ProductActivity


class ProductActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductActivity
        fields = (
            'pk', 'name', 'is_product', 'price', 'commission', 'quantity',
            '_get_total_price'
        )
    
    def to_internal_value(self, data, *args, **kwargs):
        ProductActivityService(
            name=data['name'],
            is_product=data['is_product'],
            price=data['price'],
            commission=data['commission'],
            quantity=data['quantity']
        ).handle_commission_range()
        return super().to_internal_value(data, *args, **kwargs)