from django.db import models
from django.forms import ModelForm
from phonenumber_field.modelfields import PhoneNumberField

class Callback(models.Model):
    name = models.CharField(max_length=120, unique=False, verbose_name="Имя")
    phone = PhoneNumberField(null=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id", "-timestamp"]
