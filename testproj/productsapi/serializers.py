from rest_framework import serializers
from products.models import product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=["ProductName","ProductDescription","ProductPrice"]