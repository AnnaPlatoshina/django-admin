
from django.contrib import admin
from .models import Workplace

@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    """Админка для рабочих мест"""
    list_display = ('desk_number', 'employee', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('desk_number', 'employee__username', 'employee__first_name', 'employee__last_name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('desk_number', 'employee', 'additional_info')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )