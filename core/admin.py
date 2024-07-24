from django.contrib import admin

# Register your models here.
from .models import Products, Blog

admin.site.register(Products)


#admin.site.register(Blog)
@admin.register(Blog)
class Blog(admin.ModelAdmin):
    # form = BlogAdminForm # Estilização do Form Blog do Admin
    list_display = ['mini_image', 'blo_title']
    search_fields = ['blo_title']