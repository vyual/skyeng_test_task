from datetime import date, timedelta

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def orders_last_month(self):
        last_month_start = date.today().replace(day=1) - timedelta(days=1)
        last_month_end = last_month_start.replace(day=1)
        return self.order_set.filter(created_at__range=[last_month_start, last_month_end]).count()

    def orders_current_month(self):
        today = date.today()
        current_month_start = today.replace(day=1)
        return self.order_set.filter(created_at__gte=current_month_start).count()

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ManyToManyField(Product, through='OrderProduct')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
