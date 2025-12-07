from django.contrib import admin
from .models import Image, Place
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline, SortableAdminBase


@admin.display(description="Предпросмотр")
def get_preview(self, obj):
    if not obj.pk or not obj.image:
        return 'Нет изображения'
    return format_html(
        '<img src="{}" style="max-height:200px; width:auto;" />',
        obj.image.url,
    )


class PlaceImageInline(SortableStackedInline):
    model = Image
    extra = 1
    fields = ('image', 'preview', 'position')
    readonly_fields = ('preview',)

    preview = get_preview


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [PlaceImageInline]
    list_display = (
        'title', 
        'lng', 
        'lat',
    )


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        'place_title',
        'preview',
        'position'
    )
    readonly_fields = ('preview',)

    preview = get_preview


    @admin.display(description="Место")
    def place_title(self, obj):
        return obj.place.title
