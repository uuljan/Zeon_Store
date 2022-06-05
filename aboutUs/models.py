from django.db import models


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
