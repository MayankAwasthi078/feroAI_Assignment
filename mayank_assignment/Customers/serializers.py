from rest_framework import serializers
from Customers.models import Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Customer
        fields="__all__"
        