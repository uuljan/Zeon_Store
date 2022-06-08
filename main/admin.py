from django.contrib import admin
from .models import *

admin.site.register(Bestseller)
admin.site.register(Slider)
admin.site.register(Novelty)


from .forms import AdvantageForm
from .models import Advantage


@admin.register(Advantage)
class SectionAdmin(admin.ModelAdmin):
    list_display = 'title_advantage',
    search_fields = 'title_advantage',
    form = AdvantageForm