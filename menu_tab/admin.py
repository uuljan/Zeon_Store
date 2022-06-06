from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from menu_tab.models import *


class OfferAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Offer
        fields = '__all__'

@admin.register(Offer)
class Offer(admin.ModelAdmin):
    form = OfferAdminForm

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class AboutAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = About
        fields = '__all__'

class Image_aboutInline(admin.TabularInline):
    model = Image_about
    max_num = 3

@admin.register(About)
class About(admin.ModelAdmin):
    inlines = [Image_aboutInline,]
    form = AboutAdminForm
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
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



