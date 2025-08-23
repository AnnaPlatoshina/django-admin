from django.db import models
from django.core.exceptions import ValidationError

# Валидатор соседних столов
def no_adjacent_tables(employee):
    if not employee.table:
        return
    adjacent_numbers = [employee.table.number - 1, employee.table.number + 1]
    conflicting = Employee.objects.filter(table__number__in=adjacent_numbers)
    if conflicting.exists():
        raise ValidationError(
            f"Стол {employee.table.number} соседствует с другим занятым столом."
        )

class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f"Table {self.number}"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, blank=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)

    def clean(self):
        no_adjacent_tables(self)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
