from django import forms
from django.contrib import admin
from .models import *


@admin.register(MyCallback)
class MyCallback(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {
            'number': forms.TextInput(attrs={'placeholder': '+996771234567'})
        }
        return super().get_form(request, obj, **kwargs)
