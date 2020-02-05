from django.contrib import admin
from .models import (Product, Category, Cart, Order)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('gender_choice', 'slug')
    prepopulated_fields = {'slug':('gender_choice',)}

admin.site.register(Category, CategoryAdmin)

admin.site.register(Cart)
admin.site.register(Order)


admin.site.register(Product)
