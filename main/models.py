from django.db import models

from account.models import User
from product.models import ImageProduct, Product


class Slider(models.Model):
    img1 = models.ImageField(upload_to='carusel-img')
    img2 = models.ImageField(upload_to='carusel-img')
    img3 = models.ImageField(upload_to='carusel-img')
    img4 = models.ImageField(upload_to='carusel-img')
    img5 = models.ImageField(upload_to='carusel-img')
    main_url = models.URLField(max_length=200, blank=True)


class ProductRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - Избранное:{}".format(self.user.username, self.product.name, self.favorite)

class Bestseller(models.Model):
    obj = models.ForeignKey(Product, related_name='best', on_delete=models.CASCADE, null=True)
    bestseller = models.BooleanField(default=False, unique=True)

    def __str__(self):
        return "{}".format(self.obj)

class Novelty(models.Model):
    # item1 = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    # novelty = models.BooleanField(default=False)
    image_new = models.ImageField(upload_to='products')
    title_new = models.CharField(max_length=50)
    price_new = models.IntegerField()
    price_with_discount_new = models.IntegerField(blank=True)
    discount_new = models.IntegerField('Скидка в процентах', blank=True, default=0)
    size_new = models.CharField(max_length=20)
    favorite_new = models.BooleanField(default=False)
    image_color = models.ManyToManyField(ImageProduct, related_name='novelty_img_color')

    def save(self, *args, **kwargs):
        '''Расчитать стоимость со скидкой'''
        self.price_with_discount_new = int(self.price_new * (100 - self.discount_new) / 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_new


class Advantage(models.Model):
    image = models.ImageField(upload_to='products')
    title_advantage = models.CharField(max_length=150)
    description_advantage = models.TextField()

    def __str__(self):
        return self.title_advantage
