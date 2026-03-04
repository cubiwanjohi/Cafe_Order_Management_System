from rest_framework import serializers
from .models import Category, MenuItem, Order, OrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'items', 'created_at']