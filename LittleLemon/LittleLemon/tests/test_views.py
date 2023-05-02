from rest_framework.test import APITestCase, APIClient, force_authenticate, APIRequestFactory
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from LittleLemonAPI.models import MenuItem, Cart, Category
from LittleLemonAPI.serializers import MenuItemSerializer

class MenuItemsViewTest(APITestCase):
    def setUp(self):
        self.c = APIClient()
        self.user = User.objects.create_user('tester', 'tester@littlelemon.com', 'testerpass')       
        self.c.force_authenticate(user=self.user) 
    
    def test_list_menu_items(self):
        response = self.c.get('/api/menu-items')
        self.assertEquals(response.status_code, 200)
    
    def test_create_menu_item(self):
        # client = APIClient()
        # Group.objects.create(name='Manager')
        # manager = User.objects.create_user('manager', 'manager@littlelemon.com', 'managerpass')
        # manager.groups.set([1])
        # manager.save()
        # client.force_authenticate(user=manager)
        

        #Access denied for non-managers
        response = self.c.post('/api/menu-items', {'title': 'Pumpkin Juice', 'price': 2.50, 'category_id': 3}, formar='json')
        self.assertEquals(response.status_code, 403)

class SingleMenuItemViewTest(APITestCase):
    def setUp(self):
        self.c = APIClient()
        self.user = User.objects.create_user('tester', 'tester@littlelemon.com', 'testerpass')       
        self.c.force_authenticate(user=self.user)
        

        Category.objects.create(title='dessert')
        MenuItem.objects.create(title='Chocolate Frog', price=3, category_id=1, featured=False)
    
    def test_list_menu_item(self):
        response = self.c.get('/api/menu-items/1')
        serializer = MenuItemSerializer(response)
        self.assertEquals(response.status_code, 200)
        # self.assertEquals(response.data, serializer.data)
        self.assertEquals(response.data, {
	"id":1,
	"title":"Chocolate Frog",
	"price":"3.00",
	"featured":False,
	"category": {
		"id": 1,
		"title": "dessert"
	}
})

    
class CartViewTest(APITestCase):
    def setUp(self):
        self.c = APIClient()
        self.user = User.objects.create_user('customer', 'customer@littlelemon.com', 'customerpass')       
        self.c.force_authenticate(user=self.user)

        Category.objects.create(title='dessert')
        MenuItem.objects.create(title='Chocolate Frog', price=3, category_id=1, featured=False)
        self.request_post = self.c.post('/api/cart/menu-items', {'menuitem':1, 'unit_price': 3, 'quantity': 1})


    def test_add_item_to_cart(self):
        self.assertEquals(self.request_post.status_code, 201)
        
    
    def test_list_cart_items(self):
        request_get = self.c.get('/api/cart/menu-items')
        self.assertEquals(request_get.status_code, 200)
    
    def test_delete_items_from_cart(self):
        # cart_items = Cart.objects.filter(user=self.user)
        response = self.c.delete('/api/cart/menu-items')
        self.assertEquals(response.status_code, 204)
        

            

        
    
