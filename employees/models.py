from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="skills")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(default=1)  # уровень от 1 до 10

    class Meta:
        unique_together = ('employee', 'skill')

    def __str__(self):
        return f"{self.employee.username} - {self.skill.name} (Level {self.level})"


class EmployeeImage(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='employee_images/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.employee.username} image"
