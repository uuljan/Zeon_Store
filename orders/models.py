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
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    line = models.IntegerField(verbose_name='Количество линеек', null=True, blank=True)
    product_quantity = models.IntegerField(verbose_name='Количество товаров', null=True, blank=True)
    cost = models.IntegerField(verbose_name='Стоимость', null=True, blank=True)
    # discount = models.IntegerField(verbose_name='Скидки', null=True)
    # total = models.IntegerField(verbose_name='Итого к оплате', null=True)

    def save(self, *args, **kwargs):
        self.line = int(self.quantity * 5)
        self.product_quantity = int(self.quantity * 5)
        self.cost = int(self.product_quantity * self.line)
        # self.discount = int(self.product_quantity * self.line)
        # self.total = int(self.cost - self.discount)
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity



