from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import *


def addtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Products.objects.get(id=prod_id)
            if (product_check):
                if (Cart.objects.filter(product_id = prod_id)):
                    return JsonResponse({"status": "Product Already in Cart"})
                else:
                    prod_qty = int(request.POST.get("product_qty"))

            else:
                return JsonResponse({"status": "No such product found"})
        else:
            return JsonResponse({'status': "Login to Continue"})
        
    return redirect("/")

def viewcart(request):
    cartdata = Cart.objects.filter()
    data = {'cartdata' : cartdata}
    return render(request, "auth/CartData.html" , data)


def updateCart(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cartdata = Cart.objects.get(product_id=prod_id)
            cartdata.product_qty = prod_qty
            cartdata.save()
        return JsonResponse({"status":"Update Cart Successfully"})
    return redirect("/")


def deleteCartItem(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id)
            cartitem.delete()
        return JsonResponse({"status":"Removed Item Successfully"})
    return redirect("/")