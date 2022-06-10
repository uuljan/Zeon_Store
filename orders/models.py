from django.db import models

from mycart.models import Cart
from product.models import Product
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    ORDER_STATUS = [
        ('NEW', 'НОВЫЙ'),
        ('ISSUED', 'ОФОРМЛЕН'),
        ('CANCELED', 'ОТМЕНЕН'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    number = PhoneNumberField(verbose_name="Номер телефона", null=True)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=55, choices=ORDER_STATUS, default='NEW')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE, null=True)
    line = models.IntegerField(verbose_name='Количество линеек', null=True, blank=True)
    product_quantity = models.IntegerField(verbose_name='Количество товаров', null=True, blank=True)
    cost = models.IntegerField(verbose_name='Стоимость', null=True, blank=True)
    discount = models.IntegerField(verbose_name='Скидки', null=True, blank=True)
    total_cost = models.IntegerField(verbose_name='Итого к оплате', null=True, blank=True)

    # def __str__(self):
    # return "{} - :{}".format(self.product.name, self.product.price)

    # for e in Product.objects.all():
    #     p = e.price
    # for item in Cart.objects.all():
    #     q = item.quantity

    # def save(self, *args, **kwargs):
    #
    #     # self.line = .objects.aggregate(total_likes=Sum('tt_like'))
    #     self.product_quantity = self.line * 5
    #     self.cost = self.cart.quantity * self.p * self.product_quantity
    #     # self.price_with_discount = self.product.price_with_discount
    #     # self.quantity = self.cart.quantity
    #     super().save(*args, **kwargs)
