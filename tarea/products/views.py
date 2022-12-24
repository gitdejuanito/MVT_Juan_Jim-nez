from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products

# Create your views here.

def create_product (request):
    new_product=Products.objects.create (name ="hermana", price=32, stock=True)
    print(new_product)
    return HttpResponse("se nuevo producto")

def list_products(request):
    all_products= Products.objects.all()
    context ={
        "products":all_products,
    }
    return render(request, "list_products.html", context=context)


