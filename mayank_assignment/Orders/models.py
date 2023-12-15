from django.db import models
from Customers.models import Customer
from Products.models import Product
import datetime
from django.core.exceptions import ValidationError
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_number = models.CharField(max_length=200)
    date = models.DateField(default=datetime.date.today())
    order_date = models.DateTimeField(default=datetime.datetime.now(), blank='true')
    customer= models.ForeignKey(
        Customer,
        on_delete=models.PROTECT, related_name="Order"
    )
    address=models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if self.date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(Order, self).save(*args, **kwargs)
    def __str__(self):
        return self.order_number
    @property
    def customer_name(self):
        return self.customer.name

class OrderItem(models.Model):
    id= models.AutoField(primary_key=True)
    order=models.ForeignKey(
        Order,
        on_delete=models.PROTECT, related_name="OrderItem"
    )    
    product=models.ForeignKey(
        Product,
        on_delete=models.PROTECT, related_name="OrderItemProduct"
    )
    quantity=models.PositiveSmallIntegerField()
    def __str__(self):
        return self.product.name

