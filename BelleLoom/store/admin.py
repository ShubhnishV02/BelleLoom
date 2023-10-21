from django.contrib import admin
from store.models import Category,Products,Cart, Order, OrderItem, Country, State, City, Profile, DeliveryArea

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("Product_Name", "status","created_at")

class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "product_qty","product")

class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Products)
admin.site.register(Cart, CartAdmin )
admin.site.register(Order)
admin.site.register(OrderItem)

admin.site.register(Country, CountryAdmin)
admin.site.register(State)
admin.site.register(City)



admin.site.register(Profile)

admin.site.register(DeliveryArea)
