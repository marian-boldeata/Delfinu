from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product

def index(request):
    return render(request, "market/home.html")

def products_list(request):
    all_products = Product.objects.all()
    context = {
        "products":all_products
    }
    return render(request,"market/product_list.html", context)

def single_product(request, product_id):
    one_product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": one_product
    }
    return render(request, "market/one_product.html", context)

def about(request):
    return render(request, "market/about.html")


