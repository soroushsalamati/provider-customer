from django.contrib.admin import register, ModelAdmin
from product.models import Product


@register(Product)
class ProductAdmin(ModelAdmin):
    pass
