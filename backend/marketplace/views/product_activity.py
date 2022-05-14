from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions, status
from marketplace.models.product_activity import ProductActivity
from marketplace.serializers.product_activity import ProductActivitySerializer


class ProductActivityViewSet(ModelViewSet):
    queryset = ProductActivity.objects.all()
    serializer_class = ProductActivitySerializer
    permission_classes = (permissions.AllowAny,)

    @action(detail=True, methods=['get'])
    def product_activitys(self, request, *args, **kwargs):
        serializer = ProductActivitySerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProductActivitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data}, status=status.HTTP_201_CREATED)
