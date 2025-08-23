from django.db import models
from django.contrib.auth.models import AbstractUser


# Пользователь с ролями
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("developer", "Developer"),
        ("tester", "Tester"),
        ("manager", "Manager"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="developer")

    def __str__(self):
        return f"{self.username} ({self.role})"


# Сотрудник
class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    position = models.CharField(max_length=100, verbose_name="Должность")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Зарплата")
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.position}"


# Навыки сотрудника
class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.employee.name} - {self.skill.name} ({self.level})"


# Изображения сотрудника
class EmployeeImage(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="employee_images/")

    def __str__(self):
        return f"{self.employee.name} image"
