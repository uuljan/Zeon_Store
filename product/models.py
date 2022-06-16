from django.db import models
from colorfield.fields import ColorField

class Collection(models.Model):
    """Коллекция товаров"""
    slug = models.SlugField(max_length=100, primary_key=True, blank=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    image_collection = models.ImageField(upload_to='products', verbose_name='Фотография')

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель Товар"""
    collection = models.ForeignKey(Collection, related_name='coll', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    vendor = models.CharField(max_length=150, unique=True, verbose_name='Артикул')
    price = models.IntegerField(verbose_name='Цена')
    price_with_discount = models.IntegerField(null=True, blank=True, verbose_name='Цена со скидкой')
    discount = models.IntegerField(null=True, blank=True, default=0, verbose_name='Процент скидки')
    description = models.TextField(verbose_name='Описание')
    size_range = models.CharField(max_length=150, default='42-50', blank=True, verbose_name='Размерный ряд')
    structure = models.CharField(max_length=150, verbose_name='Состав ткани')
    line = models.IntegerField(default=5, verbose_name='Количество в линейке')
    fabric = models.CharField(max_length=150, verbose_name='Материал')

    def save(self, *args, **kwargs):
        '''Стоимость со скидкой'''

        self.price_with_discount = int(self.price * (100 - self.discount) / 100)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return "{}".format(self.name)


class ImageProduct(models.Model):
    """Фотографии и цвет товара"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image_color')
    image = models.ImageField(upload_to='products', verbose_name='Фотография')
    COLOR_PALETTE = [
        ("#BED5D2", "#BED5D2",),
        ("#D6EEC4", "#D6EEC4",),
        ("#002B73", "#002B73",),
        ("#AC8549", "#AC8549",),
        ("#BAC0F8", "#BAC0F8",),
        ("#FDFDFD", "#FDFDFD",),
        ("#D3D3D2", "#D3D3D2",),
        ("#FF8888", "#FF8888",),
    ]
    color = ColorField(samples=COLOR_PALETTE)

    def __str__(self):
        return "color: {} - image: {}".format(self.color, self.image)


class Favorite(models.Model):
    """Избранные товары"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    favorite = models.BooleanField(default=False, verbose_name='Избранное')
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name='Количество избранных товаров')

    def save(self, *args, **kwargs):
        '''Количество всех товаров в избранных'''
        self.quantity = Favorite.objects.all().count()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return "{} - Избранное:{}".format(self.product.name, self.favorite)
