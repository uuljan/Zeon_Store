from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import About, Image_about

class AboutAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = About
        fields = '__all__'
#
class Image_aboutInline(admin.TabularInline):
    model = Image_about
    max_num = 3

@admin.register(About)
class About(admin.ModelAdmin):
    inlines = [Image_aboutInline,]
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
