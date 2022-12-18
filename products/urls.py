from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'products'

urlpatterns = [
   path('', login_required(views.products, login_url='elogin'), name="products"),
   path('search/', views.search, name="search"),
   
   path('add/', views.add_product, name="add"),
   path('add_product_action/', views.add_product_action, name="add_product_action"),
   path('delete/ <pk>', views.delete_product, name="delete_product"),
   path('single_product/',views.single_product,name='single_product'),
   # path('product_detail/ <pk>', views.product_detail, name="product_detail"),
   
   
   path('cart/',views.cart,name='cart'),
   path('<id>/add_to_cart', views.add_to_cart, name='add_to_cart'),
   path('remove_from_cart/<id>', views.remove_from_cart, name='remove_from_cart'),
   
   path('add_to_orders/', views.all_orders, name="add_to_orders"),
   path('all_orders/', views.all_orders, name="all_orders"),

   
   
   
   # path('<pk>/edit_product', views.edit_product, name="edit_product"),
   # path('<id>/order_detail/', views.order_detail, name="order_detail"),
    
]