from django.shortcuts import render
from rest_framework import viewsets
from Customers.models import Customer
from rest_framework.response import Response
from rest_framework import status
from Customers.serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

