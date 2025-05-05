from django.shortcuts import render

# Create your views here.
def cart(request):
    context={}
    return render(request,"ecommerce_app/cart.html")
def checkout(request):
    context={}
    return render(request,'ecommerce_app/checkout.html')
def store(request):
    context={}
    return render(request,'ecommerce_app/store.html')