from django.contrib import admin
from .models import MediaItem


@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'date_added')
    list_filter = ('media_type', 'date_added')
    search_fields = ('title', 'description')
    ordering = ('-date_added',)