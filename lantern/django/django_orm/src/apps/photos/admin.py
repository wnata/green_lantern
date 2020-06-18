from django.contrib import admin
from apps.photos.models import Photo



@admin.register(Photo)
class PhotoModelAdmin(admin.ModelAdmin):
    pass