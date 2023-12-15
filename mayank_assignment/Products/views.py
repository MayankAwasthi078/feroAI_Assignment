from django.shortcuts import render
from rest_framework import viewsets
from Products.models import Product
from rest_framework.response import Response
from rest_framework import status
from Products.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    

