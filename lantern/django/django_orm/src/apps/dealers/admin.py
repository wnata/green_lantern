from django.contrib import admin

from django.utils.safestring import mark_safe
from apps.dealers.models import Country, City, Dealer


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(City)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('user',)
