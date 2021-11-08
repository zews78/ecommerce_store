from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced,
    Reviews
)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','selling_price','discounted_price','description','genre','category','image']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']


@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','customerinfo','product','productinfo','quantity','ordered_date','status']

    def customerinfo(self,obj):
        link=reverse("admin:app_customer_change",args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link,obj.customer.name)
    
    def productinfo(self,obj):
        link=reverse("admin:app_product_change",args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link,obj.product.name)

admin.site.register(Reviews)