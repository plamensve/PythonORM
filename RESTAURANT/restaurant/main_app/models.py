from datetime import timezone

from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    orders = models.ManyToManyField(Menu, through='Order')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"Order by {self.client} for {self.menu} on {self.date_time}"
