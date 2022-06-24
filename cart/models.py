from django.db import models

from product.models import Product
from users.models import User


class Cart(models.Model):
    """Модель корзины"""

    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE,
                             verbose_name="Владелец"
                             )
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='cart_product'
                                )
    quantity = models.IntegerField(verbose_name='Количество товаров',
                                   null=True
                                   )
    cart_cost = models.IntegerField(null=True, blank=True)
    total_cart_cost = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return 'Корзина {}'.format(self.id)

    def save(self, *args, **kwargs):
        self.cart_cost = self.product.price * self.quantity
        price = self.product.price_with_discount \
            if self.product.price_with_discount \
            else self.product.price
        self.total_cart_cost = price * self.quantity
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return 'Корзина клиента: {}'.format(self.user)


class CartInfo(models.Model):
    """Модель детали товаров корзины"""

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
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
        verbose_name = 'Детали корзины'
        verbose_name_plural = 'Детали корзины'

    def __str__(self):
        return 'Корзина {}'.format(self.id)

    def save(self, *args, **kwargs):
        """функция для вычета общего количества и
           стоимости товаров в корзине"""

        all_cart_items = Cart.objects.all()
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
