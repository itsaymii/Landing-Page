from django.contrib import admin
from .models import Category, Product, Review, Customer, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_available', 'created_at']
    list_filter = ['category', 'is_available', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['price', 'stock', 'is_available']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'product', 'rating', 'date_added']
    list_filter = ['rating', 'date_added']
    search_fields = ['customer_name', 'product__name', 'comment']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'date_joined']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['date_joined']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'quantity', 'total_price', 'status', 'order_date']
    list_filter = ['status', 'order_date']
    search_fields = ['customer__first_name', 'customer__last_name', 'product__name']
    list_editable = ['status']
