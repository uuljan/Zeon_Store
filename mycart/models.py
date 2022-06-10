from django.db import models
from django.db.models.aggregates import Sum

from main.models import Product

class Cart(models.Model):
    """tset"""
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=False)

    line = models.IntegerField(verbose_name='Количество линеек', null=True, blank=True)
    product_quantity = models.IntegerField(verbose_name='Количество товаров', null=True, blank=True)
    cost = models.IntegerField(verbose_name='Стоимость', null=True, blank=True)
    discount = models.IntegerField(verbose_name='Скидки', null=True, blank=True)
    total_cost = models.IntegerField(verbose_name='Итого к оплате', null=True, blank=True)

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        self.line = Cart.objects.aggregate(Sum('quantity'))
        # self.product_quantity = self.line * 5
        # self.cost = self.cart.quantity * self.p * self.product_quantity
        # # self.price_with_discount = self.product.price_with_discount
        # # self.quantity = self.cart.quantity
        # super().save(*args, **kwargs)