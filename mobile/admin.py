from django.contrib import admin
from .models import category ,products

# Register your models here.

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display=("id","name","description","icon")

@admin.register(products)
class productsAdmin(admin.ModelAdmin):
    list_display=("id","name","brand","price","category","storage","color")