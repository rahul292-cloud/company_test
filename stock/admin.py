from django.contrib import admin
from .models import Tag,Category,Product, Customer


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    search_fields = ('category_name',)
    list_filter = ('category_name',)

admin.site.register(Customer)
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    model=Product
    search_fields = ('category_name','product_name',)
    list_filter = ('category_name','product_name',)
    # list_display = ('product_name','category_name',)

admin.site.register(Product,ProductAdmin)


admin.site.register(Tag)
