from django.db import models
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
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True, blank=True)
    price_with_discount = models.IntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    line = models.IntegerField(verbose_name='Количество линеек', null=True, blank=True)
    product_quantity = models.IntegerField(verbose_name='Количество товаров', null=True, blank=True)
    cost = models.IntegerField(verbose_name='Стоимость', null=True, blank=True)
    discount = models.IntegerField(verbose_name='Скидки', null=True)
    total_cost = models.IntegerField(verbose_name='Итого к оплате', null=True)
    def __str__(self):
        return "{} - :{}".format(self.product.name, self.product.price)

    def save(self, *args, **kwargs):
        self.price = self.product.price
        self.price_with_discount = self.product.price_with_discount
        super().save(*args, **kwargs)






