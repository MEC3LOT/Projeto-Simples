from django.contrib import admin

# Register your models here.
from .models import Products, Blog, Category, Cars, Brand



#admin.site.register(Blog)
@admin.register(Products)
class Products(admin.ModelAdmin):
    # form = BlogAdminForm # Estilização do Form Blog do Admin
    list_display = ['name', 'mini_image']
    search_fields = ['name']

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    # form = BlogAdminForm # Estilização do Form Blog do Admin
    list_display = ['mini_image', 'blo_title']
    search_fields = ['blo_title']

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['cat_name', 'slug']
    search_fields = ['cat_name']

@admin.register(Brand)
class Category(admin.ModelAdmin):
    list_display = ['brand_name', 'slug']
    search_fields = ['brand_name']


@admin.register(Cars)
class Products(admin.ModelAdmin):
    # form = BlogAdminForm # Estilização do Form Blog do Admin
    list_display = ['car_name', 'mini_image','slug']
    search_fields = ['car_name']