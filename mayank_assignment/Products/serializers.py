from rest_framework import serializers
from Products.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Product
        fields="__all__"
