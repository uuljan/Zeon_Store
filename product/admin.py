from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from main.models import Bestseller, Novelty
from .models import *


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_collection']


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
    description = forms.CharField(label='Описание',
                                  widget=CKEditorUploadingWidget()
                                  )

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageProductInline, BestsellerInline, NoveltyInline]
    form = ProductAdminForm
    list_display = ['id', 'collection', 'name', 'vendor', 'price',
                    'price_with_discount', 'discount', 'description',
                    'size_range',
                    'structure', 'line', 'fabric', 'bestseller', 'novelty']

    def bestseller(self, obj):
        for e in Bestseller.objects.all():
            return e.bestseller

    def novelty(self, obj):
        for e in Novelty.objects.all():
            return e.novelty


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['id', 'favorite', 'product', 'quantity', 'user']
