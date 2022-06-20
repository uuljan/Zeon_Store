from django.contrib import admin

from . import models
from .forms import AdvantageForm
from .models import Slider, Advantage, Bestseller, Novelty


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('img', 'main_url')


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('image', 'title_advantage', 'description_advantage')
    form = AdvantageForm


@admin.register(Bestseller)
class BestsellerAdmin(admin.ModelAdmin):
    list_display = ('obj', 'bestseller')


@admin.register(Novelty)
class NoveltyAdmin(admin.ModelAdmin):
    list_display = ('item1', 'novelty')
