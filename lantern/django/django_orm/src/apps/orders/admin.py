from django.contrib import admin
from apps.orders.models import Order


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    pass