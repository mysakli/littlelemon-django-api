# littlelemon-django-api

This is a RESTful API for a food ordering system of a mock restaurant (Little Lemon) built with Django Rest Framework (DRF). This project was built as part of a Back-End Developer specialization  on Coursera. The API provides endpoints to manage authentication, menu items and orders.



## API Endpoints

For testing the API locally in the browser or via a REST client (e.g. Postman or Insomnia), use `http://localhost:8000/` with the respective endpoint.

All endpoints *require authentication* via token-based authentication. You can obtain an authentication token by sending a POST request to the `/api/token/` endpoint with valid credentials. You can create your own account at `/api/users` or use [the mock accounts](#mock-accounts) listed at the end of this document.


### Menu Items
`api/category` // list menu categories\
`api/menu-items` // GET - list all menu items; POST, PUT, PATCH, DELETE - create/update/delete a new item (*managers* only)\
`api/menu-items/{id}` GET - list a single menu item

### Cart
`api/cart/menu-items` // GET - returns current items in the cart for the current user; POST - adds a menu item to the cart; DELETE - deletes all menu items from the user's cart

### Orders
`api/orders` // GET - list user's orders (*customer*)/ list all orders (*managers*)/ list assigned orders (*delivery crew*); POST - adds items from the cart to a newly created order and deletes all items from the cart \
`api/orders/{id}` // GET - returns all items for this order id; PUT, PATCH - *managers* can assign delivery crew to the order or update the delivery status (*managers, delivery crew*); DELETE - deletes the order(*managers* only)\
`api/order-items` // list order items linked to the logged user


### Authentication
`api/users` // create an account
`api/token/login` // POST - get a token

### Groups
`api/groups/manager/users` // GET - list users assigned to the 'manager' group (managers only); POST - assign a user to the 'manager' group (*managers* only) \
`api/groups/manager/users/{id}` // DELETE - removes the user from the 'manager' group  
`api/groups/delivery-crew/users/` // GET - list users assigned to the 'delivery crew' group (managers only); POST - assign a user to the 'delivery crew' group (*managers* only)\
`api/groups/delivery-crew/users/{id}` // DELETE - removes the user from the 'delivery crew' group

### Mock Accounts

**Superuser**

***username:*** admin\
***password:*** adminadmin\
***token:*** 86f1228fa05ffd648ed66b79020f3d48815102fe

**Managers**

patricia\
man123.!\
b59a0927ed211086f063460d2d9a30cc9088d6b3

meredith\
m1m2m3.!\
b8e9d0d306e8e25084ac1ab329e7cf3fd042e6ac

**Delivery crew**

albert\
del123.!\
9903250b0475332280826e3aac6ca9db4cc16ada

bob\
del234.!\
0a4c14364460292b82f4ea21e869a019f50a8d06

**Customers**

customer1\
c1c2c3.!\
9d3573c19fc807903fb333b220f4a20bb9b42ad4

customer2\
c1c2c3.!\
d47ccadf5ec24a5efc730915de6bf839a7c2a9f0





  


