from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from product import serializers

from product.models import NewProduct, Category


class ProductViewSet(ModelViewSet):
    queryset = NewProduct.objects.all()
    # serializer_class = serializers.ProductSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        else:
            return serializers.ProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny(),]
        else:
            return [permissions.IsAuthenticated(),]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAdminUser]