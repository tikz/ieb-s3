from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import Product
from api.serializers import ProductSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    """
     ViewSet de solo lectura que expone un endpoint de listado de productos (/api/products)
     y de get de un producto individual (/api/products/<code>)
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, pk=None):
        """ Override para que en lugar de recibir y buscar un producto por el ID interno
        de la base de datos, buscarlo por el campo str:code """
        product = get_object_or_404(self.queryset, code=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)