from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.exceptions import ValidationError


class Offer(models.Model):
    '''модель Публичная оферта'''

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Публичная оферта'
        verbose_name_plural = 'Публичная оферта'

    def __str__(self):
        return "{} - {}".format(self.title, self.description)


class About(models.Model):
    '''модель О нас'''

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return "{} - {}".format(self.title, self.description)


class Image_about(models.Model):
    '''модель Изображение О нас'''

    obj = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products', verbose_name='Картинки для О нас')

    def __str__(self):
        return "{}".format(self.image)


class News(models.Model):
    '''модель Новости'''

    image = models.ImageField(upload_to='tab_img', verbose_name='Фотография')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return "{} - {} - {}".format(self.title, self.description, self.image)


class ImageQuestion(models.Model):
    '''модель Помощь/Изображение'''

    image = models.ImageField(upload_to='tab_images', null=True, blank=True, verbose_name='Изображение')

    def save(self, *args, **kwargs):
        if ImageQuestion.objects.exists() and not self.pk:
            raise ValidationError('Экземпляр уже создан')
        return super(ImageQuestion, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Помощь/Изображение'
        verbose_name_plural = 'Помощь/Изображение'

    def __str__(self):
        return "{}".format(self.image)


class Question(models.Model):
    '''модель Помощь'''

    Image_question = models.ForeignKey(ImageQuestion, on_delete=models.CASCADE, null=True,
                                       verbose_name='Помощь/Изображение',
                                       related_name='questions')
    question = models.CharField(max_length=250, verbose_name='Вопрос')
    reply = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return "{} - {}".format(self.question, self.reply)

    class Meta:
        verbose_name = 'Вопрос/Ответ'
        verbose_name_plural = 'Вопрос/Ответ'

class Footer1(models.Model):
    '''модель Футер, первая вкладка'''
    header_logo = models.ImageField(upload_to='Logo-img', verbose_name='Хедер лого')
    footer_logo = models.ImageField(upload_to='Logo-img', verbose_name='Футер лого')
    text = models.CharField(max_length=255)
    header_contact = PhoneNumberField(null=False, verbose_name='Хедер контакт')
    class Meta:
        verbose_name = 'Футер1'
        verbose_name_plural = 'Футер1'

class Footer2(models.Model):
    '''модель Футер, вторая вкладка'''
    contact_number = models.CharField(max_length=155, verbose_name='Контакты')
    mail = models.CharField(max_length=80, verbose_name='Почта')
    instagram = models.CharField(max_length=100, verbose_name='Инстаграм')
    telegram = models.CharField(max_length=80, verbose_name='Телеграм')
    whatsapp = models.CharField(max_length=80, verbose_name='Ватсапп')

    objects = models.Manager()

    class Meta:
        verbose_name = 'Футер2'
        verbose_name_plural = 'Футер2'

    def save(self, *args, **kwargs):
        self.mail = f'https://mail.google.com/'
        self.instagram = f'https://www.instagram.com/{self.instagram}'
        self.telegram = f'https://t.me/{self.telegram}'
        self.whatsapp = f'https://api.whatsapp.com/send?phone={self.whatsapp}'
        super(Footer2, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.mail, self.instagram, self.telegram, self.whatsapp)
