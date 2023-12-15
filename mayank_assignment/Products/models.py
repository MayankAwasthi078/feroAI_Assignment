from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    weight= models.DecimalField(
        max_digits=5,
        decimal_places=1,
        validators=[
            MaxValueValidator(25.0),
            MinValueValidator(1)
        ],
    )
    def __str__(self):
        return self.name