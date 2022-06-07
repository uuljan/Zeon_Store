from django.contrib.auth.models import User
from django.db import models


from product.models import Product


class Slider(models.Model):
    img = models.ImageField(upload_to='carusel-img')
    main_url = models.URLField(max_length=200, blank=True)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - Избранное:{}".format(self.user.username, self.product.name, self.favorite)

class Bestseller(models.Model):
    obj = models.ForeignKey(Product, related_name='best', on_delete=models.CASCADE, null=True)
    bestseller = models.BooleanField(default=False, unique=True)

    def __str__(self):
        return "{}".format(self.bestseller)

class Novelty(models.Model):
    item1 = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    novelty = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.novelty)

class Advantage(models.Model):
    image = models.ImageField(upload_to='products')
    title_advantage = models.CharField(max_length=150)
    description_advantage = models.TextField()

    def __str__(self):
        return self.title_advantage
