from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import *


@login_required(login_url='loginpage')
def wishlistIndex(request):
    wishlistitems = Wishlist.objects.filter(user=request.user)
    data = {
        'wishlistitems' : wishlistitems
    }
    return render(request, "auth/WISHLIST.html", data)


def addtowishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Products.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status': "Product Already in Wishlist"})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "Product Added to Wishlist"})

            else:
                return JsonResponse({'status': "No Such Product Found"})
        else:
            return JsonResponse({'status': "Login to Continue"})
    return redirect("/")

def deleteFromWishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitems = Wishlist.objects.get(product_id=prod_id, user=request.user)
                wishlistitems.delete()
                return JsonResponse({'status': "Product Removed from Wishlist"})
            else:
                return JsonResponse({'status': "Product not found in wishlist"})

        else:
            return JsonResponse({'status': "Login to Continue"})
    return redirect('/')