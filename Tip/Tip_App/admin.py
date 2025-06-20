from django.contrib import admin
from django.utils.html import format_html
from .models import Waiter

@admin.register(Waiter)

class WaiterAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'contact_number', 'email', 'joined_date', 'total_tips_received', 'photo_tag')
    search_fields = ('name', 'email', 'contact_number')
    list_filter = ('gender', 'joined_date')
    readonly_fields = ('photo_tag', 'joined_date')
    fieldsets = (
        (None, {
            'fields': ('name', 'gender', 'photo', 'photo_tag')
        }),
        ('Contact Information', {
            'fields': ('contact_number', 'email')
        }),
        ('Other Info', {
            'fields': ('joined_date', 'total_tips_received')
        }),
    )

    def photo_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="80" height="80" style="object-fit: cover; border-radius: 8px;" />', obj.photo.url)
        return "No Photo"
    
    photo_tag.short_description = 'Preview'
