from django.contrib import admin

# Register your models here.
from .models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand')


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'title', 'comments')


admin.site.register(Review, ReviewAdmin)
