from django.contrib import admin
from .models import Image, Place
from django.utils.html import format_html


class PlaceImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image', 'get_preview', 'position')
    readonly_fields = ('get_preview',)


    @admin.display(description="Предпросотр")
    def get_preview(self, obj):
        return format_html(
            '<img src="{}" style="max-height:200px; width:auto;" />',
            obj.image.url,
        )


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
        'place_title',
        'get_preview',
        'position'
    )
    readonly_fields = ('get_preview',)


    @admin.display(description="Предпросотр")
    def get_preview(self, obj):
        return format_html(
            '<img src="{}" style="max-height:200px; width:auto;" />',
            obj.image.url,
        )


    @admin.display(description="Место")
    def place_title(self, obj):
        return obj.place.title
