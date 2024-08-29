from django.contrib.admin import register, ModelAdmin
from customer.models import Customer


@register(Customer)
class CustomerAdmin(ModelAdmin):
    pass
