from rest_framework import serializers
from Orders.models import Order,OrderItem
from Products.serializers import ProductSerializer
from Customers.serializers import CustomerSerializer

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    customer=CustomerSerializer()
    class Meta:
        model=Order
        fields=['id','customer', 'order_date','address']
       
class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    order=OrderSerializer()
    product=ProductSerializer()
    id=serializers.ReadOnlyField()
    class Meta:
        model=OrderItem
        fields=['id','order','product','quantity']      