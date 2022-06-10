from django.contrib import admin

from .models import Cart


@admin.register(Cart)
class Cart(admin.ModelAdmin):
    pass