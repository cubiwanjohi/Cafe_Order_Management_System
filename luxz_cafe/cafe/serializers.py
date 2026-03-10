from rest_framework import serializers
from .models import Category, MenuItem, Order, OrderItem

"""
    Handles the conversion of Category models.
    Used to group menu items (e.g., 'Drinks', 'Snacks').
    """
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

"""
    Handles the conversion of individual food/drink items.
    Converts name, description, price, and category into JSON.
    """
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

"""
    Handles the conversion of Customer Orders.
    Includes a special 'items' field to show what was bought.
    """
class OrderSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'items', 'created_at']