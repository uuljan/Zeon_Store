from django.db import models
from product.models import Product
from phonenumber_field.modelfields import PhoneNumberField

from users.models import User


class Order(models.Model):
    """Модель оформление заказа"""

    ORDER_STATUS = [
        ('NEW', 'НОВЫЙ'),
        ('ISSUED', 'ОФОРМЛЕН'),
        ('CANCELED', 'ОТМЕНЕН'),
    ]
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                             related_name='orders',
                             verbose_name="Пользователь"
                             )
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Почта")
    number = PhoneNumberField(verbose_name="Номер телефона", null=True)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=55,
                                    choices=ORDER_STATUS, default='NEW'
                                    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ {}'.format(self.id)


class OrderItem(models.Model):
    """Модель детали заказа"""

    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              null=True, blank=True
                              )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количество товаров',
                                   null=True
                                   )

    order_cost = models.IntegerField(null=True, blank=True)
    total_cost = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детали заказа'

    def __str__(self):
        return 'Детали заказа {}'.format(self.id)

    def save(self, *args, **kwargs):
        self.order_cost = self.product.price * self.quantity
        price = self.product.price_with_discount \
            if self.product.price_with_discount \
            else self.product.price
        self.total_cost = price * self.quantity
        super().save(*args, **kwargs)


class OrderInfo(models.Model):
    """Модель детали товаров заказа"""

    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              null=True, blank=True
                              )
    lines = models.IntegerField(verbose_name='Количество линеек',
                                null=True, blank=True
                                )
    product_quantity = models.IntegerField(verbose_name='Количество '
                                                        'всех товаров',
                                           null=True, blank=True
                                           )
    cost = models.IntegerField(verbose_name='Стоимость',
                               null=True, blank=True
                               )
    discount = models.IntegerField(verbose_name='Скидка',
                                   null=True, blank=True
                                   )
    total_cost = models.IntegerField(verbose_name='Итого к оплате',
                                     null=True, blank=True
                                     )

    class Meta:
        verbose_name = ' Информация заказа'
        verbose_name_plural = 'Информация заказа'

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    def save(self, *args, **kwargs):
        all_order_items = self.order.orderitem_set.all()
        lines = 0
        quantity = 0
        cost = 0
        total = 0
        for i in all_order_items:
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
