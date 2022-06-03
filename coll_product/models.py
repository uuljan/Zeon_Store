from django.db import models

from product.models import Product


class Coll_product(models.Model):
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{}".format(self.item)
