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

    def get_queryset(self, *args, **kwargs):
        search = self.request.GET.get('search')
        if search:
            return self.queryset.filter(
                Q(pk__icontains=search) | Q(name__icontains=search)
            )
        return self.queryset.all()

    def create(self, request, *args, **kwargs):
        serializer = ProductActivitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        serializer = ProductActivitySerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
