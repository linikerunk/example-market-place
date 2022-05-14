from marketplace.models.sale import Sale
from marketplace.serializers.sale import SaleSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions, status


class SaleViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (permissions.AllowAny,)
    combined_lookup_field = ['pk', 'slug']

    def avaliacoes(self, request, *args, **kwargs):
        serializer = SaleSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = SaleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": serializer.data}, status=status.HTTP_201_CREATED)
