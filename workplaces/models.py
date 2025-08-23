from django.db import models
from employees.models import CustomUser
from django.core.exceptions import ValidationError

class Workplace(models.Model):
    number = models.PositiveIntegerField(unique=True)
    employee = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    def clean(self):
        # Проверка соседних столов
        if self.employee:
            # Получаем всех соседей (номер стола ±1)
            neighbors = Workplace.objects.filter(number__in=[self.number - 1, self.number + 1])
            for neighbor in neighbors:
                if neighbor.employee:
                    if (self.employee.role == 'developer' and neighbor.employee.role == 'tester') or \
                       (self.employee.role == 'tester' and neighbor.employee.role == 'developer'):
                        raise ValidationError(f"Нельзя посадить {self.employee} рядом с {neighbor.employee}")

    def save(self, *args, **kwargs):
        self.clean()  # Проверяем перед сохранением
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Стол {self.number} — {self.employee}"
