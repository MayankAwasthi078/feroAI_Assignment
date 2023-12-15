from django.db import models

class Customer(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    contact_number= models.CharField(max_length=10)
    email=models.EmailField(max_length = 254)

    def __str__(self):
        return self.name