from django.db import models
from main.models import Product

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=False)


    def __str__(self):
        return "{} - {} - {} - {}- {}".format(self.product.name,
                                          self.product.size_range,
                                          self.product.price,
                                          self.product.price_with_discount,
                                          self.product.line
                                          )