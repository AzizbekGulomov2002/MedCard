from django.contrib import admin
from .models import MedCard, Logo


class MedCardAdmin(admin.ModelAdmin):
    list_display = [
        "dori_nomi",
        "narx",
    ]
    list_per_page = 10
    class Meta:
        model = MedCard
admin.site.register(MedCard, MedCardAdmin)



admin.site.register(Logo)