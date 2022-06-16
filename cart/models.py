from django.db import models
from django.db.models.aggregates import Sum

from product.models import Product


class Cart(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    # def __str__(self):
    #     return '{}'.format(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product')
    quantity = models.IntegerField(verbose_name='Количество товаров', null=True)

    cart_cost = models.IntegerField(null=True, blank=True)
    total_cart_cost = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Детали корзины'
        verbose_name_plural = 'Детали корзины'

    # def __str__(self):
    #     return '{}'.format(self.id)

    def save(self, *args, **kwargs):
        self.cart_cost = self.product.price * self.quantity
        price = self.product.price_with_discount if self.product.price_with_discount else self.product.price
        self.total_cart_cost = price * self.quantity
        super().save(*args, **kwargs)


class CartInfo(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    lines = models.IntegerField(verbose_name='Количество линеек', null=True, blank=True)
    product_quantity = models.IntegerField(verbose_name='Количество всех товаров', null=True, blank=True)
    cost = models.IntegerField(verbose_name='Стоимость', null=True, blank=True)
    discount = models.IntegerField(verbose_name='Скидка', null=True, blank=True)
    total_cost = models.IntegerField(verbose_name='Итого к оплате', null=True, blank=True)

    class Meta:
        verbose_name = ' Информация заказа'
        verbose_name_plural = 'Информация заказа'

    def __str__(self):
        return '{}'.format(self.id)

    def save(self, *args, **kwargs):
        all_cart_items = self.cart.cartitem_set.all()
        lines = 0
        quantity = 0
        cost = 0
        total = 0
        for i in all_cart_items:
            lines += i.quantity
            quantity += i.quantity * i.product.line
            cost += i.quantity * i.product.price
            total += i.quantity * i.product.price_with_discount

        self.lines = lines
        self.product_quantity = quantity
        self.cost = cost
        self.total_cost = total
        self.discount = self.cost - self.total_cost

        super().save(*args, **kwargs)
