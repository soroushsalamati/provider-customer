from django.db import models
from provider.models import Provider


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Name",
        help_text="Enter the name of the product."
    )
    description = models.TextField(
        verbose_name="Description",
        help_text="Enter the description of the product."
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price",
        help_text="Enter the price of the product."
    )
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        verbose_name="Provider",
        help_text="Select the provider of the product."
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
