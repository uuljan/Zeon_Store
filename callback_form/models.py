from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MyCallback(models.Model):
    """Модель Обратный звонок"""

    STATUS = [
        ('YES', 'ДА'),
        ('NO', 'НЕТ'),
    ]
    call_status = models.CharField(choices=STATUS, max_length=20, default='NO', verbose_name="Статус позвонили")
    name = models.CharField(max_length=120, verbose_name="Имя")
    number = PhoneNumberField(null=False, verbose_name="Номер телефона")
    type_of_appeal = models.CharField(max_length=55, default='Обратный звонок', verbose_name="Тип обращения")
    time = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратный звонок'

    def __str__(self):
        return "Имя: {} - Номер телефона: {} - Дата обращения: {} - " \
               "Тип обращения: {}".format(self.name, self.number, self.time, self.type_of_appeal)
