from django.contrib import admin
from .models import Image, Place


class PlaceImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
    list_display = (
        'title', 
        'lng', 
        'lat',
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'place_title',
    )


    def place_title(self, obj):
        return obj.place.title
