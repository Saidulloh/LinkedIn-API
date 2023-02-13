from django.contrib import admin

from apps.premium.models import Premium, PremiumOrder


@admin.register(Premium)
class PremiumAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'date_during',)


@admin.register(PremiumOrder)
class PremiumOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', )
