from django.shortcuts import render
from django.http import request
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import CategorySerializer, MenuItemSerializer, UserSerializer, CartSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.mixins import RetrieveModelMixin
from rest_framework import generics, filters, status
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.views import APIView
from .permissions import CanChangeOrderFields


# Create your views here.

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    search_fields = ['category__title', 'title']
    ordering_fields = ['price']
    

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [DjangoModelPermissions]
           
            
class ManagerGroupView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups=1)
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]

    def get(self, request):
        user = self.request.user
        if user.groups.filter(name='Manager').exists() or user.is_superuser:
            queryset = User.objects.filter(groups=1)
            serializer = UserSerializer(queryset, many=True)
            
            return Response(serializer.data)
        else:
            return Response({'message': 'You are not authorized'}, 403)
     

    def post(self, request):
        edited_user = request.data['username']
        user_object = User.objects.get(username=edited_user)
        user_object.groups.set([1])
        user_object.save()
        return Response({'message' : '201 - Created'})



class SingleUserManagerGroupView(generics.DestroyAPIView):
    queryset = User.objects.filter(groups=1)
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]


class DeliveryCrewGroupView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups=2)
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]

    def get(self, request):
        user = self.request.user
        if user.groups.filter(name='Manager').exists() or user.is_superuser:
            queryset = User.objects.filter(groups=2)
            serializer = UserSerializer(queryset, many=True)
            
            return Response(serializer.data)
        else:
            return Response({'message': 'You are not authorized'}, 403)
     

    def post(self, request):
        edited_user = request.data['username']
        user_object = User.objects.get(username=edited_user)
        user_object.groups.set([2])
        user_object.save()
        return Response({'message' : '201 - Created'})

    

  
class SingleUserDeliveryCrewGroupView(generics.DestroyAPIView):
    queryset = User.objects.filter(groups=2)
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]


class ListCreateBulkDeleteCart(generics.ListCreateAPIView, APIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        user = self.request.user

        return Cart.objects.filter(user=user)


    def delete(self, request):
        user = self.request.user
        queryset = Cart.objects.filter(user=user)           
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrdersView(generics.ListAPIView, APIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        elif user.groups.filter(name='Delivery-crew').exists():
            return Order.objects.filter(delivery_crew=user)
        else:
            return Order.objects.filter(user=user)
    
    def post(self, request, format=None):
        user = self.request.user
        cart = Cart.objects.filter(user=user)
        total = 0
        for item in cart:
            total += item.price 
        
        order = Order.objects.create(user=user, total = total)
        serializer = OrderSerializer(order, context={'request':request}, data = request.data)
        if serializer.is_valid():
            serializer.save()

            for item in cart:
                OrderItem.objects.create(quantity= item.quantity, unit_price= item.unit_price, price= item.price, 
                                         menuitem = item.menuitem, order_id = order.pk)
            
            cart.delete()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SingleOrderView(generics. RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, CanChangeOrderFields]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        elif user.groups.filter(name='Delivery-crew').exists():
            return Order.objects.all()
        else:
            return Order.objects.filter(user=user)

    
# testing viewclass
class OrderItemsView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



