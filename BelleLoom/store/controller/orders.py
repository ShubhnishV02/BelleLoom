from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import *
from django.contrib.auth.models import User


@login_required(login_url='loginpage')  
def myordersIndex(request):
    orders = Order.objects.filter(user=request.user)
    cartitems = Cart.objects.filter(user=request.user)
    data = {
        "orders" : orders,
        "cartitems": cartitems,
    }
    return render(request, "auth/MYOrders.html", data)


def orderview(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    data = {"order": order, "orderitems":orderitems }
    return render(request, "auth/view.html",data)
