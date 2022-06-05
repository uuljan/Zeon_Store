from django.db import models
from rest_framework.exceptions import ValidationError

class Offer(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name = 'Публичная оферта'
        verbose_name_plural = 'Публичная оферта'

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    def save(self, *args, **kwargs):
        if About.objects.exists() and not self.pk:
            raise ValidationError('Экземпляр уже создан')
        return super(About, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title

class Image_about(models.Model):
    obj = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products')
