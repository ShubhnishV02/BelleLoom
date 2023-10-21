from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import *
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist


import random


@login_required(login_url='loginpage')
def checkoutINDEX(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.Product_Quantity :
            item.delete() # Delete the instance

    cartitems = Cart.objects.filter(user=request.user)
    overall_total_price = 0
    

    for item in cartitems:
        item_total_price = item.product.Selling_Price * item.product_qty
        # Calculate the overall total price
        overall_total_price += item_total_price

    
    userprofile = Profile.objects.filter(user=request.user).first()

    # single_product_total_prices = list(set(single_product_total_prices)
    data = {"cartitems" : cartitems, "overall_total_price": overall_total_price, "userprofile": userprofile}
    return render(request, "auth/CHECKOUT.html", data)



@login_required(login_url='loginpage')
def placeOrder(request):
    if request.method == "POST":

        # "globally" declared the city, state and country variable to use the instance for new user as well as registered user who placed an order for autofilling address.
        # Get or create City, State, and Country instances
        city_name = request.POST.get("city")
        state_name = request.POST.get("state")
        country_name = request.POST.get("country")

        try:
            city_instance, created = City.objects.get_or_create(name=city_name)
        except ObjectDoesNotExist:
            city_instance = City.objects.create(name=city_name)

        try:
            state_instance, created = State.objects.get_or_create(name=state_name)
        except ObjectDoesNotExist:
            state_instance = State.objects.create(name=state_name)

        try:
            country_instance, created = Country.objects.get_or_create(name=country_name)
        except ObjectDoesNotExist:
            country_instance = Country.objects.create(name=country_name)

        # now these 3 instances used in both currentuser userprofile and neworders which is declared in upper code


        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name :
            currentuser.first_name = request.POST.get("firstname")
            currentuser.last_name = request.POST.get("lastname")
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get("phone")
            userprofile.address1 = request.POST.get("address1")
            userprofile.address2 = request.POST.get("address2")
            userprofile.city = city_instance
            userprofile.state = state_instance
            userprofile.country = country_instance
            userprofile.pincode = request.POST.get("pincode")
            userprofile.save()
            


        # these are the code which takes the entry from user before placing an order
        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get("firstname")
        neworder.lname = request.POST.get("lastname")
        neworder.email = request.POST.get("email")
        neworder.phone = request.POST.get("phone")
        neworder.address1 = request.POST.get("address1")
        neworder.address2 = request.POST.get("address2")
       
        neworder.city = city_instance
        neworder.state = state_instance
        neworder.country = country_instance
        neworder.pincode = request.POST.get("pincode")

        neworder.payment_mode = request.POST.get("payment_mode")

        cartitem = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cartitem:
            cart_total_price = cart_total_price + item.product.Selling_Price * item.product_qty


        neworder.overall_total_price = cart_total_price
        trackno = "prod" + str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_no = trackno) is None:          #using this loop for checking if the tracking no is not matched from any other tracking no. if it is so.. than it will false the loop and new tracking no. will create.
            trackno = "prod" + str(random.randint(1111111,9999999))

        neworder.tracking_no = trackno

        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order = neworder,
                product = item.product,
                price = item.product.Selling_Price,
                quantity = item.product_qty
            )

            # to decrease the product quantity from available stock

            orderproduct = Products.objects.filter(id=item.product_id).first()
            orderproduct.Product_Quantity = orderproduct.Product_Quantity - item.product_qty
            orderproduct.save()

        # to clear user's cart
        Cart.objects.filter(user=request.user).delete()

        messages.success(request,"Your order has been placed successfully")

    return redirect("/")
