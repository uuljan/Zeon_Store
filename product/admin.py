from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import *


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        exclude = ('favorite',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm


admin.site.register(ImageProduct)


admin.site.register(Collection)