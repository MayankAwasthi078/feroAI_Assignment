from django.shortcuts import render
from rest_framework import viewsets
from Orders.models import Order,OrderItem
from Products.models import Product
from Customers.models import Customer
#from url_filter.integrations.drf import DjangoFilterBackend
from Orders.serializers import OrderSerializer,OrderItemSerializer
from Products.serializers import ProductSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["customer__name"]

class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['order__customer__name','product__name']

