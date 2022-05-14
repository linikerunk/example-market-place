from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions, status
from marketplace.models.sale_product_activity import SaleProductActivity
from marketplace.serializers.sale_product_activity import SaleProductActivitySerializer


class SaleProductActivityViewSet(ModelViewSet):
    queryset = SaleProductActivity.objects.all()
    serializer_class = SaleProductActivitySerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        serializer = SaleProductActivitySerializer(
            self.get_queryset(),
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)
        SaleProductActivitySerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = SaleProductActivitySerializer(
            self.get_queryset(),
            data=request.data,
            many=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data}, status=status.HTTP_201_CREATED)
