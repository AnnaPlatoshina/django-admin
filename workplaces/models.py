from django.db import models
from employees.models import CustomUser

class Workplace(models.Model):
    """Модель рабочего места"""
    desk_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Номер стола'
    )
    employee = models.OneToOneField(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Сотрудник',
        related_name='workplace'
    )
    additional_info = models.TextField(
        verbose_name='Дополнительная информация',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Рабочее место'
        verbose_name_plural = 'Рабочие места'

    def __str__(self):
        return f"Стол №{self.desk_number}"