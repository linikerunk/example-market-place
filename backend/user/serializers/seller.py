from rest_framework import serializers
from user.models.seller import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'name',)