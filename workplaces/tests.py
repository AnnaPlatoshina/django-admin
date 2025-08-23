from django.test import TestCase
from .models import Table, Employee
from django.core.exceptions import ValidationError

class TableValidatorTests(TestCase):
    def setUp(self):
        self.table1 = Table.objects.create(number=1)
        self.table2 = Table.objects.create(number=2)

    def test_adjacent_tables_validator(self):
        employee1 = Employee.objects.create(name="Alice", table=self.table1)
        employee2 = Employee(name="Bob", table=self.table2)

        with self.assertRaises(ValidationError):
            employee2.full_clean()  # Проверка валидатора
