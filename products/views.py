from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.decorators import login_required
from products.forms import ProductForm
from products.models import Cart, Orders, Product
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages 
from django.http.response import JsonResponse


#    main products
def products(request):
    product_list = Product.objects.all()
    return render(request, 'product.html', {'product_list':product_list})

def single_product(request, pk):
    product = Product.objects.filter(id = pk)
    product.name = request.POST.get("name")
    return render(request,'product.html',{'products':product})
    


def add_product(request):
    context = {
        'productform': ProductForm(),
    }
    return render(request, 'addproduct.html', context)

@login_required
def add_product_action(request):
    if not request.user.is_staff:
        return HttpResponse('YOU ARE Not allowed to delete products')
    productform = ProductForm(request.POST, request.FILES)
    if productform.is_valid():
        productform.save()
        return redirect('products:products')
    else:
        context = {
            'productform': productform,
        }
        return render(request, 'addproduct.html', context)


@login_required
def delete_product(request, pk):
    if not request.user.is_staff:
        return HttpResponse('YOU ARE Not allowed to delete products')
    product = Product.objects.filter(id=pk).delete()
    if request.method =="GET":
        return render(request, 'product.html')
    else:
        product.name = request.POST.get("name")
        product.delete()   
        messages.info(request, "DELETED SUCCESSFULY")
        return render(request, 'deleteproduct.html', {'products':product, 'delete':True})


def search(request):
    my_search = request.GET.get('search')
    product_list = Product.objects.filter(name__contains=my_search)
    return render(request, 'single-product.html', {'products':product_list})



def all_orders(request,):
    all_orders = Cart.objects.filter(customer = request.user)
    return render(request,'all_orders.html',{'all_orders':all_orders})


@login_required
def add_to_orders(request):
    order = Cart.objects.get(customer = request.user)
    if ObjectDoesNotExist:
        print("order does not exist - creating order")
    order = Orders()
    from datetime import datetime
    order.customerorder=datetime.now()
    order.save()
    cart.customer.add(request.user)
    order.customerorder.add(order)
    # return redirect('products:cart')
    return render(request, "all_orders.html" ,{'order':order})




def cart(request):
    cart = Cart.objects.get(customer=request.user)
    return render(request,"cart.html",{'cart':cart})


@login_required
def add_to_cart(request,id):
        try:
            product = Product.objects.get(pk=id)
        except:
            messages.error(f"NO PRODUCT WITH ID:{id}") 
            return redirect('index')

        try:
            cart = Cart.objects.get(customer = request.user)
        except ObjectDoesNotExist:
            print("cart does not exist - creating cart")
            cart = Cart()
        from datetime import datetime
        cart.buy_date=datetime.now()
        cart.save()
        cart.customer.add(request.user)
        cart.product.add(product)
        # return redirect('products:cart')
        return render(request, "cart.html" ,{'cart':cart})


@login_required
def remove_from_cart(request,id):
        try:
            product = Product.objects.get(pk=id)
        except:
            messages.error(f"NO PRODUCT WITH ID:{id}") 
            return redirect('index')
        
        cart = Cart.objects.get(customer = request.user)
        cart.product.remove(product)
        cart.save()
        return render (request,"cart.html", {'cart':cart})





# def product_detail(request, pk):
#     product = Product.objects.get(id=pk)
#     return render(request, 'product_detail.html', {'products':product})

# def order_detail(request,pk):
#     order = Orders.objects.get(id=pk)
#     customer = Cart.objects.filter(order_id=order.id)
#     return render(request,'order_detail.html',{'cart':customer})



# def edit_product(request,pk):
#     product = Product.objects.get(id=pk)
#     if request.POST:
#         product.name = request.POST.get('name')
#         product.price = request.POST.get('price')
#         product.Year_manufacture = request.POST.get('Year_manufacture')
#         try:
#             product.save()
#             messages.info(request, 'Saved successfuly!')
#             return redirect('products:product_detail', product.id)
#         except Exception as ex:
#             messages.error(request, 'ERROR saving product!'+ str(ex))
#             product = Product.objects.get(id=pk)
#     return render(request, 'poduct_detail.html', {'products':product, 'edit_product': True})


