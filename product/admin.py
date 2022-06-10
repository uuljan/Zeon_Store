from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from main.models import Bestseller, Novelty
from .models import *

class BestsellerInline(admin.TabularInline):
    model = Bestseller
    max_num = 1

class NoveltyInline(admin.TabularInline):
    model = Novelty
    max_num = 1

class ImageProductInline(admin.TabularInline):
    model = ImageProduct
    max_num = 8

class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        exclude = ('favorite',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageProductInline, BestsellerInline, NoveltyInline ]
    form = ProductAdminForm


admin.site.register(Collection)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['favorite', 'product']
