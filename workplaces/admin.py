from django.contrib import admin
from django.utils.html import format_html
from .models import Workplace

@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    list_display = ('number', 'employee', 'status')

    def status(self, obj):
        # Получаем соседние столы
        neighbors = Workplace.objects.filter(number__in=[obj.number - 1, obj.number + 1])
        warning = False
        for neighbor in neighbors:
            if neighbor.employee:
                if (obj.employee and
                   ((obj.employee.role == 'developer' and neighbor.employee.role == 'tester') or
                    (obj.employee.role == 'tester' and neighbor.employee.role == 'developer'))):
                    warning = True
                    break
        # Возвращаем цветной текст
        if warning:
            return format_html('<span style="color: red;">❌ Конфликт с соседями</span>')
        return format_html('<span style="color: green;">✅ Всё ок</span>')
    status.short_description = 'Статус соседних мест'
