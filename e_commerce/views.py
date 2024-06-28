from django.shortcuts import render, get_object_or_404, render
from .models import product, Customer 

# Create your views here.
def product_list(request):
    products = product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'e_commerce/product_list.html',context) 
 
def product_detail(request, pk):
    product = get_object_or_404(product, pk=pk)
    context = {
        'product':product
    }
    return render(request, 'e_commerce/product_detail.html', context)

def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request,'e_commerce/ustomer_list', context)

def customer_detail(request, pk):
    customer = get_object_or_404(customer, pk=pk)
    context ={
        'customer': customer
    }
    return render (request, 'e_commerce/customer_detail', context)
                  