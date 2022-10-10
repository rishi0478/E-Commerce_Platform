from django.contrib import admin
from .models import ProductItem,Product_details,AddToCart
# Register your models here.

admin.site.register(AddToCart)

@admin.register(ProductItem)
class ProductItem_Admin(admin.ModelAdmin):
    list_display = ['product']

@admin.register(Product_details)
class Product_Admin(admin.ModelAdmin):
    list_display = ['product_name','product_title','slug','product_price','on_sale','sale_price']

