from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from menu_tab import models
from menu_tab.models import Offer, About, Image_about, Question, Reply, News, Footer


class OfferAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Offer
        fields = '__all__'


@admin.register(Offer)
class Offer(admin.ModelAdmin):
    form = OfferAdminForm

    def has_add_permission(self, request):
        retVal = super().has_add_permission(request)
        if retVal and models.Offer.objects.exists():
            retVal = False
        return retVal


class AboutAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = About
        fields = '__all__'


class Image_aboutInline(admin.TabularInline):
    model = Image_about
    max_num = 3


@admin.register(About)
class About(admin.ModelAdmin):
    inlines = [Image_aboutInline, ]
    form = AboutAdminForm

    def has_add_permission(self, request):
        retVal = super().has_add_permission(request)
        if retVal and models.About.objects.exists():
            retVal = False
        return retVal


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class News(admin.ModelAdmin):
    form = NewsAdminForm


class ReplyInline(admin.TabularInline):
    model = Reply
    max_num = 1


@admin.register(Question)
class Question(admin.ModelAdmin):
    inlines = [ReplyInline, ]


@admin.register(Footer)
class Footer(admin.ModelAdmin):

    def has_add_permission(self, request):
        retVal = super().has_add_permission(request)
        if retVal and models.Footer.objects.exists():
            retVal = False
        return retVal
