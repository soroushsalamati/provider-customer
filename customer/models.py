from django.db import models
from product.models import Product

class Customer(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="First Name",
        help_text="Enter the first name of the customer."
    )
    phone_number = models.CharField(
        max_length=11,
        verbose_name="Phone Number",
        help_text="Enter the phone number of the customer."
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Product",
        help_text="Select the product purchased by the customer."
    )
    wallet = models.FloatField(
        verbose_name="Wallet",
        help_text="Enter the wallet amount of the customer."
    )

    def __str__(self) -> str:
        return self.first_name
    
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"