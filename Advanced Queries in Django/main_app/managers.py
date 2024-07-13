from django.db import models


class ProductManager(models.Manager):
    def available_products(self):
        product_available = self.filter(is_available=True)
        return product_available

    def available_products_in_category(self, category_name: str):
        product_in_category_is_available = self.filter(is_available=True, category__name=category_name)
        return product_in_category_is_available


