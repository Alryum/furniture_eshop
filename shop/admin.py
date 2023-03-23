from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Furniture


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'size', 'producer',)
    list_display_links = ('name',)
    fields = ('name', 'image', 'description', 'price', 'size', 'producer',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')

    get_image.short_description = 'Фото'


admin.site.register(Furniture, ProductAdmin)
