from rest_framework import serializers
from marketplace.models.product_activity import ProductActivity


class ProductActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductActivity
        fields = ('id', 'name', 'is_product', 'price', 'commission')
