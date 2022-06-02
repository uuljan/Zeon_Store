from django.db import models
from colorfield.fields import ColorField

# from main.models import Collection


class ImageProduct(models.Model):
    image = models.ImageField(upload_to='products')
    COLOR_PALETTE = [
        ('#BED5D2', '#BED5D2'),
        ('#D6EEC4', '#D6EEC4'),
        ('#002B73', '#002B73'),
        ('#AC8549', '#AC8549'),
        ('#BAC0F8', '#BAC0F8'),
        ('#FDFDFD', '#FDFDFD'),
        ('#D3D3D2', '#D3D3D2'),
        ('#FF8888', '#FF8888'),
    ]
    color = ColorField(choices=COLOR_PALETTE, default='#BED5D2', unique=True)

    def __str__(self):
        return self.color

class Product(models.Model):
    # collection = models.ForeignKey(Collection, related_name='coll', on_delete=models.CASCADE)
    image_color = models.ManyToManyField(ImageProduct, related_name='image_color')
    name = models.CharField(max_length=150, unique=True, null=False, blank=False)
    vendor = models.CharField(max_length=150, unique=True, null=False, blank=False)
    price = models.IntegerField()
    price_with_discount = models.IntegerField(blank=True)
    discount = models.IntegerField('Скидка в процентах', blank=True, default=0)
    description = models.TextField()
    size_range = models.CharField(max_length=150, default='42-50', blank=True)
    structure = models.CharField(max_length=150)
    line = models.IntegerField('Количество в линейке', default=5)
    fabric = models.CharField(max_length=150)
    bestseller = models.BooleanField(default=False)
    novelty = models.BooleanField(default=True)
    favorite = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        '''Стоимость со скидкой'''
        self.price_with_discount = int(self.price * (100 - self.discount) / 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

