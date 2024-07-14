from django.db import models


class ProductManager(models.Manager):

    def available_products(self):
        products = self.filter(is_available=True)
        return products

    def available_products_in_category(self, category_name: str):
        products = self.filter(is_available=True, category__name=category_name)
        return products

