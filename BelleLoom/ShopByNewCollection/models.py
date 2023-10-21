from django.db import models
from django.conf import settings

# Create your models here.
class Size(models.Model):
    name = models.CharField(max_length=5 , null=True)


class ShopByNewCollection(models.Model):
    Product_ID = models.IntegerField(primary_key=True)
    Image = models.ImageField(upload_to='ShopByNewCollection/images')
    Product_Name = models.CharField(max_length=100)
    Customer_Cost = models.DecimalField(max_digits=10, decimal_places=2)
    Actual_Cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Size_Of_Product = models.PositiveIntegerField(default=0)
    Quantity = models.PositiveIntegerField(null=True , default=1)
    Stock_Of_Product_Quantity = models.PositiveIntegerField(null=True , default=0)
    Stock_Of_Product_Sizes_Available = models.TextField(max_length=1000, null=True)
    Ships_in_Days = models.PositiveIntegerField(default=10)
    Product_Description = models.TextField(max_length=2800)
    Measurement_Details = models.TextField(max_length=2000)
    Fabric_Used = models.TextField(max_length=1500)
    Care_Instructions = models.TextField(max_length=1500)
