from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(primary_key=True,
                              verbose_name='Email пользователя'
                              )

    def __str__(self):
        return "{}".format(self.username)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


