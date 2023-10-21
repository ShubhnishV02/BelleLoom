"""
URL configuration for SVFashion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from SVFashion import views
from django.conf import settings
from django.conf.urls.static import static

from store.controller import authview , cart, wishlist, checkout, orders


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homepage , name="homepage"),
    path('category/', views.Categoryy, name="category" ),                  # later may be created a new page for category because this name attribute requires a seperate Category page
    path('category/<str:slug>', views.categoryView, name="category" ),
    path('category/<str:cate_slug>/<str:prod_slug>', views.SINGLEPRODUCT, name="productview" ),

    path('singlePRODUCT/', views.SINGLEPRODUCT, name="singlePRODUCT" ),
    path('aboutus/', views.ABOUTUS, name="aboutus" ),
    path('contactus/', views.CONTACTUS, name="contactus" ),
    path('testimonials/', views.TESTIMONIALS, name="testimonials" ),
    path('privacy-policy/', views.PRIVACYPOLICY, name="privacy-policy" ),
    path('terms-and-conditions/', views.TERMSANDCONDITIONS, name="terms-and-conditions" ),
    path('faqs/', views.FAQS, name="faqs" ),


    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logoutpage"),

    path('add-to-cart/', cart.addtocart, name="addtocart"),
    path('cartview/', cart.viewcart, name="cartview"),
    path('update-cart/', cart.updateCart, name="updateCart"),
    path('delete-cart-item/', cart.deleteCartItem, name="deleteCartItem"),

    path('wishlist/',wishlist.wishlistIndex, name='wishlist'),
    path('add-to-wishlist/',wishlist.addtowishlist, name='addtowishlist'),
    path('delete-from-wishlist/',wishlist.deleteFromWishlist, name='deleteFromWishlist'),


    path('checkout/',checkout.checkoutINDEX, name='checkout'),
    path('place-order/',checkout.placeOrder, name='placeorder'),


    path('my-orders/',orders.myordersIndex, name='myorders'),
    path('view-order/<str:t_no>',orders.orderview, name='orderview'),

    path('check-delivery-area/', views.check_delivery_area, name='check_delivery_area'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

