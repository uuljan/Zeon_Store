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




class News(models.Model):
    image = models.ImageField(upload_to='tab_img')
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    #
    def __str__(self):
        return self.title




class Question(models.Model):
    question = models.CharField('Вопрос', max_length=250)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question

class Reply(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='replies')
    reply = models.TextField('Ответ')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class ImageQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='tab_images', null=True, blank=True)

    def save(self, *args, **kwargs):
        if ImageQuestion.objects.exists() and not self.pk:
            raise ValidationError('Экземпляр уже создан')
        return super(ImageQuestion, self).save(*args, **kwargs)
