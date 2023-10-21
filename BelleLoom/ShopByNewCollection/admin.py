from django.contrib import admin
from .models import ShopByNewCollection
# Register your models here.

class ShopByNewCollectionAdmin(admin.ModelAdmin):
    list_display = ("Product_Name", "Customer_Cost","Size_Of_Product", "Quantity", "Ships_in_Days" ,"Fabric_Used")


admin.site.register(ShopByNewCollection, ShopByNewCollectionAdmin)