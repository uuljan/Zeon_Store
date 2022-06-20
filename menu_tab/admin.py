from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from menu_tab import models
from menu_tab.models import Offer, About, Image_about, Question, News, Footer1, Footer2, ImageQuestion


class OfferAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Offer
        fields = '__all__'


@admin.register(Offer)
class Offer(admin.ModelAdmin):
    form = OfferAdminForm
    list_display = ['title', 'description']

    def has_add_permission(self, request):
        """Функция скрывает кнопку сохранения, после одного экземпляра"""

        main = super().has_add_permission(request)
        if main and models.Offer.objects.exists():
            main = False
        return main


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
    list_display = ['title', 'description', 'get_image']

    def get_image(self, obj):
        for e in Image_about.objects.all():
            return e.image

    def has_add_permission(self, request):
        """Функция скрывает кнопку сохранения, после одного экземпляра"""

        main = super().has_add_permission(request)
        if main and models.About.objects.exists():
            main = False
        return main


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class News(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ['image', 'title', 'description']


class QuestionInline(admin.TabularInline):
    model = Question


@admin.register(ImageQuestion)
class ImageQuestion(admin.ModelAdmin):
    inlines = [QuestionInline, ]

    def has_add_permission(self, request):
        """Функция скрывает кнопку сохранения, после одного экземпляра"""

        main = super().has_add_permission(request)
        if main and models.ImageQuestion.objects.exists():
            main = False
        return main


@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ['question', 'reply']


@admin.register(Footer1)
class Footer1(admin.ModelAdmin):
    list_display = ['id', 'header_logo', 'footer_logo', 'text', 'header_contact']

    def has_add_permission(self, request):
        """Функция скрывает кнопку сохранения, после одного экземпляра"""

        main = super().has_add_permission(request)
        if main and models.Footer1.objects.exists():
            main = False
        return main


@admin.register(Footer2)
class Footer2(admin.ModelAdmin):
    list_display = ['id', 'contact_number', 'mail', 'instagram',
                    'telegram', 'whatsapp']

    def has_add_permission(self, request):
        """Функция скрывает кнопку сохранения, после одного экземпляра"""

        main = super().has_add_permission(request)
        if main and models.Footer2.objects.exists():
            main = False
        return main
