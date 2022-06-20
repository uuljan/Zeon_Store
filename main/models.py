from django.db import models
from product.models import Product


class Slider(models.Model):
    """Слайдер главная страница"""

    img = models.ImageField(upload_to='carusel-img',
                            verbose_name="Фотография"
                            )
    main_url = models.URLField(max_length=200, blank=True,
                               verbose_name='Ссылка'
                               )

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'

    def __str__(self):
        return "{} - {}".format(self.img, self.main_url)


class Advantage(models.Model):
    """Модель Наши преимущества"""

    image = models.ImageField(upload_to='products',
                              verbose_name='Иконка'
                              )
    title_advantage = models.CharField(max_length=150,
                                       verbose_name='Заголовок'
                                       )
    description_advantage = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Наши преимущества'
        verbose_name_plural = 'Наши преимущества'

    def __str__(self):
        return "{} - {} - {}".format(self.image,
                                     self.title_advantage,
                                     self.description_advantage)


class Bestseller(models.Model):
    """Модель Хит продаж"""

    obj = models.ForeignKey(Product, related_name='best',
                            on_delete=models.CASCADE, null=True)
    bestseller = models.BooleanField(default=False,
                                     verbose_name='Хит продаж')

    class Meta:
        verbose_name = 'Хит продаж'
        verbose_name_plural = 'Хиты продаж'

    def __str__(self):
        return "{}".format(self.bestseller)


class Novelty(models.Model):
    """Модель Новинки"""

    item1 = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    novelty = models.BooleanField(default=False, verbose_name='Новинка')

    class Meta:
        verbose_name = 'Новинка'
        verbose_name_plural = 'Новинки'

    def __str__(self):
        return "{}".format(self.novelty)
