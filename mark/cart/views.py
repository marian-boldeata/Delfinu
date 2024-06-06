from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product, Cart_item


def continue_shopping(request):
    return redirect('market/product_list.html')

def view_cart(request):
    cart_items = Cart_item.objects.filter(user = request.user)
    for item in cart_items:
        item.stack_price = item.product.pret * item.quantity

    total_price = sum(item.stack_price for item in cart_items)
    context ={"cart_items":cart_items, "total_price":total_price}
    return render(request, 'cart/view_cart.html', context)

def add_to_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart_item.objects.get_or_create(product = product, user = request.user)
    cart_item.quantity +=1
    cart_item.save()
    return redirect("cart:view_cart")

def remove_from_cart(request,item_id):
    cart_item = Cart_item.objects.get(id = item_id)
    cart_item.delete()
    return redirect("cart:view_cart")



