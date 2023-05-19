from django.contrib import admin
from .models import Product, ProductAdmin, Contact, ContactAdmin, Order, OrderAdmin, OrderUpdate, OrderUpdateAdmin

# Register your models here.
admin.site.register(
    Product,
    ProductAdmin
)
admin.site.register(
    Contact,
    ContactAdmin
)
admin.site.register(
    Order,
    OrderAdmin
)
admin.site.register(
    OrderUpdate,
    OrderUpdateAdmin
)
