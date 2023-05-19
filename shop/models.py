from django.db import models
from django.contrib import admin


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    desc = models.CharField(max_length=1500)
    price = models.IntegerField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images')

    def __str__(self):
        return self.product_name

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_id",
        "product_name",
        "category",
        "subcategory",
        "desc",
        "price",
        "pub_date"
    )

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    dateAdded = models.DateField()

    def __str__(self):
        return self.name

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "msg_id",
        "name",
        "email",
        "phone",
        "desc",
        "dateAdded"
    )

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=10000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.IntegerField()
    phone = models.IntegerField()
    dateAdded = models.DateField()

    def __str__(self) -> str:
        return self.name
    
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_id",
        "name",
        "email",
        "address1",
        "address2",
        "city",
        "state",
        "zip_code",
        "phone",
        "dateAdded"
    )


class OrderUpdate(models.Model):
    updateId = models.AutoField(primary_key=True)
    orderId = models.IntegerField(default=0)
    updateDesc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.updateDesc[0:7] + '...'


class OrderUpdateAdmin(admin.ModelAdmin):
    list_display = (
        "updateId",
        "orderId",
        "updateDesc",
        "timestamp"
    )