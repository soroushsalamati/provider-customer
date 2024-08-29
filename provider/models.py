from django.db import models
from product.models import Product

class Provider(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name="First Name",
        help_text="Enter the first name of the Provider."
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Last Name",
        help_text="Enter the last name of the Provider."
    )
    phone_number = models.CharField(
        max_length=11,
        verbose_name="Phone Number",
        help_text="Enter the phone number of the Provider."
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Product",
        help_text="Select the product provided by the Provider."
    )

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"
