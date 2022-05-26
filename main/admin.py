from django.contrib import admin
from .models import Bestseller
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProductAdminForm(forms.ModelForm):
    color = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Bestseller
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = ProductAdminForm

admin.site.register(Bestseller, PostAdmin)