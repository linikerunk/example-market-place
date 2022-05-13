from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from user.serializers.client import ClientSerializer
from user.models.client import Client


class ClientView(APIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)