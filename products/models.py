from django.db import models

# Create your models here.
from enum import Enum
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductType(Enum):
    BIG_ITEM = 1
    SMALL_ITEM = 2
 
class Product(models.Model):   
    class ProductType2(models.IntegerChoices):
        BIG_ITEM = 1, "bigger then 10 inch"
        SMALL_ITEM = 2, "smaller then 10 inch"      

    name = models.CharField(max_length=200, null=False)
    seller = models.CharField(max_length=200, null=False)
    Year_manufacture = models.DateField()
    type = models.SmallIntegerField(choices=ProductType2.choices, default=ProductType2.BIG_ITEM , null=False)
    price = models.DecimalField(decimal_places=2,max_digits=100 ,default=True)
    created_time=models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField(default=1)
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')
    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ManyToManyField(User )   
    product = models.ManyToManyField(Product)
    buy_date = models.DateTimeField()
    quantity=models.IntegerField(default=1)
    price = models.DecimalField(decimal_places=2,max_digits=100 ,default=True)
    total_price = models.DecimalField(decimal_places=2,max_digits=100 ,default=True)
    is_cart = models.BooleanField(default=True)
    def get_total_price(self):
        total=0
        for product in self.product.all():
            total=total+product.price
        return total



class Orders(models.Model):
    customerorder=models.ManyToManyField(Cart)
    def __str__(self):
        return '{}'.format(self.id)
    

    

