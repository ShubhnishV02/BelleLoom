from django.db import models

from django.contrib.auth.models import User
# Create your models here.




class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    Product_Name = models.CharField(max_length=150, null=False, blank=False)
    Image = models.ImageField(upload_to="store/images", null=True)
    Product_Desc = models.TextField(max_length=2000)
    status = models.BooleanField(default=False, help_text="0=default , 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default , 1=Trending")
    meta_title = models.CharField(max_length=150)
    meta_keyword = models.CharField(max_length=150)
    meta_description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Product_Name


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    Product_Name = models.CharField(max_length=150, null=False, blank=False)
    Original_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Selling_Price = models.DecimalField(max_digits=10, decimal_places=2)

    Product_Image_Main = models.ImageField(upload_to="store/images", null=False , default="")
    Product_Image2 = models.ImageField(upload_to="store/images", null=False , default="")
    Product_Image3 = models.ImageField(upload_to="store/images", null=False , default="")
    Product_Image4 = models.ImageField(upload_to="store/images", null=False , default="")

    Product_Quantity = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=20, default="")

    Product_Small_Desc = models.CharField(max_length=250)
    Product_Desc = models.TextField(max_length=2000)

    status = models.BooleanField(default=False, help_text="0=default , 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default , 1=Trending")
    tag = models.CharField(max_length=150, null=True, blank=True)

    meta_title = models.CharField(max_length=150)
    meta_keyword = models.CharField(max_length=150)
    meta_description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Product_Name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


# below are the models of the billing address of the customer present in the database

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    address1 = models.TextField(null=False)
    address2 = models.TextField(null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=9, null=False)

    overall_total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=300, null=True)
    orderstatuses = (
        ('Pending', 'Pending'),
        ('Out For Shipping', 'Out For Shipping'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=150, choices=orderstatuses, default='Pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=180, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.PositiveIntegerField(null=False)

    def __str__(self):
        return '{} {}'.format(self.order.id, self.order.tracking_no)
    
 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=80, null=False)
    address1 = models.TextField(null=False)
    address2 = models.TextField(null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=9, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

# this class model is used to check the availablity of the pincode for delivery and COD payments
class DeliveryArea(models.Model):
    pincode = models.CharField(max_length=10, unique=True)
    cod_available = models.BooleanField(default=False)

    def __str__(self):
        return self.pincode