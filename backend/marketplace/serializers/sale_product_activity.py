from rest_framework import serializers
from marketplace.models.product_activity import ProductActivity
from marketplace.models.sale_product_activity import SaleProductActivity
from .sale import SaleSerializer
from marketplace.serializers.product_activity import ProductActivitySerializer
from marketplace.services.sale_product_activity import SaleProductActivityService


class SaleProductActivitySerializer(serializers.ModelSerializer):
    sale = SaleSerializer(required=True)
    product_activity = ProductActivitySerializer(required=True)

    def to_internal_value(self, data, *args, **kwargs):
        import ipdb; ipdb.se
        SaleProductActivityService(
            operation_date=self.initial_data['sale']['operation_date'],
            commission=self.initial_data['product_activity']['commission']
        ).verify_commission_time()
        return super().to_internal_value(data, *args, **kwargs)

    def create(self, validated_data):
        name = self.data['product_activity']['name']
        product_activity = ProductActivity.objects.get()
        return product_activity

    def to_representation(self, instance):
        import ipdb; ipdb.set_trace();

    #     representation = super(EquipmentSerializer, self).to_representation(instance)
    #     representation['assigment'] = AssignmentSerializer(instance.assigment_set.all(), many=True).data
    #     return representation 

    class Meta:
        model = SaleProductActivity
        fields = ('pk', 'sale', 'product_activity')
