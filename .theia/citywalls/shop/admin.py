from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','artist']
    prepopulated_fields = {'artist':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'artist':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)
