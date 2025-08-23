from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Skill, EmployeeSkill


class EmployeeSkillInline(admin.TabularInline):
    """Inline для отображения навыков сотрудника"""
    model = EmployeeSkill
    extra = 1
    fields = ['skill', 'level', 'experience_years', 'last_used']
    autocomplete_fields = ['skill']


class CustomUserAdmin(UserAdmin):
    """Админка для сотрудников с расширенными полями"""

    list_display = [
        'username', 'email', 'get_full_name', 'position',
        'department', 'is_active_employee', 'is_staff'
    ]

    list_filter = [
        'gender', 'is_staff', 'is_superuser', 'is_active',
        'is_active_employee', 'department', 'hire_date'
    ]

    search_fields = [
        'username', 'email', 'first_name', 'last_name',
        'middle_name', 'position', 'department'
    ]

    ordering = ['last_name', 'first_name']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Персональная информация'), {
            'fields': (
                'first_name', 'last_name', 'middle_name', 'email',
                'gender', 'date_of_birth', 'phone_number'
            )
        }),
        (_('Рабочая информация'), {
            'fields': (
                'position', 'department', 'hire_date', 'is_active_employee'
            )
        }),
        (_('Описание'), {
            'fields': ('description',),
            'classes': ('wide',)
        }),
        (_('Права доступа'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',)
        }),
        (_('Важные даты'), {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2',
                'first_name', 'last_name', 'middle_name'
            ),
        }),
    )

    inlines = [EmployeeSkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Админка для навыков"""
    list_display = ['name', 'category', 'description_short']
    list_filter = ['category']
    search_fields = ['name', 'category']
    list_editable = ['category']

    def description_short(self, obj):
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description

    description_short.short_description = _('Краткое описание')


@admin.register(EmployeeSkill)
class EmployeeSkillAdmin(admin.ModelAdmin):
    """Админка для связи сотрудник-навык"""
    list_display = ['employee', 'skill', 'level', 'experience_years', 'last_used']
    list_filter = ['skill', 'level', 'last_used']
    search_fields = ['employee__username', 'employee__first_name', 'employee__last_name', 'skill__name']
    autocomplete_fields = ['employee', 'skill']
    list_editable = ['level', 'experience_years']


# Регистрируем модели
admin.site.register(CustomUser, CustomUserAdmin)

from .models import EmployeeImage


class EmployeeImageInline(admin.TabularInline):
    """Inline для отображения изображений сотрудника"""
    model = EmployeeImage
    extra = 1
    fields = ['image', 'order', 'created_at']
    readonly_fields = ['created_at']


class CustomUserAdmin(UserAdmin):
    # ... существующие настройки ...
    inlines = [EmployeeSkillInline, EmployeeImageInline]  # Добавляем ImageInline


@admin.register(EmployeeImage)
class EmployeeImageAdmin(admin.ModelAdmin):
    """Админка для изображений сотрудников"""
    list_display = ['employee', 'order', 'image_preview', 'created_at']
    list_filter = ['created_at']
    search_fields = ['employee__username', 'employee__first_name', 'employee__last_name']
    list_editable = ['order']
    readonly_fields = ['created_at', 'image_preview']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px;" />'
        return "Нет изображения"

    image_preview.allow_tags = True
    image_preview.short_description = _('Превью')