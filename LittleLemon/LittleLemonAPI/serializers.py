from rest_framework import serializers
from .models import Category, MenuItem, Cart, Order, OrderItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only = True)
    category = CategorySerializer(read_only = True)
    
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category_id', 'category']
        extra_kwargs = {'price': {'min_value':0}, }


class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        default = serializers.CurrentUserDefault()
    )
    price = Cart.price
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'quantity','menuitem', 'unit_price', 'price']
      
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'menuitem', 'quantity', 'unit_price', 'price']
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        default = serializers.CurrentUserDefault()
     )
    
    # total = Order.total

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date', 'order_items']
        


