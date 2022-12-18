from django.forms import ModelForm
from .models import Orders, Product
from django.contrib.auth.models import User

 
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'seller', 'Year_manufacture','price', 'type', 'quantity', 'image']

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['customerorder']
        
 
        