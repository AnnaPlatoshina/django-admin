from django.contrib import admin
from .models import CustomUser, Skill, Employee, EmployeeSkill, Workplace, EmployeeImage

admin.site.register(CustomUser)
admin.site.register(Skill)
admin.site.register(Employee)
admin.site.register(EmployeeSkill)
admin.site.register(Workplace)
admin.site.register(EmployeeImage)
