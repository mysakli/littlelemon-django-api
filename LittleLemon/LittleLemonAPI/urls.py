from django.urls import path
from . import views


urlpatterns = [ 
    path('category', views.CategoryView.as_view()), 
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('groups/manager/users', views.ManagerGroupView.as_view()),
    path('groups/manager/users/<int:pk>', views.SingleUserManagerGroupView.as_view()),
    path('groups/delivery-crew/users', views.DeliveryCrewGroupView.as_view()),
    path('groups/delivery-crew/users/<int:pk>', views.SingleUserDeliveryCrewGroupView.as_view()),
    path('cart/menu-items', views.ListCreateBulkDeleteCart.as_view()),
    path('orders', views.OrdersView.as_view()),
    path('orders/<int:pk>', views.SingleOrderView.as_view()),
    path('order-items', views.OrderItemsView.as_view()),
    
    
    
] 