from django.db import models

# Create your models here.

class product(models.Model):
    ProductName= models.CharField(max_length=15)
    ProductDescription=models.TextField()
    ProductPrice=models.DecimalField(max_digits=10,decimal_places=2)