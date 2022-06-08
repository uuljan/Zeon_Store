from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class MyCallback(models.Model):
    STATUS = [
        ('YES', 'ДА'),
        ('NO', 'НЕТ'),
    ]
    call_status = models.CharField(choices=STATUS, max_length=20, default='NO', verbose_name="Статус позвонили")
    name = models.CharField(max_length=120, verbose_name="Имя")
    number = PhoneNumberField(null=False, verbose_name="Номер телефона")
    type_of_appeal = models.CharField(max_length=55, default='Обратный звонок', verbose_name="Тип обращения")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "Имя: {} - Номер телефона: {} - Дата обращения: {} - " \
               "Тип обращения: {}".format(self.name, self.number, self.timestamp, self.type_of_appeal)
