from django.contrib import admin
from menu_tab import models
from .forms import AdvantageForm
from .models import Slider, Advantage, Bestseller, Novelty


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('img', 'main_url')


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('image', 'title_advantage', 'description_advantage')
    form = AdvantageForm

    def has_add_permission(self, request):
        """Функция скрывает кнопку сохранения, после одного экземпляра"""

        if Advantage.objects.exists():
            return  False


admin.site.register(Bestseller)

admin.site.register(Novelty)
