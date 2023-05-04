from rest_framework import serializers
from shop.models import Furniture


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'


class CartItemSerializer(serializers.Serializer):
    product = FurnitureSerializer()
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)
# ['name', 'description', 'price', 'image', 'size', 'producer']
