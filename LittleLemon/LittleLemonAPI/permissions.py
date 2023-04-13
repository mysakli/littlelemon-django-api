from rest_framework.permissions import BasePermission

class CanChangeOrder(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        if request.method in ['PATCH', 'PUT']:
          if request.user.groups.filter(name='Delivery-crew').exists() and not any(field in request.data for field in self.forbidden_fields_delivery):
              return True
          elif request.user.groups.filter(name='Manager').exists() and  not any(field in request.data for field in self.forbidden_fields_manager):
              return True
          return False
        elif request.method in ['DELETE']:
            if request.user.groups.filter(name='Manager').exists():
                return True
            return False
          
        return False

class CanChangeOrderFields(CanChangeOrder):
    forbidden_fields_manager = ['user', 'total', 'date']
    forbidden_fields_delivery = ['user', 'delivery_crew', 'total', 'date']



        
             
  


 
