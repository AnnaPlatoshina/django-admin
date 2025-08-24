from django.db import models
from django.contrib.auth.models import AbstractUser

# Пользователь
class CustomUser(AbstractUser):
    pass  # Можно добавить поля, если нужно

# Навык
class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Сотрудник
class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Навыки сотрудника
class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee} - {self.skill}"

# Место работы
class Workplace(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

# Изображения сотрудников
class EmployeeImage(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='employee_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.employee}"
