from django.db import models

from product.models import ImageProduct, Collection, Product


class Slider(models.Model):
    img1 = models.ImageField(upload_to='carusel-img')
    img2 = models.ImageField(upload_to='carusel-img')
    img3 = models.ImageField(upload_to='carusel-img')
    img4 = models.ImageField(upload_to='carusel-img')
    img5 = models.ImageField(upload_to='carusel-img')
    main_url = models.URLField(max_length=200, blank=True)


class Bestseller(models.Model):
    collection = models.ForeignKey(Collection, related_name='product', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    price_with_discount = models.IntegerField(blank=True)
    discount = models.IntegerField('Скидка в процентах', blank=True, default=0)
    size = models.CharField(max_length=20)
    favorite = models.BooleanField(default=False)
    image_color = models.ManyToManyField(ImageProduct, related_name='bestseller_img_color')

    class Meta:
        ordering = ('title',)

    def save(self, *args, **kwargs):
        '''Расчитать стоимость со скидкой'''
        self.price_with_discount = int(self.price * (100 - self.discount) / 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


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
