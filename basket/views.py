from rest_framework import views
from rest_framework.response import Response

from basket import serializers


class BasketApiView(views.APIView):
    def post(self, request):
        serializer = serializers.OrderSerializers(
            data=request.data
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)