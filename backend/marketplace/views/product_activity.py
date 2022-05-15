from django.db.models import Q
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from marketplace.models.product_activity import ProductActivity
from marketplace.services.product_activity import ProductActivityService
from marketplace.serializers.product_activity import ProductActivitySerializer


class ProductActivityViewSet(ModelViewSet):
    queryset = ProductActivity.objects.all()
    serializer_class = ProductActivitySerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace();
        search = request.GET.get('search')
        if search:
            return self.queryset.filter(Q(pk=search) | Q(name=search))
        return self.queryset.all()

    def create(self, request, ):
        serializer = ProductActivitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # @action(detail=False, methods=['get'])
    # def search_for_product_activity(self, request, *args, **kwargs):
    #     search = request.GET.get('search_product_activity')
    #     product_activity = ProductActivity.objects.filter(
    #         Q(pk=search) | Q(name=search)
    #     )
    #     serializer = ProductActivitySerializer('json', product_activity)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


    def list(self, request, *args, **kwargs):
        serializer = ProductActivitySerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
