from rest_framework import serializers
from product_app.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'price', 'description','image']