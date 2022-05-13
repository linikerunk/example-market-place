from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from marketplace.serializers.sale import SaleSerializer
from marketplace.models.sale import Sale


class SaleView(APIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

